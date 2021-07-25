import Constants as keys
from telegram.ext  import * 
import Responses as R
import Commands as C
import logging


logger = logging.getLogger(__name__)


print("Im alive!") 


#Send a message when the command /start is issued.
def start(update, context):
    
    update.message.reply_text('Im alive!')


#Send a message when the command /help is issued.
def help(update, context):

    update.message.reply_text('/rfox: random foxes\n/short: urlshortener\n/weather: weather today\n/plus: suma 2 numeros\n/rps: rock, paper or scissors\n')
    
#Echo the user message.
def echo(update, context):
    
    update.message.reply_text(update.message.text)

#Log Errors caused by Updates.
def error(update, context):

    logger.warning('Update "%s" caused error "%s"', update, context.error)

#Send responses from Responses.py
def responses(update, context):

  text = str(update.message.text).lower()
  response = R.responses(text)
  
  update.message.reply_text(response)


#Start the bot.
def main():
    #Create the Updater and pass it your bot's token.
    #Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(keys.TOKEN, use_context=True)

    #Get the dispatcher to register handlers
    dp = updater.dispatcher

    #Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("plus", C.plus))
    dp.add_handler(CommandHandler("short", C.urlShortener))
    dp.add_handler(CommandHandler("weather", C.getWeather))
    dp.add_handler(CommandHandler("rfox", C.rfox))
    dp.add_handler(CommandHandler("rps", C.rps))

    #Messages
    dp.add_handler(MessageHandler(Filters.text, responses))

    #Log all errors
    dp.add_error_handler(error)

    #Start the Bot
    updater.start_polling()

    #Run the bot until you press Ctrl-C or the process receives SIGINT,
    #SIGTERM or SIGABRT. This should be used most of the time, since
    #start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

#corazon()
if __name__ == '__main__':
    main()