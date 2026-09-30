import json
from aiogram import Bot, Dispatcher, types, executor

TOKEN = "8967754983:AAFLVIgjRBWQtUBZGLNmVy6UggRDEiM0bpw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

with open("formulas.json", "r", encoding="utf-8") as f:
    formulas = json.load(f)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text = (
        "👋 Привет! Я бот с формулами за 6-9 класс.\n\n"
        "Просто напиши название формулы, например:\n"
        "• площадь круга\n"
        "• теорема пифагора\n"
        "• дискриминант\n\n"
        "Или напиши /list — покажу все формулы."
    )
    await message.answer(text)

@dp.message_handler(commands=["list"])
async def list_formulas(message: types.Message):
    text = "📚 Все доступные формулы:\n\n"
    for name in formulas.keys():
        text += f"• {name}\n"
    await message.answer(text)

@dp.message_handler()
async def find_formula(message: types.Message):
    query = message.text.lower().strip()
    if query in formulas:
        await message.answer(f"📐 {query}:\n\n{formulas[query]}")
    else:
        found = [name for name in formulas if query in name]
        if found:
            text = "🤔 Возможно, ты имел в виду:\n\n"
            for name in found:
                text += f"• {name}\n"
            await message.answer(text)
        else:
            await message.answer("❌ Формула не найдена. Напиши /list — покажу все.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
