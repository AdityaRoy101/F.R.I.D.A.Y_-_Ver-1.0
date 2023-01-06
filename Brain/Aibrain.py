  # Api Key
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

  # Importing
import openai
from dotenv import load_dotenv

  # Coding
openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
  Filelog = open("DataBase\\chat_log.txt","r")
  chat_log_template = Filelog.read()
  Filelog.close()
  
  if chat_log is None:
    chat_log = chat_log_template
    
  prompt = f'{chat_log}You : {question}\nF.R.I.D.A.Y : '
  response = completion.create(
    model = "text-davinci-002",
    prompt = prompt,
    temperature = 0.5,
    max_tokens = 60,
    top_p = 0.3,
    frequency_penalty = 0.5,
    presence_penalty = 0)
  answer = response.choices[0].text.strip()
  chat_log_template_update = chat_log_template + f"\nYou : {question} \nF.R.I.D.A.Y : {answer}"
  Filelog = open("DataBase\\chat_log.txt","w")
  Filelog.write(chat_log_template_update)
  Filelog.close()
  return answer

