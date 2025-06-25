import importlib
import subprocess
import sys

REQUIRED_MODULES = [
    "yoomoney",
    "aiogram",
    "sqlalchemy",
    "requests",
    "alembic",
    "solana",
    "xrpl",
    "web3",
    "bitcoinrpc",
    "flask",
]


def ensure_requirements() -> None:
    """Install required packages if any are missing."""
    missing = []
    for module in REQUIRED_MODULES:
        try:
            importlib.import_module(module)
        except Exception:
            missing.append(module)

    if missing:
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
        ])


from threading import Thread
from bot import start_bot
from bot.ipn_server import app as ipn_app


def run_ipn() -> None:
    ipn_app.run(host="0.0.0.0", port=8000)

if __name__ == '__main__':
    ensure_requirements()
    Thread(target=run_ipn, daemon=True).start()
    start_bot()
