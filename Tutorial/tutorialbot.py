import praw
import time

r = praw.Reddit(user_agent = "Tutorial Bot www.github.com/maharshmellow/patebot")
r.login()       # will ask for the username / password when the program is run
# words that the bot should search for in the comments
wordsToFind = ["test"]         
# comments that have already been processed
cache = []                      

def run_bot():
    print("Getting Subreddit")
    # use the /r/test subreddit since it is made for testing bots like this
    subreddit = r.get_subreddit("test")     
    print("Getting Comments")
    # only looks at 25 comments (there is a limit of 100)
    comments = subreddit.get_comments(limit=25)
    for comment in comments:
	# gets the comment text 
        commentText = comment.body.lower()
	# checks if there are any words in the comment that are also in the wordsToFind list
        isMatch = any(string in commentText for string in wordsToFind)
	# only processes the comment if there is a match and it hasn't been processed before
        if comment.id not in cache and isMatch:
            print("Match Found! Comment ID: " + comment.id)
	    # replies to the comment that contains the match
            comment.reply("This comment contains the word test")
            print("Reply Successful")
	    # saves the comment id so that it doesn't get processed again
            cache.append(comment.id)
	    # need to sleep the bot since there is a limit to how many comments can be made
            time.sleep(600)

    print("Sleeping...\n\n")

while True:
    run_bot()
    time.sleep(60)        # sleep the bot


"""PROBLEMS WITH CURRENT VERSION:
    - need to update ratelimit or program will shut down (praw.errors.RateLimitExceeded)"""
