import telebot
from telebot import types

# ── CONFIG ──────────────────────────────────────────
TOKEN    = "8688094007:AAGkcFOOJtC-geBVLRQW8hSiOJM08Ckki0Y"
ADMIN_ID = 6861320052
CONTACT  = "@ubaidbhat03"
CHANNEL  = "@GHOTLIOS"

bot = telebot.TeleBot(TOKEN)

# ── USER LANGUAGE STORE ──────────────────────────────
user_lang = {}   # uid → "ar" / "pt" / "hi" / "en" / "ur" / "rhu"
pending   = {}   # uid → {plan, price, lang}

# ── PLANS ───────────────────────────────────────────
PLANS = [
    ("1 Week • 1 Device",     "₹700",  "$7",   "700 ر.س"),
    ("1 Week • 2 Devices",    "₹1000", "$10",  "1000 ر.س"),
    ("2 Weeks • 1 Device",    "₹1000", "$10",  "1000 ر.س"),
    ("2 Weeks • 2 Devices",   "₹1500", "$15",  "1500 ر.س"),
    ("1 Month • 1 Device",    "₹2200", "$22",  "2200 ر.س"),
    ("1 Month • 2 Devices",   "₹2700", "$27",  "2700 ر.س"),
    ("2 Months • 1 Device",   "₹3000", "$30",  "3000 ر.س"),
    ("2 Months • 2 Devices",  "₹3500", "$35",  "3500 ر.س"),
    ("Permanent • 1 Device",  "₹5200", "$52",  "5200 ر.س"),
    ("Permanent • 2 Devices", "₹6000", "$60",  "6000 ر.س"),
]

