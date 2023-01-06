import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()
    
    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
        
    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    # Another method to open the Required App
    # elif "start" in Query:
    #     Nameoftheapp = Query.replace("start ","")
    #     if "chrome" in Nameoftheapp:
    #         os.startfile(r"file_name")
    
# OpenExe('visit facebook')
