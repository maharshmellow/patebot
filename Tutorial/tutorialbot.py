import praw
import time

r = praw.Reddit(user_agent = "Tutorial Bot www.github.com/maharshmellow/patebot")
r.login()       # will ask for the username / password when the program is run

wordsToFind = ["test"]         # words to find in the comments
cache = []                      # comments that have already been processed

def run_bot():
    print("Getting Subreddit")
    subreddit = r.get_subreddit("test")     # test subreddit - made for testing bots like this
    print("Getting Comments")
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
        commentText = comment.body.lower()
        isMatch = any(string in commentText for string in wordsToFind)
        if comment.id not in cache and isMatch:
            print("Match Found! Comment ID: " + comment.id)
            comment.reply("This comment contains the word test")
            print("Reply Successful")
            cache.append(comment.id)

            time.sleep(600)

    print("Sleeping...\n\n")

while True:
    run_bot()
    time.sleep(60)        # sleep the bot


"""PROBLEMS WITH CURRENT VERSION:
    - need to update ratelimit or program will shut down (praw.errors.RateLimitExceeded)"""