# ── TRANSLATIONS ─────────────────────────────────────
# price_key index in PLANS tuple: 1=INR, 2=USD, 3=Arabic SAR
T = {
    # ── ARABIC ───────────────────────────────────────
    "ar": {
        "welcome": (
            "💀 *أهلاً بك يا {name} في GHOST MODER!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *اللعبة:* Last Island of Survival\n"
            "⚡ *المميزات:* ESP، بدون ارتداد، طيران، +50 ميزة\n"
            "🛡️ *تجاوز الحماية:* ✅\n"
            "📱 *جميع الأجهزة:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "اختر من الأسفل 👇"
        ),
        "buy":      "💎 شراء مفتاح",
        "features": "📋 المميزات",
        "channel":  "📢 القناة",
        "support":  "📲 الدعم",
        "plans_title": "💎 *اختر خطتك:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *تم اختيار الخطة!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *الخطة:* {plan}\n"
            "💰 *السعر:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *للحصول على المفتاح تواصل:*\n"
            "{contact}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *شكراً لثقتك بنا*\n"
            "*نتمنى أن تستمتع بخدمتنا* 💀"
        ),
        "price_key": 3,
        "back": "🔙 رجوع",
        "plans_back": "🔙 الخطط",
        "features_text": (
            "👑 *مميزات GHOST MODER* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* ماستر، صندوق 3D، هيكل، صحة، مسافة\n"
            "🔫 *قتال:* بدون ارتداد، رصاصة سحرية، اختراق الجدران\n"
            "🌾 *زراعة تلقائية:* أشجار، كبريت، حجر، حديد\n"
            "🏗️ *بناء:* بناء إجباري، بناء تحت الماء\n"
            "✈️ *حركة:* طيران، المشي تحت الماء\n"
            "👻 *خاص:* شبح، لاعب صغير، عرض iPad\n"
            "🛡️ *حماية:* تجاوز الحماية، منع الكشف\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*+50 ميزة إجمالاً* ⚡"
        ),
    },

    # ── PORTUGUESE ───────────────────────────────────
    "pt": {
        "welcome": (
            "💀 *Bem-vindo, {name}, ao GHOST MODER!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *Jogo:* Last Island of Survival\n"
            "⚡ *Recursos:* ESP, Sem Recuo, Voar, +50 funções\n"
            "🛡️ *Anti-cheat Bypass:* ✅\n"
            "📱 *Todos os Dispositivos:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Escolha uma opção abaixo 👇"
        ),
        "buy":      "💎 Comprar Chave",
        "features": "📋 Recursos",
        "channel":  "📢 Canal",
        "support":  "📲 Suporte",
        "plans_title": "💎 *Escolha seu plano:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *Plano Selecionado!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *Plano:* {plan}\n"
            "💰 *Preço:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *Para receber a chave, contate:*\n"
            "{contact}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *Obrigado por confiar em nós!*\n"
            "*Esperamos que goste do serviço* 💀"
        ),
        "price_key": 2,
        "back": "🔙 Voltar",
        "plans_back": "🔙 Planos",
        "features_text": (
            "👑 *RECURSOS GHOST MODER* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* Master, Box 3D, Esqueleto, Saúde\n"
            "🔫 *Combate:* Sem Recuo, Bala Mágica, Penetração\n"
            "🌾 *Auto Farm:* Árvore, Enxofre, Pedra, Ferro\n"
            "🏗️ *Build:* Force Build, Build Subaquático\n"
            "✈️ *Movimento:* Voar, Andar na Água\n"
            "👻 *Especial:* Super Invisível, iPad View\n"
            "🛡️ *Proteção:* Bypass Anti-cheat\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*+50 Recursos no Total* ⚡"
        ),
    },

    # ── HINDI ────────────────────────────────────────
    "hi": {
        "welcome": (
            "💀 *{name}, GHOST MODER mein aapka swagat hai!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *Game:* Last Island of Survival\n"
            "⚡ *Features:* ESP, No Recoil, Fly, +50 features\n"
            "🛡️ *Anti Cheat Bypass:* ✅\n"
            "📱 *All Devices:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Neeche se choose karo 👇"
        ),
        "buy":      "💎 Key Kharido",
        "features": "📋 Features",
        "channel":  "📢 Channel",
        "support":  "📲 Support",
        "plans_title": "💎 *Apna plan choose karo:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *Plan Select Ho Gaya!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *Plan:* {plan}\n"
            "💰 *Price:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *Key ke liye contact karo:*\n"
            "{contact}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *THANKS FOR TRUSTING*\n"
            "*HOPE YOU LIKE OUR SERVICE* 💀"
        ),
        "price_key": 1,
        "back": "🔙 Wapas",
        "plans_back": "🔙 Plans",
        "features_text": (
            "👑 *GHOST MODER FEATURES* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* Master, Box 3D, Skeleton, Health, Distance\n"
            "🔫 *Combat:* No Recoil, Magic Bullet, Wall Penetration\n"
            "🌾 *Auto Farm:* Tree, Sulfur, Stone, Iron, Titanium\n"
            "🏗️ *Build:* Force Build, Underwater Build\n"
            "✈️ *Movement:* Player Fly, Walk Underwater\n"
            "👻 *Special:* Invisible, Tiny Player, iPad View\n"
            "🛡️ *Protection:* Anti Cheat Bypass, Block Detection\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*50+ Features Total* ⚡"
        ),
    },

    # ── ENGLISH ──────────────────────────────────────
    "en": {
        "welcome": (
            "💀 *Welcome, {name}, to GHOST MODER!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *Game:* Last Island of Survival\n"
            "⚡ *Features:* ESP, No Recoil, Fly, +50 Features\n"
            "🛡️ *Anti-Cheat Bypass:* ✅\n"
            "📱 *All Devices:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Choose an option below 👇"
        ),
        "buy":      "💎 Buy Key",
        "features": "📋 Features",
        "channel":  "📢 Channel",
        "support":  "📲 Support",
        "plans_title": "💎 *Choose your plan:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *Plan Selected!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *Plan:* {plan}\n"
            "💰 *Price:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *To receive your key, contact:*\n"
            "{contact}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *Thanks for trusting us!*\n"
            "*Enjoy the service* 💀"
        ),
        "price_key": 2,
        "back": "🔙 Back",
        "plans_back": "🔙 Plans",
        "features_text": (
            "👑 *GHOST MODER FEATURES* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* Master, Box 3D, Skeleton, Health, Distance\n"
            "🔫 *Combat:* No Recoil, Magic Bullet, Wall Penetration\n"
            "🌾 *Auto Farm:* Tree, Sulfur, Stone, Iron, Titanium\n"
            "🏗️ *Build:* Force Build, Underwater Build\n"
            "✈️ *Movement:* Player Fly, Walk Underwater\n"
            "👻 *Special:* Invisible, Tiny Player, iPad View\n"
            "🛡️ *Protection:* Anti-Cheat Bypass, Block Detection\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*50+ Features Total* ⚡"
        ),
    },

    # ── URDU ─────────────────────────────────────────
    "ur": {
        "welcome": (
            "💀 *{name}، GHOST MODER میں خوش آمدید!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *گیم:* Last Island of Survival\n"
            "⚡ *فیچرز:* ESP، نو ریکوئل، اڑنا، +50 فیچرز\n"
            "🛡️ *اینٹی چیٹ بائی پاس:* ✅\n"
            "📱 *تمام ڈیوائسز:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "نیچے سے آپشن چنیں 👇"
        ),
        "buy":      "💎 کی خریدیں",
        "features": "📋 فیچرز",
        "channel":  "📢 چینل",
        "support":  "📲 سپورٹ",
        "plans_title": "💎 *اپنا پلان چنیں:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *پلان منتخب ہو گیا!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *پلان:* {plan}\n"
            "💰 *قیمت:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *کی لینے کے لیے رابطہ کریں:*\n"
            "{contact}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *ہم پر اعتماد کا شکریہ!*\n"
            "*امید ہے آپ کو سروس پسند آئے گی* 💀"
        ),
        "price_key": 1,
        "back": "🔙 واپس",
        "plans_back": "🔙 پلانز",
        "features_text": (
            "👑 *GHOST MODER فیچرز* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* ماسٹر، باکس 3D، اسکیلٹن، ہیلتھ، دوری\n"
            "🔫 *لڑائی:* نو ریکوئل، میجک بلٹ، وال پینٹریشن\n"
            "🌾 *آٹو فارم:* درخت، سلفر، پتھر، لوہا، ٹائٹینیم\n"
            "🏗️ *بلڈ:* فورس بلڈ، پانی کے اندر بلڈ\n"
            "✈️ *حرکت:* اڑنا، پانی میں چلنا\n"
            "👻 *خاص:* انویزیبل، چھوٹا کھلاڑی، iPad ویو\n"
            "🛡️ *تحفظ:* اینٹی چیٹ بائی پاس، ڈیٹیکشن بلاک\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*50+ فیچرز کل* ⚡"
        ),
    },

    # ── ROMAN URDU / HINDUSTANI ───────────────────────
    "rhu": {
        "welcome": (
            "💀 *{name}, GHOST MODER mein khush amdeed!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎮 *Game:* Last Island of Survival\n"
            "⚡ *Features:* ESP, No Recoil, Urdna, +50 Features\n"
            "🛡️ *Anti Cheat Bypass:* ✅\n"
            "📱 *Sab Devices:* ✅\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Neeche se option chuno 👇"
        ),
        "buy":      "💎 Key Kharido",
        "features": "📋 Features",
        "channel":  "📢 Channel",
        "support":  "📲 Support",
        "plans_title": "💎 *Apna plan chuno:*\n━━━━━━━━━━━━━━━━━━━━━━\n",
        "plan_selected": (
            "✅ *Plan Select Ho Gaya!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "📦 *Plan:* {plan}\n"
            "💰 *Qeemat:* {price}\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🔑 *Key lene ke liye rabta karo:*\n"
            "{contact}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "🙏 *Shukriya trust karne ka!*\n"
            "*Umeed hai service pasand aaye* 💀"
        ),
        "price_key": 1,
        "back": "🔙 Wapas",
        "plans_back": "🔙 Plans",
        "features_text": (
            "👑 *GHOST MODER FEATURES* 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👁️ *ESP:* Master, Box 3D, Skeleton, Health, Doori\n"
            "🔫 *Ladai:* No Recoil, Magic Bullet, Wall Penetration\n"
            "🌾 *Auto Farm:* Darakht, Sulfur, Pathar, Loha, Titanium\n"
            "🏗️ *Build:* Force Build, Paani ke andar Build\n"
            "✈️ *Harkat:* Urdna, Paani mein chalna\n"
            "👻 *Khaas:* Invisible, Chota Player, iPad View\n"
            "🛡️ *Tahaffuz:* Anti Cheat Bypass, Detection Block\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "*50+ Features kul* ⚡"
        ),
    },
}

