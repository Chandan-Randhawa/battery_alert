import psutil #import psutil module by using this command pip install psutil run this command in terminal or cmd
import pyttsx3 #import pyttsx3 module by using this command pip install pyttsx3 run this command in terminal or cmd
from plyer import notification
import time


while True:
    Battery = psutil.sensors_battery()
    Percentage_of_battry = Battery.percent
    Pluged = Battery.power_plugged
    if Percentage_of_battry > 95 and Pluged == True:
        notification.notify(
            title = 'Sufficient Charged !!',
            message = f'Hii Chandan , Your Battery is {Battery.percent}% charged, kindly unplug the charger',
            app_icon = r'C:\Users\Randhawa\Desktop\DR JJ\unofficial_gpt\icon.ico',
            timeout = 10
        )
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice' , voices[1].id)
        engine.setProperty('rate',185)
        pyttsx3.speak(f"Hii Chandan , Your Battery is {Battery.percent} percent  charged, kindly unplug the charger")

    elif Percentage_of_battry < 20 and Pluged == False:
        notification.notify(
            title = 'Battery Drained !!',
            message = f'Hii Chandan , Your Battery is {Battery.percent}% charged, Kindly plug the charger',
            app_icon = r'C:\Users\Randhawa\Desktop\DR JJ\unofficial_gpt\icon.ico',
            timeout = 10
        )
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice' , voices[0].id)
        engine.setProperty('rate',185)
        engine.say(f" Hii Chandan , Your Battery is {Battery.percent} percent charged, kindly plug the charger")
        engine.runAndWait()
    
    print(Percentage_of_battry)
    time.sleep(20)