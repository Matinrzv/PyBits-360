from gtts import gTTS
import os

def Create_AudioBook(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
        
    tts = gTTS(text=text, lang='en')
    
    tts.save(output_file)
    print(f"AudioBook saved as {output_file}")
    
text_file = "Text.txt"
output_file = "AudioBook.mp3"

Create_AudioBook(text_file, output_file)
os.system(f"start {output_file}")

# import pyttsx3

# def Create_AudioBook(text, filename="AudioBook2.mp3"):
#     engine = pyttsx3.init()
    
#     engine.setProperty("rate", 150)
    
#     engine.setProperty("volume", 1.0)
    
#     engine.save_to_file(text, filename)
    
#     engine.runAndWait()
#     print(f"AudioBook saved as {filename}")
    
# if __name__ == "__main__":
#     text = """ Welcome to PyBits!
# This channel is all about learning Python through real projects.  
# From beginner-friendly exercises to creative coding challenges,  
# you’ll find tutorials that are simple, clear, and fun to follow.
# Our goal is to help you improve step by step — building practical skills  
# while creating exciting projects along the way.  
# Subscribe and join the journey!"""
#     Create_AudioBook(text, "AudioBook2.mp3")