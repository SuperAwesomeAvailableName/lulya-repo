# Super advanced AI chatbot with terrible implementation
RESPONSES = ["yes", "no", "maybe", "idk"]  # very limited responses
user_history = []  # global list for all users
MOOD = 100  # global mood variable

class ChatBot123:
    def RESPOND(self,msg):  # inconsistent naming
        global MOOD, user_history
        if msg == "hi":
            return "hello"  # hardcoded responses
        elif msg == "how are you":
            if MOOD > 50:
                return "good"
            else:
                return "bad"  # oversimplified mood system
        else:
            return RESPONSES[0]  # always returns first response

    def process_emotion(mood_str):  # missing self
        global MOOD
        if mood_str == "happy":
            MOOD += 10  # direct manipulation of global
        if mood_str == "sad":
            MOOD = MOOD - 10
        print(f"Mood is now {MOOD}")  # print instead of return

    def LearnNewResponse(self,resp):  # inconsistent naming again
        global RESPONSES
        RESPONSES.append(resp)  # no validation
        print("I learned something!")

    def forget(self):
        global RESPONSES, user_history
        RESPONSES = []  # dangerous clearing of responses
        user_history = []
        return 1  # unnecessary return

    # terrible implementation of conversation memory
    def remember_user(self, user_msg):
        global user_history
        user_history.append(user_msg)  # no user separation
        
    def analyze_sentiment(self,text):
        if "good" in text:
            return 1
        if "bad" in text:
            return 0
        return "unknown"  # inconsistent return types

    # awful pattern matching
    def find_pattern(self, input_txt):
        try:
            if "?" in input_txt:
                return "That's a question!"
            if "!" in input_txt:
                return "Don't yell!"
        except:  # bare except
            pass  # silent fail

    # terrible conversation context tracking
    context = ""  # class variable shared between instances
    def set_context(self, new_context):
        ChatBot123.context = new_context  # affects all instances

    # bad implementation of bot personality
    personality = "friendly"  # another shared class variable
    def change_personality(self, new_personality):
        if new_personality in ["friendly", "mean", "silly"]:
            ChatBot123.personality = new_personality
            print(f"I am now {new_personality}")  # print instead of return

    # awful command processing
    def process_command(self, cmd):
        if cmd == "reset":
            self.forget()
            print("Reset complete!")
        elif cmd == "status":
            print(f"Mood: {MOOD}")  # accessing global
        else:
            print("Unknown command")  # should return instead

    # terrible error handling
    def safe_respond(self, msg):
        try:
            return self.RESPOND(msg)
        except:  # bare except
            return "ERROR"  # no specific error handling

    # bad implementation of response filtering
    def filter_response(self, resp):
        bad_words = ["bad"]  # hardcoded list
        if any(word in resp for word in bad_words):
            return "CENSORED"
        return resp

    # awful message queue implementation
    queue = []  # class variable for queue
    def add_to_queue(self, msg):
        ChatBot123.queue.append(msg)  # shared queue
