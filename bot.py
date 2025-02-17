from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import logging

API_TOKEN = "7934788290:AAFCnzA657xF6YcZKzB3Z5V42efXygtY8gE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



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
