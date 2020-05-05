import pyowm
import telebot
import pandas as pd


tables = pd.read_html("https://coronavirus-monitor.info/country/belarus/")


owm = pyowm.OWM ('e81b7a02bb98aaf6bf6a0e76c3d68884', language = "ru")
bot = telebot.TeleBot("981381779:AAHq36XXIUnY7whRtWqyicllwerMElBWaTA")




@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)



@bot.message_handler(content_types=['text','photo'])
def dog(message):
   if message.text == "/hello":
      bot.send_message(message.from_user.id, "Привет, ты хочешь пообщаться со мной?")    
      return
   elif message.text == 'Да':
      bot.send_message(message.from_user.id, 'Тогда нажимай сюда: @xaytfun_bot!\nСдесь ты сможешь пообщаться со мной!\nЖду тебя!')     
      return
   elif message.text == 'Допустим':
      bot.send_message(message.from_user.id, 'Тогда нажимай сюда: @xaytfun_bot!\nСдесь ты сможешь пообщаться со мной!\nЖду тебя!')     
      return
   elif message.text == 'Карта':
      bot.send_message(message.from_user.id,'Онлайн карта распространения коронавируса в мире:https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')
   elif message.text == 'Возможно':
      bot.send_message(message.from_user.id, 'Тогда нажимай сюда: @xaytfun_bot!\nСдесь ты сможешь пообщаться со мной!\nЖду тебя!')     
      return
   elif message.text == 'Нет':
      bot.send_message(message.from_user.id, 'tables')
     
      return




   if message.text == "Коронаминус":
      bot.send_message(message.from_user.id, 'Тебе не нужно носить с собой\n  электрошокер, потому что \n            своей красотой   \n    ты шокируешь любого!  ')
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAILXl5vuoCPsvxWqO7ob-g5iifR9EOEAAJYAQACFkJrCvnyXxerSs6ZGAQ')    
      return
   if message.text == "Ты кто?":
      bot.send_message(message.from_user.id, 'Я бот который даёт информацию') 
      return
   if message.text == "Выйти":
      bot.send_message(message.from_user.id, 'Вы благополучно вышли')
      return      

   if message.text == "Коронавирус":
      bot.send_message(message.from_user.id, "Появилась онлайн-карта\nраспространения коронавируса\n\nСпециалисты разработали\nинтерактивный сервис с постоянно\nобновляющейся статистикой\nраспространения коронавируса.\n\nПосмотреть можете тут по ссылке:\nhttps://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6\n\n\nВ Беларуси:\nУмерших: 89\nВылеченно: 2 386\nЗаражений: 14 027")
      return
   
   if message.text == "/start":
      bot.send_message(message.from_user.id, "Привет! Меня зовут Прогнозчик!\n Вот что я умею:\n1)\weather\n2)\help\n3)\hello\n4)Коронавирус.\n\nЕсли вы введёте эту комманду,\nто я расскажу вам какая погода сейчас!\n\nМой создатель Андрющенко Денис Николаевич\nВк:https://vk.com/denis759sd\nИнстаграмм:https://www.instagram.com/denis759sd/")
      print(message.text)
      print(message.from_user)
      return

   if message.text == "/help":
      bot.send_message(message.from_user.id, "Обратись к нему если у тебя есть вопроссы!\nИмя: Denis\nИмя пользователя: @den759sd ")
      return
   elif message.text == "Вызов":
      bot.send_message(message.from_user.id, 'Обратитесь в тех поддержку')
      return

   if message.text == "/weather":
      bot.send_message(message.from_user.id, "Введи город!")
      print(message.text)
      print(message.from_user)
      return
   elif message.text == message.text:
         print(message.text)
         print(message.from_user)
         observation = owm.weather_at_place( message.text )
         w = observation.get_weather()  
         temp = w.get_temperature('celsius')["temp"]

         answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
         answer += "Температура сейчас в районе " + str (temp) +"\n\n"

         if temp <= 5:
            answer += "Сейчас очень хххолоддно, одевайся очень тепло!!!"
         elif temp <= 8:
            answer += 'Оденься тепло!!!'
         elif temp <= 10:
            answer += "Сейчас холодно, одевайся теплее"
         elif temp <= 15:
            answer += "Сейчас не так холодно, так что можешь одеться полегче)"
         elif temp <= 20:
            answer += "Сейчас на улице тёпленько)"
         else:
            answer += "Температура норм, одевай что угодно))" 

         bot.send_message(message.chat.id, answer)
         return
   else:
      bot.send_message(message.from_user.id, message.text)
      bot.send_message(message.from_user.id, 'Такой комманды нет!\nВведи "/help".')
      return


   print(message.text)
   print(message.from_user)
   print()
   
bot.polling(none_stop = True)