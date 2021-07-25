import random, time, os
import requests


def plus(update,context):
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])

        result = num1 + num2

        update.message.reply_text(str(num1)+"+"+str(num2)+" = "+str(result))

    except (ValueError):
        update.message.reply_text("Utiliza dos numeros capo")



#Send a short version of an URL 
#Get API Key from https://rapidapi.com/BigLobster/api/url-shortener-service
def urlShortener(update,context): 
  url = "https://url-shortener-service.p.rapidapi.com/shorten"
  payload = "url="+ str (context.args)
  
  payload = payload.replace('[', '')
  payload = payload.replace(']', '')
  payload = payload.replace("'", '')
  headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "APIKEY", #API Key here
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com"
    }
  response = requests.request("POST", url, data=payload, headers=headers)
  a = response.text.replace('"','')
  a = a.replace('{', '')
  a = a.replace('}', '')
  a = a.replace("\\", "")
  a = a.replace("result_url:", "")  
  a = a.replace("url=", "")  

  
  update.message.reply_text(a)


#Current weather anywhere in the world
#Get API Key from https://home.openweathermap.org/api_keys

def getWeather(update,context):
	
    APIKEY = "YourAPIKEY"
    place = str(context.args)
    place = place.replace('[', '')
    place = place.replace(']', '')
    place = place.replace("'", '')
    place = place.replace(" ", '')
    place = place.replace(",", '+')

    api = str("http://api.openweathermap.org/data/2.5/weather?q="+str(place)+"&appid="+APIKEY)
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    
    final_info = condition + "\n" + str(temp) + "°C"

    update.message.reply_text(final_info)



#Send a random fox from https://randomfox.ca
def rfox(update,context):

  response = requests.get("https://randomfox.ca/floof/")

  fox = response.json()

  url = fox['image']

  r = requests.get(url)

  update.message.reply_photo(r.content)


#Rock Paper Scissor game
def rps(update, context):
  choices = ['rock', 'paper', 'scissors']

  player = str(context.args)
  player = player.replace('[', '')
  player = player.replace(']', '')
  player = player.replace("'", '')

  update.message.reply_text("You chose: " + player)
	
  cpu = random.choice(choices)

  update.message.reply_text("I chose: " +str(cpu))

  if player == cpu:
    
	  time.sleep(1)
	  os.system('clear')
	  update.message.reply_text("Tie!")
  elif ((player == 'paper' and cpu == 'scissors') or (player == 'rock' and cpu == 'paper') or (player == 'scissors' and cpu == 'rock')):
    
	  update.message.reply_text("You Lose! I always win..")
	  time.sleep(3)
	  os.system('clear')
  elif ((player == 'paper' and cpu == 'rock') or (player == 'rock' and cpu == 'scissors') or (player == 'scissors' and cpu == 'paper')):
    
	  update.message.reply_text("You Win :c")
	  time.sleep(3)
	  os.system('clear')
  else:
	  update.message.reply_text("You can only choose between: rock, paper or scissors")
