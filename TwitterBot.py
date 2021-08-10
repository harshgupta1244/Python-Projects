import tweepy

consumer_key = "kFCB8uwiUlK6psEb31xxXofrj"
consumer_secret = "nmlscYKwYK8x6bN77WiTt8pobM9RkmwzZAVOBUyVwNE588N0Lj"
access_token = "845867221230411776-5puAvkKtyCiGqHUQrIMe6EN3JXSl1uQ"
access_token_secret = "yr3niBUflhiQXFlAxP0GLw5njxXyaFC5QLkwItjoEjJZW"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error During Authentication")


# api.update_status("Hello Everyone")
"""
tweet = "Elephant"
photo = "C:\\Users\\user\\OneDrive\\Documents\\Coding BLocks\\Python\\Projects\\Elephant.jpg"
status = api.update_with_media(photo, tweet)
api.update_status(status=tweet)
"""
username = input("Enter the Username: ")
user = api.get_user(username)
print("User Details: ")
print(user.name)
print(user.description)
print(user.location)
print("Last 20 Followers: ")
for follower in user.followers():
    print(follower.name)
