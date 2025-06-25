from flask import Flask, request, abort
import datetime
import hmac
import hashlib

from bot.misc import EnvKeys, TgConfig
from bot.database import Database
from bot.database.models.main import UnfinishedOperations
from bot.database.methods import (
    finish_operation,
    create_operation,
    update_balance,
    get_user_referral,
)
from bot.logger_mesh import logger

app = Flask(__name__)


def verify_signature(data: bytes, signature: str | None) -> bool:
    if not EnvKeys.NOWPAYMENTS_IPN_SECRET:
        return True
    if not signature:
        return False
    calc = hmac.new(
        EnvKeys.NOWPAYMENTS_IPN_SECRET.encode(),
        data,
        hashlib.sha512,
    ).hexdigest()
    return hmac.compare_digest(calc, signature)


@app.route("/nowpayments-ipn", methods=["POST"])
def nowpayments_ipn():
    if not verify_signature(request.data, request.headers.get("x-nowpayments-sig")):
        abort(400)

    data = request.get_json(silent=True) or {}
    payment_id = str(data.get("payment_id"))
    status = data.get("payment_status")
    if not payment_id or not status:
        return "", 400

    if status in ("finished", "confirmed", "sending", "paid", "partially_paid"):
        session = Database().session
        record = (
            session.query(UnfinishedOperations)
            .filter(UnfinishedOperations.operation_id == payment_id)
            .first()
        )
        if record:
            value = record.operation_value
            user_id = record.user_id
            finish_operation(payment_id)
            formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            create_operation(user_id, value, formatted_time)
            update_balance(user_id, value)

            referral_id = get_user_referral(user_id)
            if referral_id and TgConfig.REFERRAL_PERCENT != 0:
                referral_operation = round((TgConfig.REFERRAL_PERCENT / 100) * value)
                update_balance(referral_id, referral_operation)

            logger.info(
                "NOWPayments IPN confirmed payment %s for user %s", payment_id, user_id
            )
    return "", 200
