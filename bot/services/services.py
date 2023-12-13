import random

LEXICON_RU: dict[str, str] = {
    '/start': '<b>Привет!</b>\nДавай с тобой сыграем в игру '
              '"Камень, ножницы, бумага"?\n\nЕсли ты, вдруг, '
              'забыл правила, команда /help тебе поможет!\n\n<b>Играем?</b>',
    '/help': 'Это очень простая игра. Мы одновременно должны '
             'сделать выбор одного из трех предметов. Камень, '
             'ножницы или бумага.\n\nЕсли наш выбор '
             'совпадает - ничья, а в остальных случаях камень '
             'побеждает ножницы, ножницы побеждают бумагу, '
             'а бумага побеждает камень.\n\n<b>Играем?</b>',
    'rock': 'Камень 🗿',
    'paper': 'Бумага 📜',
    'scissors': 'Ножницы ✂',
    'yes_button': 'Давай!',
    'no_button': 'Не хочу!',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...',
    'yes': 'Отлично! Делай свой выбор!',
    'no': 'Жаль...\nЕсли захочешь сыграть, просто разверни '
          'клавиатуру и нажми кнопку "Давай!"',
    'bot_won': 'Я победил!\n\nСыграем еще?',
    'user_won': 'Ты победил! Поздравляю!\n\nДавай сыграем еще?',
    'nobody_won': 'Ничья!\n\nПродолжим?',
    'bot_choice': 'Мой выбор'
}


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя 
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'