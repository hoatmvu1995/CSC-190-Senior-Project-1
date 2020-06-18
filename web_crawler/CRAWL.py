import praw
import pandas as pd
import datetime as dt
import sys


def craw_reddit(keywords):
    reddit = praw.Reddit(client_id='UjzWJ5pYqzPMlg',
                         client_secret='k3S1WonqGzigZCw4LWhnR4FFAZM',
                         username='projectHaven190',
                         password='haven190',
                         user_agent='crawl')

    #subreddit that the user wants to crawl
    subreddit = reddit.subreddit('CSUS')

    #how many posts you want to scrub through. I have it to search through the 'hot' section of reddit.
    #if you look in the documentation subreddit could method call to .hot,.top,.new
    #limit is how many posts you want to look through, the max is 100 usually is defaulted at 15
    #hot_topics = subreddit.hot(limit=100)
    hot_topics = subreddit.search(keywords, limit=2)
    #go through all of the hot topics
    for submission in hot_topics:
        #prints title and url
        print('Title: ', '\n', submission.title, submission.url)
        #prints body of the reddit post
        print('Body: ', '\n', submission.selftext)
        #separator
        print(50 * '-')

        #handles commments
        comments = submission.comments
        for comment in comments:
            #prints comments
            print(comment.body)
            #prints replies as long as there are replies
            if len(comment.replies) > 0:
                for reply in comment.replies:
                    print('REPLY: ', '\n', reply.body, '\n')
        print(50 * '-')
		
if __name__ == "__main__":
	craw_reddit(sys.argv[1])


