import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from keyboards import report_or_problem, Pro_floor  # Reply keyboardlar
import asyncio
import keyboards as kb
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
GROUP_ID = os.getenv('GROUP_ID')
TOPIC_REPORT = os.getenv("TOPIC_REPORT")
TOPIC_PROBLEM = os.getenv("TOPIC_PROBLEM")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ✅ FSM uchun klass yaratamiz
class ReportState(StatesGroup):
    slecting_build = State()
    selecting_zone = State()  # Zona tanlash holati
    sending_message = State()  # Xabar yuborish holati
# Start komandasi




@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # await message.answer("Hisobot yoki Muammo tanlang:", reply_markup=report_or_problem)

    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfKh3oQqskezYPaYwMks4PEOE3qbNugxjzIw&s",
        
    )
    await message.reply(f"Salom {message.from_user.full_name} befit texnik botiga xush kelibsiz\n",reply_markup= kb.main)
    if message.from_user.id == ADMIN_ID:
        await message.answer(f"Siz bot adminisiz", reply_markup= kb.main_admin)

# Lug‘atlar foydalanuvchining tanlovlarini saqlash uchun
selected_building = {}
selected_zone = {}
user_last_message = {}

# ✅ Asosiy menyu
@dp.message(F.text == "Asosiy menu")
async def asosiy_menyu(message: Message):
    await message.answer("Binoni tanlang", reply_markup=kb.main_admin)

# ✅ Binoni tanlash
@dp.message(F.text.in_(["Befit Pro", "Befit Sky"]))
async def select_building(message: types.Message, state: FSMContext):

    bino_nomi = message.text
    user_id = message.from_user.id
    await state.update_data(selected_building=message.text)
    # selected_building[user_id] = message.text  # To‘g‘rilangan lug‘atga yozish
    if bino_nomi == "Befit Pro":
        if user_id == 553240994:
            await message.answer("Tanla Umid otchot berasanmi, yo problemang bormi:", reply_markup=kb.report_or_problem)
        elif user_id == 983622997:
            await message.answer("Najmiddin, tanla", reply_markup=kb.report_or_problem)
        else:
            await message.answer(f"Statusni tanlang", reply_markup=kb.report_or_problem)
    elif bino_nomi == "Befit Sky":
        if user_id == 553240994:
            await message.answer("Tanla Umid otchot berasanmi, yo problemang bormi:", reply_markup=kb.sky_rep_to_prob)
        elif user_id == 983622997:
            await message.answer("Najmiddin, tanla", reply_markup=kb.sky_rep_to_prob)
        else:
            await message.answer(f"Statusni tanlang", reply_markup=kb.sky_rep_to_prob)        
# ✅ Sky zonalari inline tugmalari
sky_zones = ["Marketing", "Bugalteriya", "Muzokara", "Stuff zona","Salateriya", "Oshxona", "Reception", 
             "Sotuv bo'limi","Vip koridor","Functional", "Body & Mind","Pilates","Rehab","Crio",
             "E.Kiyinish xonasi","A. Kiyinish xonasi","Basseyn", "Shit","Trenerlar x_1","Trenerlar x_2","Trenajor zal"]
buttons = [InlineKeyboardButton(text=zone, callback_data=f"abc_{zone}") for zone in sky_zones]
inline_sky = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i+3] for i in range(0, len(buttons), 3)])

# ✅ "Hisobot" yoki "Muammo"ni tanlash
@dp.message(F.text.in_(["Hisobot", "Muammo"]))
async def select_report_or_problem(message: Message, state: FSMContext):
    user_choice = "hisobot" if message.text == "Hisobot" else "muammo"
    await state.update_data(choice=user_choice)
    await state.set_state(ReportState.selecting_zone)

    await message.answer("Qavatni tanlang:", reply_markup=Pro_floor)
# ==------------------------------------------------------------------
@dp.message(F.text.in_(["Hisobot sky", "Muammo sky"]))
async def select_report_or_problem(message: Message, state: FSMContext):
    user_choice = "hisobot" if message.text == "Hisobot sky" else "muammo"
    
    # ✅ Foydalanuvchi tanlovini FSM-ga saqlaymiz
    await state.update_data(choice=user_choice)
    
    # ✅ Keyingi holatga o‘tamiz
    await state.set_state(ReportState.selecting_zone)
    
    await message.answer("Zonani tanlang:", reply_markup=inline_sky)  # Qavat tugmalarini chiqarish

# ✅ Ortga tugmasi
@dp.message(F.text == "Ortga")
async def go_back_to_report_or_problem(message: types.Message):
    await message.answer("Hisobot yoki Muammo tanlang:", reply_markup=report_or_problem)

# ✅ Qavatni tanlash va zonalarni chiqarish
@dp.message(F.text.in_({"-1", "1", "2", "3", "4","Basseyn","Ko'cha"}))
async def process_floor_selection(message: types.Message):
    floor = message.text

    if floor in kb.inline_buttons:
        await message.answer(f"{floor}-qavat zonalarini tanlang:", reply_markup=kb.inline_buttons[floor])

# ✅ Zona tanlash

user_zone_info = {}

@dp.callback_query(F.data.startswith(("zone_", "abc_")))
async def process_zone_selection(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    data = callback.data

    if data.startswith("zone_"):
        building_name = "Befit Pro"
        zone_name = data.replace("zone_", "")
    elif data.startswith("abc_"):
        building_name = "Befit Sky"
        zone_name = data.replace("abc_", "")
    else:
        await callback.answer("Noto‘g‘ri ma’lumot!")
        return

    # FSM-ga tanlangan binoni va zonani saqlaymiz
    await state.update_data(selected_building=building_name, selected_zone=zone_name)
    user_zone_info[user_id] = (building_name, zone_name)  # Dictionary-ga saqlaymiz

    # Guruhga bino + zona nomi bilan xabar yuboramiz
    user_data = await state.get_data()
    choice = user_data.get("choice")
    topic_id = TOPIC_REPORT if choice == "hisobot" else TOPIC_PROBLEM

    await bot.send_message(
        GROUP_ID,
        f"📍 *{building_name} – {zone_name}*.",
        message_thread_id=topic_id,
        parse_mode="Markdown"
    )

    await state.set_state(ReportState.sending_message)
    await callback.message.answer(f"{building_name} – {zone_name} uchun xabar yuboring:")
    await callback.answer()


# -----------------------------------------------
# ✅ Xabar yuborilganda forward qilish
@dp.message(ReportState.sending_message)
async def save_and_forward_message(message: Message, state: FSMContext):
    user_data = await state.get_data()
    choice = user_data.get("choice")
    topic_id = TOPIC_REPORT if choice == "hisobot" else TOPIC_PROBLEM

    # Forward qilamiz
    await bot.forward_message(
        chat_id=GROUP_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        message_thread_id=topic_id
    )
    await message.answer("✅ Xabar jo'natildi")
    # ✅ Foydalanuvchini yana zona tanlashga qaytaramiz
    await state.set_state(ReportState.selecting_zone)

# ortga tugmasi
@dp.message(F.text == "Ortga")
async def go_back_to_report_or_problem(message: types.Message):
    await message.answer("Hisobot yoki Muammo tanlang:", reply_markup=report_or_problem)

# ===================================================================================



async def main():
    # dp.include_router(router)
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Bot to‘xtatildi!")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to‘xtatildi.")