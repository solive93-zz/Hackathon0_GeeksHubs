from telegram.ext import Updater

def main():
    updater = Updater(token = open('./bot_token').read(), use_context = True)
    
    # preguntar a telegram si hay nuevas notificaciones
    updater.start_polling() 
    
    # si alguien corta la ejecución del bot, esta función idle permite que acabe
    updater.idle()  

main()
