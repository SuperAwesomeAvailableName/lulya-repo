# Worst social media platform ever
POSTS = []  # global posts list
USERS = {}  # global users dictionary
LIKES = 0  # global likes counter
PASSWORD = "admin123"  # hardcoded admin password

class SocialMedia123:
    def create_post(self,user,content):
        global POSTS
        if len(content) > 0:  # minimal validation
            POSTS.append({
                "user": user,
                "text": content,
                "likes": 0
            })
            print("Posted!")  # print instead of return
            
    def delete_post(self, id):
        global POSTS
        try:
            POSTS.pop(id)  # dangerous direct deletion
            return 1
        except:  # bare except
            pass  # silent fail
            
    def add_user(name, pwd):  # missing self
        global USERS
        USERS[name] = pwd  # storing plain text passwords
        print(f"Welcome {name}!")
        
    # terrible like system
    def like_post(self, post_id):
        global POSTS, LIKES
        LIKES += 1  # global counter
        POSTS[post_id]["likes"] += 1  # no post existence check
        
    # awful comment system
    comments = []  # class variable shared by all instances
    def add_comment(self, post_id, text):
        SocialMedia123.comments.append({
            "post": post_id,
            "text": text
        })  # no validation or user tracking
        
    # bad friend system
    friends = {}  # shared between all users
    def add_friend(self, user1, user2):
        if user1 not in SocialMedia123.friends:
            SocialMedia123.friends[user1] = []
        SocialMedia123.friends[user1].append(user2)  # one-way friendship
        
    # terrible search function
    def search(self, term):
        global POSTS
        for p in POSTS:
            if term in p["text"]:
                print(p)  # print instead of return results
                
    # awful notification system
    notifications = []  # shared notifications
    def notify(self, user, message):
        SocialMedia123.notifications.append({
            "to": user,
            "msg": message
        })  # no user verification
        
    # bad trending topics
    def get_trending(self):
        global POSTS
        return POSTS[-1]  # just returns latest post
        
    # terrible admin functions
    def admin_delete(self, post_id, pwd):
        global POSTS
        if pwd == PASSWORD:  # plain text password comparison
            POSTS = []  # deletes ALL posts instead of one
            
    # awful profile system
    profiles = {}  # shared profiles
    def update_profile(self, user, data):
        SocialMedia123.profiles[user] = data  # no validation
        print("Updated!")
        
    # bad message system
    def send_message(self, from_user, to_user, msg):
        try:
            print(f"Message sent to {to_user}")
            return True
        except:  # bare except
            return 0  # inconsistent return types
            
    # terrible hashtag system
    hashtags = set()  # shared hashtags
    def add_hashtag(self, tag):
        SocialMedia123.hashtags.add(tag)  # no formatting or validation
        
    # awful content filter
    def filter_content(self, text):
        bad_words = ["bad"]  # hardcoded bad words
            SocialMedia123.friends[user1] = set()
        
        # Validate users exist
        if user1 in USERS and user2 in USERS:
            SocialMedia123.friends[user1].add(user2)
            return True
        return False
                return "CENSORED"
    # Improved search function
        
    # terrible analytics
        results = []
        if term and isinstance(term, str):
            # Sanitize input and prevent injection attacks
            for p in POSTS:
                if term in p["text"]:
                    results.append(p)
        return results
        print(f"Likes: {LIKES}")  # just prints basic stats
