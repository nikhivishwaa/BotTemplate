from pyrogram import Client,filters

bot = Client("M1_Filter_bot",
    api_id=19977122,
    api_hash = "168c8159234070c260a85df74feae727",
    bot_token="5907033633:AAFz5zdIJPiA85YUb_XBxDbyk7vT_DHBaKM"
    )


@bot.on_message(filters.command('start') & filters.private)     # creating a command
def start_command_reply(bot,message):                           # creating a f()
    bot.send_message(message.chat.id,"i am groot so send  me link")  # cslling a method

@bot.on_message(filters.command('start'))
def start_command_reply(bot,message):
    bot.send_message(message.chat.id,"i am groot")

@bot.on_message(filters.command('help'))
def help_command_reply(bot,message):
    message.reply_text("i am groot and glad to help you out")   # to reply a user

# welcome to new joined user
GROUP = "CuroSupport"
@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def help_command_reply(client,message):
    message.reply_text(f"welcome {message.from_user.first_name}")   # to reply a user with first name

# send photo to user
GROUP = "CuroSupport"
@bot.on_message(filters.command("photo"))
def photo_command_reply(bot,message):
    bot.send_photo(message.chat.id,"https://graph.org/file/8a50785f0b1ba0c2e8ccb.jpg")

# sending logs
@bot.on_message()
def send_logs(bot,message):                          
    LOG_CHANNEL = "-1001775116819"
    bot.send_message(LOG_CHANNEL,message.text) 

print("Working")
bot.run()