from Brain.Aibrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> F.R.I.D.A.Y is Preparing to start : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
from Main import MainTaskExecution
print(">> F.R.I.D.A.Y rolling in : Wait For Some More Seconds.")

def MainExecution():
    
    Speak("Hello Sir")
    Speak("I am Friday, your can tell me anything you want.")
    
    while True:
        
        D0data = MicExecution()
        D1 = str(D0data).replace(".","")
        D2 = str(D1).replace(". "," ")
        D3 = str(D2).replace(" .","  ")
        D4 = str(D3).replace(". .","..")
        
        Data = D4
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass
        
        elif len(Data)<3:
            pass
        
        elif "turn on the tv" in Data:        # Specfic Commands
            Speak("Ok turning on the android tv...")
        
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            
        else: 
            Reply = ReplyBrain(Data)
            Speak(Reply)
        
def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print("Clap Detected-->>")
        print("")
        MainExecution()
        
    else:
        pass
    
ClapDetect()