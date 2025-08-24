import random
def chatbot():
    print("🤖 Hello! I'm mohanBot. Type 'bye' to exit.\n")
    r= [
        "Hmm, that's interesting!","Tell me more about that.","I'm not sure I understand, but I'm listening!","Can you rephrase that?",
        "Sounds cool! bro enter what you want just chill dont fall love enjoy yours self"]
    while True:
        a=input("You: ").lower().strip()
        if "hi" in a or "hello" in a:
            print("mohanBot: Hey there")
        elif "your name" in a:
            print("mohanBot: I'm mohanBot, your Python-powered mohan.")
        elif "how are you" in a:
            print("mohanBot: I'm doing great—thanks for asking!")
        elif "joke" in a:
            print("mohanBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛")
        elif "bye" in a or "exit" in a:
            print("mohanBot: Goodbye! Catch you later. ")
            break
        else:
            print("{} is mohanBot".format(random.choice(r)))
chatbot()



