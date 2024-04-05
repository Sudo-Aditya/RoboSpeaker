import pyttsx3

engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created By Aditya")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()