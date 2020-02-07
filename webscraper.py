from bs4 import BeautifulSoup
import requests
import json

# where you want to scrape
url = "http://ethans_fake_twitter_site.surge.sh/"

response = requests.get(url, timeout=5)

content = BeautifulSoup(response.content, "html.parser")

# the array where we store our data
tweetArr = []

# finds all relevant data 
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    # formats the data in a more readable way
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArr.append(tweetObject)

# creats a new file with all data that we need
with open('twitterData.json', 'w') as outfile:
        json.dump(tweetArr, outfile)
