import telegram.ext
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton

updater = telegram.ext.Updater('6687745137:AAHqyYwVhilo4CTfzPzIPpaV1AmNQ5Gyy0E')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.message.reply_text('Hello Python Friends, Lets Build Our Own Telegram Bot!')

def help(bot, update):
    bot.message.reply_text(
    """
    /start ---> this starts the bot
    /help ---> displays the menu
    /content ---> about the learnings
    /linux ---> first tutorial
    /contact ---> contact information
    /favorite ---> courses to take
    /services ---> display services
    """
    )

def content(bot, update):
    bot.message.reply_text('We have various methods to learn python & linux.')

def contact(bot, update):
    bot.message.reply_text('You can contact me at : stefanversan@gmail.com')

def linux(bot, update):
    bot.message.reply_text('Tutorial Link: https://fb.watch/o8U6IWTJ5j')

def service_keyboard(bot, update):
    keyboard = [
        ['Python'], ['Linux']
    ]
    bot.message.reply_text('Do you want to learn?'
                            , reply_markup = ReplyKeyboardMarkup(keyboard)
                            )

def favorite_keyboard(bot, update):
    keyboard = [
        [
            InlineKeyboardButton('linux','https://fb.watch/o8U6IWTJ5j'),
            InlineKeyboardButton('python','https://fb.watch/o8U6IWTJ5j'),
        ]
    ]
    bot.message.reply_text('Training from phoenix team', reply_markup = InlineKeyboardMarkup(keyboard))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(CommandHandler('linux',linux))
dispatcher.add_handler(CommandHandler('contact',contact))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('services', service_keyboard))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('favorite', favorite_keyboard))
updater.start_polling()
updater.idle()

