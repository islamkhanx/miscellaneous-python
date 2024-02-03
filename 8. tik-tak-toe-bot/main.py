#!/usr/bin/env python

"""
Bot for playing tic tac toe game with multiple CallbackQueryHandlers.
"""

from copy import deepcopy
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from game_module import Game


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# set higher logging level for httpx
# to avoid all GET and POST requests being logged
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# get token using BotFather
TOKEN = '6572763383:AAGzumaj3l7bmwQldwwV5-8I8da8K9cTb-w'

CONTINUE_GAME, FINISH_GAME = range(2)

FREE_SPACE = '.'
CROSS = 'X'
ZERO = 'O'


DEFAULT_STATE = [[FREE_SPACE for _ in range(3)] for _ in range(3)]


def get_default_state():
    """Helper function to get default state of the game"""
    return deepcopy(DEFAULT_STATE)


def generate_keyboard(
        state: list[list[str]]) -> list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyboard 3x3 (telegram buttons)"""
    return [
        [
            InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
            for r in range(3)
        ]
        for c in range(3)
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    context.user_data['keyboard_state'] = get_default_state()
    keyboard = generate_keyboard(context.user_data['keyboard_state'])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f'X (your) turn! Please, put {"X"} to the free place',
        reply_markup=reply_markup
        )

    return CONTINUE_GAME


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Main processing of the game"""

    game_ = Game(context.user_data['keyboard_state'])
    query = update.callback_query

    # player moves
    r, c = [int(x) for x in query.data]
    context.user_data['keyboard_state'] = game_.move(CROSS, pos=(r, c))
    if game_.won():
        return FINISH_GAME

    # robot moves
    context.user_data['keyboard_state'] = game_.move(ZERO, robo=True)
    if game_.won(ZERO) or (not game_.move_availiale()):
        return FINISH_GAME

    keyboard = generate_keyboard(game_.state)
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        f'X (your) turn! Please, put {"X"} to the free place',
        reply_markup=reply_markup
        )

    return CONTINUE_GAME


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    game_ = Game(context.user_data['keyboard_state'])
    keyboard = generate_keyboard(game_.state)

    cros_won, zero_won = game_.won(CROSS), game_.won(ZERO)
    if cros_won:
        text = 'X (you) won! Molodec'
    elif zero_won:
        text = 'X (you) lose! That is bad'
    else:
        text = 'Pobedila druzhba!'

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'{text} \n\nStart new game /start',
        reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # reset state to default so you can play again with /start
    context.user_data['keyboard_state'] = get_default_state()
    return ConversationHandler.END


def main() -> None:
    """Run the bot"""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Setup conversation handler with the states CONTINUE_GAME and FINISH_GAME
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CONTINUE_GAME: [
                CallbackQueryHandler(game, pattern='^' + f'{r}{c}' + '$')
                for r in range(3)
                for c in range(3)
            ],
            FINISH_GAME: [
                CallbackQueryHandler(end, pattern='^' + f'{r}{c}' + '$')
                for r in range(3)
                for c in range(3)
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to application
    # that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
