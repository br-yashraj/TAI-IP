import speech_recognition as sr 
from tkinter import *
from tkinter import messagebox
import pyttsx3


root = Tk()
root.title("Speech To Text")  
root.geometry("500x350")
root.resizable(0, 0)
root.config(bg="#B5C0D0")

# Initialize TTS engine
engine = pyttsx3.init() 

# Initialize Speech Recognizer
r = sr.Recognizer()

# Listen to mic and convert to text 
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_box.insert('1.0', text)
        except:
            messagebox.showerror("Speech Recognizer", "Could not understand audio")

# Text to speech conversion
def speak_text():
    text = text_box.get("1.0", "end") 
    engine.say(text)
    engine.runAndWait()
               
f1 = Frame(root, bg="#B5C0D0")
f1.pack(side="top", fill=X)   

f2 = Frame(root, bg="#B5C0D0")
f2.pack(side="bottom", fill=X, pady=5)

f3 = Frame(root, bg="#B5C0D0")
f3.pack(side="top", fill=X)

# Create text box   
result = Label(f3, text="You Said - ", bg="#B5C0D0", fg="black", font="Arial 10 bold")
result.pack(side="left", pady=5, padx=85)

text_box = Text(root, height=12, width=40, borderwidth=1.5, relief="solid")
text_box.pack()

# Buttons
listen_btn = Button(f1, text="Speak", bg="green", fg="white", command=listen)
listen_btn.pack(pady=15)
              
speak_btn = Button(f2, text="Hear", bg="yellow", fg="black", command=speak_text)
speak_btn.pack(pady=10)
 
root.mainloop()