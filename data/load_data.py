import tweepy
from secrets import *

#Tho in real life you shouldn't commit API_KEYS into version control =_=
API_KEY="DatOlICux7Cfv7Gz2aNNr1Z5D"
API_SECRET_KEY ="zWQeqWPqU4LjMcAUTf8o1G8KqMLvYN1osCuPix1OMNlE3s8C1A"
ACCESS_TOKEN = "1318369060325892096-5eGOaFKBfhcDV2LrRlQUPpD44zxGJO"
ACCESS_TOKEN_SECRET = "DGs6Z4yIguUHoUqY3T4KnE4qnURF3V9DhTBIelTDYFnsV"
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def download_all_tweets(user, file):
    list_of_pages = []
    on_page=0
    for page in tweepy.Cursor(api.user_timeline, screen_name=user,count=100, tweet_mode='extended').pages():
        # print(user + str(on_page))
        on_page += 1
        list_of_pages.append(page)
    with open(file, "a") as f:
        for page in list_of_pages:
            for tweet in page:
                    tweet_text = tweet.full_text
                    f.write(tweet_text.replace("\n", "NEWLINE") + "\n")


# donald_trump_download()
# download_all_tweets('@realDonaldTrump', "trump_data")
news_orgs = ["@cbcnews", "@cnn", "@nytimes", "@theeconomist", "@bbcworld", "@ap", "@reuters"]

for org in news_orgs:
    download_all_tweets(org, "newsorgs_data")

    