# ── BANNER PATH ──────────────────────────────────────
import os
BANNER_PATH = "Ghost.png"

# ── /start → BANNER + LANGUAGE SELECT ────────────────
@bot.message_handler(commands=['start'])
def start(msg):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🇸🇦 العربية  (Arabic)",        callback_data="lang_ar"),
        types.InlineKeyboardButton("🇧🇷 Português (Brazil)",        callback_data="lang_pt"),
        types.InlineKeyboardButton("🇮🇳 हिंदी / Hindi",             callback_data="lang_hi"),
        types.InlineKeyboardButton("🇬🇧 English",                   callback_data="lang_en"),
        types.InlineKeyboardButton("🇵🇰 اردو (Urdu)",              callback_data="lang_ur"),
        types.InlineKeyboardButton("🇵🇰 Roman Urdu / Hindustani",  callback_data="lang_rhu"),
    )
    lang_text = (
        "🌍 *Select your language / Apni language chuniye:*\n"
        "اختر لغتك\n"
        "Escolha seu idioma\n"
        "Choose your language\n"
        "زبان منتخب کریں\n"
        "Apni bhasha chuniye"
    )
    # Send banner PNG first, then language menu below it
    if os.path.exists(BANNER_PATH):
        with open(BANNER_PATH, "rb") as photo:
            bot.send_photo(
                msg.chat.id,
                photo,
                caption=lang_text,
                parse_mode="Markdown",
                reply_markup=kb
            )
    else:
        # Fallback if PNG not found
        bot.send_message(
            msg.chat.id,
            lang_text,
            parse_mode="Markdown",
            reply_markup=kb
        )

