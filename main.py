from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import logging

API_TOKEN = "7554748845:AAHNm4_mkEnvY3xAmmxTNp9goWOdRjJQBmI"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# 1
@dp.message_handler(Text(equals="Salom", ignore_case=True))
async def salom_handler(message: types.Message):
    await message.reply("Va alaykum assalom!")

# 2
@dp.message_handler(Text(contains="rahmat", ignore_case=True))
async def rahmat_handler(message: types.Message):   
    await message.reply("Sizga ham rahmat!")

# 3
@dp.message_handler(Text(startswith="Buyruq", ignore_case=True))
async def buyruq_handler(message: types.Message):
    await message.reply("Buyruq qabul qilindi.")

# 4
@dp.message_handler(Text(endswith="xayr", ignore_case=True))
async def xayr_handler(message: types.Message):
    await message.reply("Xayr, keyinroq ko'rishamiz!")

# 5
@dp.message_handler(Text(equals="test", ignore_case=True))
async def test_handler(message: types.Message):
    await message.reply("Siz test buyruq yubordingiz!")

# 6
@dp.message_handler(lambda message: message.text.isdigit())
async def only_numbers(message: types.Message):
    await message.reply("Siz faqat raqam jo'natdingiz!")

# 7
@dp.message_handler(Text(equals=["ha", "yo'q", "balki"], ignore_case=True))
async def javob_handler(message: types.Message):
    await message.reply("Sizning javobingiz qabul qilindi.")

# 8
@dp.message_handler(Text(startswith="bot") & Text(endswith="ishla"))
async def bot_start_handler(message: types.Message):
    await message.reply("Bot ishga tushdi!")


# 9
@dp.message_handler(~Text(contains="maxfiy"))
async def not_secret_handler(message: types.Message):
    await message.reply("Maxfiy so'z ishlatilmagan xabar qabul qilindi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# equals – Aniq matnni qidiradi (katta-kichik harflarni farqlamaydi).
# contains – Xabar ichidagi so'zni qidiradi (katta-kichik harflarni farqlamaydi).
# startswith – Xabarning boshlanishini tekshiradi.
# endswith – Xabarning tugashini tekshiradi.
# ignore_case – Katta va kichik harflarni farqlamaydi.
# lambda message: message.text.isdigit() – Xabar faqat raqamlardan iborat bo'lsa ishlaydi.
# in_ – Berilgan ro'yxatdan biror so'z bo'lsa ishlaydi.
# & va | – Bir nechta shartlarni birlashtirish uchun ishlatiladi.
# ~ – Xabar matnida ko'rsatilgan so'z bo'lmaganida ishlaydi.
