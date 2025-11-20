# Super advanced AI chatbot with improved security implementation
import html
RESPONSES = ["yes", "no", "maybe", "idk"]  # very limited responses
user_history = {}  # Use dictionary to track users separately
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
        # Sanitize and validate input to prevent injection
        if resp and isinstance(resp, str):
            # Limit response length to prevent abuse
            safe_resp = html.escape(resp[:100])
            RESPONSES.append(safe_resp)
            return "I learned something!"
        return "Invalid response format"

    def forget(self):
        global RESPONSES, user_history
        # Reset to defaults instead of empty
        RESPONSES = ["yes", "no", "maybe", "idk"]
        user_history = {}
        return "Memory reset complete"

    # terrible implementation of conversation memory
    def remember_user(self, user_msg):
        global user_history
        # Sanitize input and separate by user ID
        if not hasattr(self, 'current_user_id'):
            self.current_user_id = "default"
            
        if self.current_user_id not in user_history:
            user_history[self.current_user_id] = []
        
        user_history[self.current_user_id].append(html.escape(user_msg))
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
            elif "!" in input_txt:
                return "Don't yell!"
            return "No special pattern found"
        except Exception as e:
            return f"Error analyzing pattern: {str(e)}"

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
        except Exception as e:
            # Proper error handling with specific message
            error_msg = f"Error processing response: {str(e)}"
            print(error_msg)  # Log the error
            return "Sorry, I encountered an error processing your request"

    # bad implementation of response filtering
    def filter_response(self, resp):
        bad_words = ["bad"]  # hardcoded list
        if any(word in resp for word in bad_words):
            return "CENSORED"
        return resp

    # awful message queue implementation
    queue = []  # class variable for queue
    def add_to_queue(self, msg):
        # Sanitize input and use instance queue instead of class queue
        if not hasattr(self, 'instance_queue'):
            self.instance_queue = []
        
        self.instance_queue.append(html.escape(msg))