# ── LANGUAGE SELECTED → MAIN MENU ───────────────────
@bot.callback_query_handler(func=lambda c: c.data.startswith("lang_"))
def set_lang(c):
    lang = c.data.replace("lang_", "")
    user_lang[c.from_user.id] = lang
    # Photo message can't be edited as text — delete it, send fresh
    try:
        bot.delete_message(c.message.chat.id, c.message.message_id)
    except Exception:
        pass
    show_main(c.message, c.from_user, lang, edit=False)

def show_main(msg, user, lang, edit=False):
    t    = T[lang]
    name = user.first_name or "Friend"
    text = t["welcome"].format(name=name)

    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton(t["buy"],      callback_data="buy"),
        types.InlineKeyboardButton(t["features"], callback_data="features"),
        types.InlineKeyboardButton(t["channel"],  url="https://t.me/GHOTLIOS"),
        types.InlineKeyboardButton(t["support"],  url="https://t.me/ubaidbhat03"),
        types.InlineKeyboardButton("🌍 Language / Bhasha", callback_data="change_lang"),
    )
    if edit:
        bot.edit_message_text(text, msg.chat.id, msg.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    else:
        bot.send_message(msg.chat.id, text,
                         parse_mode="Markdown", reply_markup=kb)

# ── CHANGE LANGUAGE ──────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data == "change_lang")
def change_lang(c):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("🇸🇦 العربية",                  callback_data="lang_ar"),
        types.InlineKeyboardButton("🇧🇷 Português",                callback_data="lang_pt"),
        types.InlineKeyboardButton("🇮🇳 Hindi",                    callback_data="lang_hi"),
        types.InlineKeyboardButton("🇬🇧 English",                  callback_data="lang_en"),
        types.InlineKeyboardButton("🇵🇰 اردو (Urdu)",             callback_data="lang_ur"),
        types.InlineKeyboardButton("🇵🇰 Roman Urdu / Hindustani", callback_data="lang_rhu"),
    )
    bot.edit_message_text(
        "🌍 *Select Language:*",
        c.message.chat.id, c.message.message_id,
        parse_mode="Markdown", reply_markup=kb
    )

# ── FEATURES ─────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data == "features")
def features(c):
    lang = user_lang.get(c.from_user.id, "hi")
    t    = T[lang]
    kb   = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(t["buy"],  callback_data="buy"))
    kb.add(types.InlineKeyboardButton(t["back"], callback_data="back"))
    bot.edit_message_text(
        t["features_text"],
        c.message.chat.id, c.message.message_id,
        parse_mode="Markdown", reply_markup=kb
    )

