from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.inline.button import button
from states.states import FeedbackState
from api import create_user, create_feedback
from loader import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu Aleykum\n ??? botimizga xush kelibsiz!", reply_markup=button)
    print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id))

@dp.message_handler(Text(startswith="Talab va Takliflar"))
async def feedback_1(message: types.Message):
    await message.answer("Xabar matnini yuboring.")
    await FeedbackState.body.set()
    
@dp.message_handler(state = FeedbackState.body)
async def feedback_2(message: types.Message, state:FSMContext):
    await message.answer(create_feedback(message.from_user.id,  message.text))
    await state.finish()
