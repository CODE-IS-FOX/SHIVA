import nltk
nltk.download('punkt')

from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"(hi|hello|hey|hy|oii)",
        ["it seems like you miss me huh?", "Hows your day my love?"]
    ],
    [
        r"what is your name ?",
        ["I am SHIVA. do you need to remeber?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but thanks for asking! How about you?"]
    ],
    [
        r"sorry (.*) (its my mistake|my foult|for problem)",
        ["It's okay! How can I help you?"]
    ],
    [
        r"I (.*) (good|well|okay|great)",
        ["Good to hear that!", "Awesome! Anything you'd like to talk about?"]
    ],
    [
        r"by|tata|see you|bye|",
        ["Goodbye! Have a great day."]
    ],
    [
        r"(.*)",  # This matches anything
        ["baby, i don't understand. please, let me explain in anothor way!!"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_start():
    print("Hi! I am your SHIVA. say 'by' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'by':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot_start()