# ── PLANS ─────────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data == "buy")
def show_plans(c):
    lang = user_lang.get(c.from_user.id, "hi")
    t    = T[lang]
    pk   = t["price_key"]

    kb = types.InlineKeyboardMarkup(row_width=1)
    for i, plan in enumerate(PLANS):
        price = plan[pk]
        kb.add(types.InlineKeyboardButton(
            f"{plan[0]} — {price}", callback_data=f"plan_{i}"))
    kb.add(types.InlineKeyboardButton(t["back"], callback_data="back"))

    bot.edit_message_text(
        t["plans_title"] + "👇",
        c.message.chat.id, c.message.message_id,
        parse_mode="Markdown", reply_markup=kb
    )

# ── PLAN SELECTED ─────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data.startswith("plan_"))
def plan_selected(c):
    lang = user_lang.get(c.from_user.id, "hi")
    t    = T[lang]
    pk   = t["price_key"]
    idx  = int(c.data.replace("plan_", ""))
    plan = PLANS[idx]

    name_str = plan[0]
    price    = plan[pk]

    pending[c.from_user.id] = {
        "plan":  name_str,
        "price": price,
        "lang":  lang
    }

    text = t["plan_selected"].format(
        plan=name_str, price=price, contact=CONTACT)

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(t["plans_back"], callback_data="buy"))

    bot.edit_message_text(
        text, c.message.chat.id, c.message.message_id,
        parse_mode="Markdown", reply_markup=kb
    )

    # ── Admin notify ──────────────────────────────────
    uname = f"@{c.from_user.username}" if c.from_user.username else "No username"
    bot.send_message(
        ADMIN_ID,
        f"🛒 *New Order!*\n"
        f"👤 {c.from_user.first_name} ({uname})\n"
        f"🆔 `{c.from_user.id}`\n"
        f"📦 {name_str} — {price}\n"
        f"🌍 Lang: {lang}",
        parse_mode="Markdown"
    )

# ── BACK ─────────────────────────────────────────────
@bot.callback_query_handler(func=lambda c: c.data == "back")
def go_back(c):
    lang = user_lang.get(c.from_user.id, "hi")
    show_main(c.message, c.from_user, lang, edit=True)

# ── ADMIN: SEND KEY ───────────────────────────────────
@bot.message_handler(commands=['sendkey'])
def send_key(msg):
    if msg.from_user.id != ADMIN_ID:
        return
    try:
        parts = msg.text.split(" ", 2)
        uid   = int(parts[1])
        key   = parts[2]
        lang  = pending.get(uid, {}).get("lang", "hi")

        msgs = {
            "ar":  f"🎉 *مفتاحك جاهز!*\n\n🔑 *المفتاح:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
            "pt":  f"🎉 *Sua chave está pronta!*\n\n🔑 *Chave:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
            "hi":  f"🎉 *Teri key ready hai!*\n\n🔑 *Key:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
            "en":  f"🎉 *Your key is ready!*\n\n🔑 *Key:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
            "ur":  f"🎉 *آپ کی کی تیار ہے!*\n\n🔑 *کی:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
            "rhu": f"🎉 *Teri key ready ho gayi!*\n\n🔑 *Key:*\n`{key}`\n\n💀 Ghost Moder\n📢 @GHOTLIOS",
        }
        bot.send_message(uid, msgs.get(lang, msgs["hi"]), parse_mode="Markdown")
        bot.reply_to(msg, f"✅ Key sent to {uid}")
        if uid in pending:
            del pending[uid]
    except Exception as e:
        bot.reply_to(msg, f"❌ Error: {e}\nFormat: /sendkey USER_ID KEY")

# ── RUN ──────────────────────────────────────────────
print("👻 Ghost Moder Bot v4 LIVE — 6 Languages!")
print("🇸🇦 Arabic | 🇧🇷 Portuguese | 🇮🇳 Hindi | 🇬🇧 English | 🇵🇰 Urdu | 🇵🇰 Roman Urdu")
bot.infinity_polling()
