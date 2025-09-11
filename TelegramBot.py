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
dp = Dispatcher()

ALLOWED_USERS = [1078017641]

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
    else:
        print(metrics)
    await message.answer(f"📊 System Metrics:\n{metrics}")

@dp.message(lambda msg: msg.text == "📊 Get Aqua Metrics")
async def get_AquaMetrics(message: types.Message):
    # Example metrics
    metrics = functions.getAquaMetrics()
    if not metrics:
        metrics = "No Data"
    else:
        temp = metrics[0]
        ph   = metrics[1]
        tds  = metrics[2]
        metrics = f"temp: {temp}, °C\nPH: {ph}\nTDS: {tds}"
    await message.answer(f"📊 Curent Aqua Metrics:\n{metrics}")


@dp.message(lambda msg: msg.text == "📡 Get Status")
async def get_status(message: types.Message):
    # Example status
    status = "✅ Service is running\n✅ Database connected"
    await message.answer(f"📡 Status Report:\n{status}")


@dp.message(lambda msg: msg.text == "⚙️ Management")
async def management(message: types.Message):
    # Example management options
    mgmt_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="▶️ Start CO2 Diffuser"), KeyboardButton(text="⏹ Stop CO2 Diffuser"), KeyboardButton(text="🔄 CO2 Auto")],
            [KeyboardButton(text="▶️ Start O2 Diffuser"),  KeyboardButton(text="🛑 Stop O2 Diffuser"),  KeyboardButton(text="🔄 Auto")],
            [KeyboardButton(text="▶️ Start Service"), KeyboardButton(text="⏹ Stop Service")],
            [KeyboardButton(text="▶️ Start Service"), KeyboardButton(text="⏹ Stop Service")],
            [KeyboardButton(text="▶️ Start Service"), KeyboardButton(text="⏹ Stop Service")],
            [KeyboardButton(text="⬅️ Back")],
        ],
        resize_keyboard=True
    )
    await message.answer("⚙️ Management Options:", reply_markup=mgmt_menu)


@dp.message(lambda msg: msg.text == "▶️ Start CO2 Diffuser")
async def start_service(message: types.Message):
    mssg = "✅ CO2 Diffuser started successfully!"
    print(mssg)
    await message.answer(mssg)

@dp.message(lambda msg: msg.text == "⏹ Stop CO2 Diffuser")
async def stop_service(message: types.Message):
    mssg = "✅ CO2 Diffuser stoped successfully!"
    print(mssg)
    await message.answer(mssg)

@dp.message(lambda msg: msg.text == "🔄 CO2 Auto")
async def stop_service(message: types.Message):
    mssg = "✅ CO2 turned to auto successfully!"
    print(mssg)
    await message.answer(mssg)










@dp.message(lambda msg: msg.text == "⬅️ Back")
async def back_to_main(message: types.Message):
    await message.answer("🔙 Back to main menu", reply_markup=main_menu)


# --- MAIN ENTRY ---
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



