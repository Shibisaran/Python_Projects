import pyttsx3
import datetime
import pandas as pd

#declaration part
a=[]
#b=["time","date","year","month"]

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good morning")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon!")   
    else:
        speak("Good evening!")
wishMe()
speak(", I am your AI assistant.")

def time():
    Time=str(datetime.datetime.now())
    speak(Time)
    
    
a=input().split()    
matched_data=[]

#database
#def database():
 #   excel_file="D:\shibi\python\jarvis project\data1.xlsx"
  #  df=pd.read_excel(excel_file)
   # for lang in a:
    #    matched_row=df[df['Language']==lang]
     #   if not matched_row.empty:
      #      matched_data.extend(matched_row.values.tolist())
    #return matched_data
excel_file = "D:\shibi\python\jarvis project\data1.xlsx"
df = pd.read_excel(excel_file)

# Matched data list
matched_data = []

# Compare collected data with Excel data
for name in a:
    matched_rows = df[(df['Language'] == name)]
    
    if not matched_rows.empty:
        matched_data.extend(matched_rows.values.tolist())

# Print matched data
print("Matched data:")
for data in matched_data:
    print(data)         
    time()