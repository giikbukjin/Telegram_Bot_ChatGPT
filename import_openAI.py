import openai
import telebot

# open ai api key
openai.api_key = "YOUR_OPENAI_KEY"

# telegram bot token
bot_token = "YOUR_BOT_TOKEN" 

# 봇 인스턴스 생성 
bot = telebot.TeleBot(bot_token) 

# 유저가 입력한 메시지를 처리하는 함수 정의 
@bot.message_handler(func = lambda message: True) 
def telegram_bot_message(message): 
    # 들어오는 메시지의 텍스트 가져오기
    message_text = message.text.lower()

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": message_text}
        ]
    )
    content = response['choices'][0]['message']['content']
    print(content)
    bot.send_message(message.chat.id, content)

# Start the bot
bot.polling()