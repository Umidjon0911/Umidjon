import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types , F 
from aiogram.types import Message , FSInputFile
from aiogram.filters import Command
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as BS
from aiogram import types
from config import BOT_TOKEN, Kanal_id, Admins
from aiogram.filters import Filter
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import and_f
logging.basicConfig(level=logging.INFO)
import time

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class CheksupChanel(Filter):
  async def __call__(self,message:Message,bot:Bot):
    user_ststus=await bot.get_chat_member(Kanal_id,message.from_user.id)
    if user_ststus.status in ['creator','administrator','member']:
      return False
    return True


@dp.message(CheksupChanel())
async def obuna1(message:Message):
  Kanal_link = 't.me/majburiyobunabolasan'
  kanallar=InlineKeyboardMarkup(
   inline_keyboard=[
     [InlineKeyboardButton(text='OBUNA BOLING :)',url=Kanal_link)]
   ]
 )
  await message.answer_photo(photo='https://codecapsules.io/wp-content/uploads/2023/08/comparing-telegram-bot-hosting-providerspng.png',caption='Kanalga obuna boling',reply_markup=kanallar)


@dp.message(Command("start"))
async def rasmy(message: types.Message):
    
    kb = [
        
        [types.KeyboardButton(text="🌦 Ob - Havo")]
        
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        
    )
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)






t = requests.get('https://sinoptik.ua/погода-Ургенч')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
@dp.message(F.text.lower() == "urganch")
async def with_puree(message: types.Message):
    await bot.send_sticker(message.from_user.id , sticker="CAACAgEAAxkBAAELjeZl256qhmpsubqNBXQ10P2HDcE9rQAChQIAAvTrGURAMLYI2z7wbTQE")
    await message.reply(f"⛅️ Bugun Urganchda Ob Havo \n\n 🌝 Kunduzi  {t_max} \n 🌚Kechqurun {t_min} \n\n 💫 Boʻlishi kutilmoqda ")

t = requests.get('https://sinoptik.ua/погода-андижан')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min1 = el.select('.temperature .min')[0].text
    max1 = el.select('.temperature .max')[0].text
    t_min1 = min1[4:]
    t_max1 = max1[5:]
@dp.message(F.text.lower() == "andijon")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Andijonda Ob Havo \n\n 🌝 Kunduzi  {t_max1} \n 🌚Kechqurun {t_min1} \n\n 💫 Boʻlishi kutilmoqda ")


t = requests.get('https://sinoptik.ua/погода-бухара')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min2 = el.select('.temperature .min')[0].text
    max2 = el.select('.temperature .max')[0].text
    t_min2 = min2[4:]
    t_max2 = max2[5:]
@dp.message(F.text.lower() == "buxoro")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Buxoroda Ob Havo \n\n 🌝 Kunduzi  {t_max2} \n 🌚Kechqurun {t_min2} \n\n 💫 Boʻlishi kutilmoqda ")

t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min3 = el.select('.temperature .min')[0].text
    max3 = el.select('.temperature .max')[0].text
    t_min3 = min3[4:]
    t_max3 = max3[5:]
@dp.message(F.text.lower() == "toshkent")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Toshkentda Ob Havo \n\n 🌝 Kunduzi  {t_max3} \n 🌚Kechqurun {t_min3} \n\n 💫 Boʻlishi kutilmoqda ")


t = requests.get('https://sinoptik.ua/погода-нукус')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min4 = el.select('.temperature .min')[0].text
    max4 = el.select('.temperature .max')[0].text
    t_min4 = min4[4:]
    t_max4 = max4[5:]
@dp.message(F.text.lower() == "nukus")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Nukusda Ob Havo \n\n 🌝 Kunduzi  {t_max4} \n 🌚Kechqurun {t_min4} \n\n 💫 Boʻlishi kutilmoqda ")




t = requests.get('https://sinoptik.ua/погода-навои')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min5 = el.select('.temperature .min')[0].text
    max5 = el.select('.temperature .max')[0].text
    t_min5 = min5[4:]
    t_max5 = max5[5:]
@dp.message(F.text.lower() == "navoi")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Navoida Ob Havo \n\n 🌝 Kunduzi  {t_max5} \n 🌚Kechqurun {t_min5} \n\n 💫 Boʻlishi kutilmoqda ")


t = requests.get('https://sinoptik.ua/погода-фергана')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min6= el.select('.temperature .min')[0].text
    max6 = el.select('.temperature .max')[0].text
    t_min6 = min6[4:]
    t_max6 = max6[5:]
@dp.message(F.text.lower() == "farg'ona")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun farg'onada Ob Havo \n\n 🌝 Kunduzi  {t_max6} \n 🌚Kechqurun {t_min6} \n\n 💫 Boʻlishi kutilmoqda ")


t = requests.get('https://sinoptik.ua/погода-самарканд')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min7 = el.select('.temperature .min')[0].text
    max7 = el.select('.temperature .max')[0].text
    t_min7 = min7[4:]
    t_max7 = max7[5:]
@dp.message(F.text.lower() == "samarqand")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Samarqandda Ob Havo \n\n 🌝 Kunduzi  {t_max7} \n 🌚Kechqurun {t_min7} \n\n 💫 Boʻlishi kutilmoqda ")


t = requests.get('https://sinoptik.ua/погода-джизак')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min8 = el.select('.temperature .min')[0].text
    max8 = el.select('.temperature .max')[0].text
    t_min8 = min8[4:]
    t_max8 = max8[5:]
@dp.message(F.text.lower() == "jizzax")
async def with_puree(message: types.Message):
    await message.reply(f"⛅️ Bugun Jizzaxda Ob Havo \n\n 🌝 Kunduzi  {t_max8} \n 🌚Kechqurun {t_min8} \n\n 💫 Boʻlishi kutilmoqda ")







@dp.message(F.text.lower() == "🌦 ob - havo")
async def with_puree(message: types.Message):

    knopka = [
            [
                types.KeyboardButton(text="Urganch"),
                types.KeyboardButton(text="Toshkent"),
                types.KeyboardButton(text="Nukus"),
        ],
        [
                types.KeyboardButton(text="Buxoro"),
                types.KeyboardButton(text="Andijon"),
                types.KeyboardButton(text="Navoi"),
        ],
        [
                types.KeyboardButton(text="Samarqand"),
                types.KeyboardButton(text="Farg'ona"),
                types.KeyboardButton(text="Jizzax"),
        ]
        ]


    keyboard = types.ReplyKeyboardMarkup(
        keyboard=knopka,
        resize_keyboard=True,

    )
    await message.answer(f"<b>{message.from_user.full_name}</b> \n hududni tanlang",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
