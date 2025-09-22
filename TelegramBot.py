from dotenv import load_dotenv
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio
import functions
from time import sleep

load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')
MyTGaccount = int(os.environ.get('MyTGaccount'))
dp = Dispatcher()

ALLOWED_USERS = [MyTGaccount]

# --- MENU ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Get System Metrics")],
        [KeyboardButton(text="📊 Get Aqua Metrics")],
        [KeyboardButton(text="📡 Get Status")],
        [KeyboardButton(text="⚙️ Management")],
    ],
    resize_keyboard=True
)


def is_allowed(user_id: int) -> bool:
    return user_id in ALLOWED_USERS


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not is_allowed(message.from_user.id):
        return  # 🚫 silently ignore
    await message.answer("✅ Welcome, authorized user!")


@dp.message(lambda msg: msg.text == "📊 Get System Metrics")
async def get_SystemMetrics(message: types.Message):
    # Example metrics
    metrics = functions.get_core_data()
    if not metrics:
        metrics = "No Data"
    await message.answer(f"📊 System Metrics:\n{metrics}")


@dp.message(lambda msg: msg.text == "📊 Get Aqua Metrics")
async def get_AquaMetrics(message: types.Message):
    # Example metrics
    metrics = functions.getAquaMetrics()
    if not metrics:
        metrics = "No Data"
    else:
        temp = metrics[0]
        ph = metrics[1]
        tds = metrics[2]
        metrics = f"temp: {temp}, °C\nPH: {ph}\nTDS: {tds}"
    await message.answer(f"📊 Curent Aqua Metrics:\n{metrics}")


@dp.message(lambda msg: msg.text == "📡 Get Status")
async def get_status(message: types.Message):
    # Example status
    result = functions.getver()
    network = functions.getNetworksData()
    status = f"✅ BD Engine: {result[0]}\n✅ Python: {result[1]}\n✅ IP address: {network}"
    await message.answer(f"📡 Status Report:\n{status}")


# --- MANAGEMENT MENU ---
management_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="▶️ Start CO2 Diffuser"), KeyboardButton(text="🛑 Stop CO2 Diffuser"),
         KeyboardButton(text="🔄 CO2 Auto")],
        [KeyboardButton(text="▶️ Start O2 Diffuser"), KeyboardButton(text="🛑 Stop O2 Diffuser"),
         KeyboardButton(text="🔄 O2 Auto")],

        [KeyboardButton(text="▶️ Start UV"), KeyboardButton(text="🛑 Stop UV"),
         KeyboardButton(text="🔄 UV Auto")],
        [KeyboardButton(text="▶️ Start Heating"), KeyboardButton(text="🛑 Stop Heating"),
         KeyboardButton(text="🔄 Heating Auto")],

        [KeyboardButton(text="▶️ Master Light ON"), KeyboardButton(text="🛑 Master Light OFF"),
         KeyboardButton(text="🔄 Master Light Auto")],
        [KeyboardButton(text="▶️ Projector Light ON"), KeyboardButton(text="🛑 Projector Light OFF"),
         KeyboardButton(text="🔄 Projector Light Auto")],

        [KeyboardButton(text="▶️ Plant Light ON"), KeyboardButton(text="🛑 Plant Light OFF"),
         KeyboardButton(text="🔄 Plant Light Auto")],
        [KeyboardButton(text="▶️ Moon Light ON"), KeyboardButton(text="🛑 Moon Light OFF"),
         KeyboardButton(text="🔄 Moon Light Auto")],

        [KeyboardButton(text="⬅️ Back")],
    ],
    resize_keyboard=True
)


@dp.message(lambda msg: msg.text == "⚙️ Management")
async def management(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    await message.answer("⚙️ Management Options:", reply_markup=management_menu)


@dp.message(lambda msg: msg.text in [
    "▶️ Start CO2 Diffuser", "🛑 Stop CO2 Diffuser", "🔄 CO2 Auto",
    "▶️ Start O2 Diffuser", "🛑 Stop O2 Diffuser", "🔄 O2 Auto",
    "▶️ Start UV", "🛑 Stop UV", "🔄 UV Auto",
    "▶️ Start Heating", "🛑 Stop Heating", "🔄 Heating Auto",
    "▶️ Master Light ON", "🛑 Master Light OFF", "🔄 Master Light Auto",
    "▶️ Projector Light ON", "🛑 Projector Light OFF", "🔄 Projector Light Auto",
    "▶️ Plant Light ON", "🛑 Plant Light OFF", "🔄 Plant Light Auto",
    "▶️ Moon Light ON", "🛑 Moon Light OFF", "🔄 Moon Light Auto",
])
async def handle_management(message: types.Message):
    if not is_allowed(message.from_user.id):
        return

    actions = {
        # CO2 Diffuser
        "▶️ Start CO2 Diffuser": "✅ CO2 Diffuser started successfully!",
        "🛑 Stop CO2 Diffuser": "✅ CO2 Diffuser stopped successfully!",
        "🔄 CO2 Auto": "✅ CO2 Diffuser set to AUTO successfully!",

        # O2 Diffuser
        "▶️ Start O2 Diffuser": "✅ O2 Diffuser started successfully!",
        "🛑 Stop O2 Diffuser": "✅ O2 Diffuser stopped successfully!",
        "🔄 O2 Auto": "✅ O2 Diffuser set to AUTO successfully!",

        # UV
        "▶️ Start UV": "✅ UV started successfully!",
        "🛑 Stop UV": "✅ UV stopped successfully!",
        "🔄 UV Auto": "✅ UV set to AUTO successfully!",

        # Heating
        "▶️ Start Heating": "✅ Heating started successfully!",
        "🛑 Stop Heating": "✅ Heating stopped successfully!",
        "🔄 Heating Auto": "✅ Heating set to AUTO successfully!",

        # Master Light
        "▶️ Master Light ON": "✅ Master Light turned ON successfully!",
        "🛑 Master Light OFF": "✅ Master Light turned OFF successfully!",
        "🔄 Master Light Auto": "✅ Master Light set to AUTO successfully!",

        # Projector Light
        "▶️ Projector Light ON": "✅ Projector Light turned ON successfully!",
        "🛑 Projector Light OFF": "✅ Projector Light turned OFF successfully!",
        "🔄 Projector Light Auto": "✅ Projector Light set to AUTO successfully!",

        # Plant Light
        "▶️ Plant Light ON": "✅ Plant Light turned ON successfully!",
        "🛑 Plant Light OFF": "✅ Plant Light turned OFF successfully!",
        "🔄 Plant Light Auto": "✅ Plant Light set to AUTO successfully!",

        # Moon Light
        "▶️ Moon Light ON": "✅ Moon Light turned ON successfully!",
        "🛑 Moon Light OFF": "✅ Moon Light turned OFF successfully!",
        "🔄 Moon Light Auto": "✅ Moon Light set to AUTO successfully!",
    }

    mssg = actions.get(message.text, "⚠️ Unknown action")
    functions.setOptionsFromTG(mssg)
    await message.answer(mssg)


@dp.message(lambda msg: msg.text == "⬅️ Back")
async def back_to_main(message: types.Message):
    if not is_allowed(message.from_user.id):
        return
    await message.answer("🔙 Back to main menu", reply_markup=main_menu)


# --- MAIN ENTRY ---
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
