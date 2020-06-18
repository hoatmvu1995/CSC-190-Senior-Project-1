from django.shortcuts import render
import requests
import praw
import pandas as pd
import datetime as dt
import sys
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'web_crawler/index.html')

@csrf_exempt
def output(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST['search_word'])
        search_word = request.POST['search_word']
        py_obj = craw_reddit(search_word)
        return render(request, 'web_crawler/output.html', {'output': py_obj})


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
    hot_topics = subreddit.search(keywords, limit=17)
    #go through all of the hot topics
    result = '<p>'
    for submission in hot_topics:
        result += '<b>' + submission.title + '</b></p>'
        result += '<p>' + submission.url + '</p>'
        result += '<p>' + submission.selftext + '</p>'
    return result

def default_page(request):
    return render(request, 'web_crawler/default_page1.html')

def admin_page(request):
    return render(request, 'web_crawler/administrator_page1.html')

def regular_page(request):
    return render(request, 'web_crawler/regular_page1.html')

def pass_forgot(request):
    return render(request, 'web_crawler/forgot_password.html')

def pass_change(request):
    return render(request, 'web_crawler/password_change.html')

def pass_change_success(request):
    return render(request, 'web_crawler/password_change_success.html')

def pass_found(request):
    return render(request, 'web_crawler/password_found.html')