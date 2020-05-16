from telegram.ext import Updater, CommandHandler

def main():
    # instantiate a new Updater, passing in the token in constructor
    updater = Updater(token = '1189835632:AAFZHwz60i6WuFMlCbaZIeqInDUqk5zpk20', use_context = True)

    # add a new command handler
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('repeat', repeat))
    updater.dispatcher.add_handler(CommandHandler('sum', sum))

    # ask telegram for new notifications
    updater.start_polling() 
    
    # capture stop-lights
    updater.idle()  

def start(update, context):
    update.message.reply_text('Hola, soy un bot hecho con Python!')
    
def repeat(update, context):
    update.message.reply_text(update.message.text)

def sum(update, context):
    result = int(context.args[0]) + int(context.args[1])
    result = str(result)
    update.message.replay_text("El resultado es " + result)

main()
