LANGUAGES = {
    'en': {
        'hello': '👋 Hello, {user}!',
        'balance': '💰 Balance: {balance} EUR',
        'basket': '🛒 Basket: {items} item(s)',
        'overpay': '💳 Send the exact amount. Overpayments will be credited.',
        'shop': '🛍 Shop',
        'profile': '👤 Profile',
        'top_up': '💸 Top Up',
        'channel': '📢 Channel',
        'support': '🆘 Support',
        'language': '🌐 Language',
        'admin_panel': '🎛 Admin Panel',
        'choose_language': 'Please choose a language',
        'invoice_message': (
            '🧾 <b>Payment Invoice Created</b>\n\n'
            '<b>Amount:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Payment Address:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Expires At:</b> {expires_at} LT\n'
            '⚠️ <b>Payment must be completed within 30 minutes of invoice creation.</b>\n\n'
            '❗️ <b>Important:</b> Send <u>exactly</u> this amount of {currency}.\n\n'
            '✅ <b>Confirmation is automatic via webhook after network confirmation.</b>'
        ),
        'i_paid': 'I paid',
        'cancel': 'Cancel',
    },
    'ru': {
        'hello': '👋 Привет, {user}!',
        'balance': '💰 Баланс: {balance} EUR',
        'basket': '🛒 Корзина: {items} шт.',
        'overpay': '💳 Отправьте точную сумму. Переплаты будут зачислены.',
        'shop': '🛍 Магазин',
        'profile': '👤 Профиль',
        'top_up': '💸 Пополнить',
        'channel': '📢 Канал',
        'support': '🆘 Поддержка',
        'language': '🌐 Язык',
        'admin_panel': '🎛 Админ панель',
        'choose_language': 'Пожалуйста, выберите язык',
        'invoice_message': (
            '🧾 <b>Создан инвойс на оплату</b>\n\n'
            '<b>Сумма:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Адрес оплаты:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Действителен до:</b> {expires_at} LT\n'
            '⚠️ <b>Оплата должна быть выполнена в течение 30 минут после создания.</b>\n\n'
            '❗️ <b>Важно:</b> Отправьте <u>ровно</u> это количество {currency}.\n\n'
            '✅ <b>Подтверждение произойдет автоматически через вебхук после подтверждения сети.</b>'
        ),
        'i_paid': 'Я оплатил',
        'cancel': 'Отмена',
    },
    'lt': {
        'hello': '👋 Sveiki, {user}!',
        'balance': '💰 Balansas: {balance} EUR',
        'basket': '🛒 Krepšelis: {items} prekės',
        'overpay': '💳 Siųskite tikslią sumą. Permokos bus įskaitytos.',
        'shop': '🛍 Parduotuvė',
        'profile': '👤 Profilis',
        'top_up': '💸 Papildyti',
        'channel': '📢 Kanalu',
        'support': '🆘 Pagalba',
        'language': '🌐 Kalba',
        'admin_panel': '🎛 Admin pultas',
        'choose_language': 'Pasirinkite kalbą',
        'invoice_message': (
            '🧾 <b>Sukurta mokėjimo sąskaita</b>\n\n'
            '<b>Suma:</b> <code>{amount}</code> {currency}\n'
            '🏦 <b>Mokėjimo adresas:</b>\n<code>{address}</code>\n\n'
            '⏳ <b>Galioja iki:</b> {expires_at} LT\n'
            '⚠️ <b>Mokėjimą reikia atlikti per 30 minučių nuo sąskaitos sukūrimo.</b>\n\n'
            '❗️ <b>Svarbu:</b> Nusiųskite <u>tiksliai</u> tiek {currency} į šį adresą.\n\n'
            '✅ <b>Patvirtinimas vyks automatiškai per webhook po tinklo patvirtinimo.</b>'
        ),
        'i_paid': 'Apmokėjau',
        'cancel': 'Atšaukti',
    },
}

def t(lang: str, key: str, **kwargs) -> str:
    lang_data = LANGUAGES.get(lang, LANGUAGES['en'])
    template = lang_data.get(key, '')
    return template.format(**kwargs)
