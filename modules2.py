import camelcase
import pyttsx3
import emoji
def camelcasecon():
    str = input("Enter yourdata: ")
    x = camelcase.CamelCase()
    if str == x.hump(str):
        print(emoji.emojize(':thumbs_up:'))
    else:
        x = camelcase.CamelCase()
        y = x.hump(str)
        spk=pyttsx3.init()
        spk.say(" Successfully converted your data into camel case")
        spk.runAndWait()
        print("The coverted data is: ",y)