from datetime import datetime

def responses(text):
    userMessage = str(text).lower()
    
    #template for bot responding messages
    if userMessage in ("word1", "word2", "wordn"): #if word1, word2... wordn is in the user message, then bot will response "Response"
       return "Response"

    #Example 
    if userMessage in ("hello", "hi","hola"):
        return "Hey!"

    #time 

    if userMessage in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    #creator
    if userMessage in ("github"):
        return "https://github.com/Chavis00 "


    #default response
     
    return "I don't understand you :c"