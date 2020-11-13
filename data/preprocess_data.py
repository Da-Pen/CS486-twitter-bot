import numpy as np
from collections import defaultdict

# CONSTANTS
NEWS_ORGS_DATA_FILE_NAME = './newsorgs_data'
TRUMP_DATA_FILE_NAME = './donald_trump_data'
SKIP_URLS = True
SKIP_ELLIPSES = False
SKIP_RETWEETS = True
SKIP_REPLIES = True  # it seems like Trump often has tweets where he simply replies to another Twitter user or quotes them. They usually start with '@' or '"@'. If this is set to true, then ignore those tweets.
VALID_CHARS = set([
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', ',', '-', '.', '/', '\n',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    ':', ';', '?', '@', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '_', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '—', '’', '“', '”'
])
MIN_VALID_CHAR_PERCENT = 0.9  # at least this ratio of the characters in the tweet have to be valid (i.e have to exist in the above grammar). Otherwise we ignore the tweet.


# returns a string minus all the urls in it
def ignore_urls(s):
    return ' '.join([x for x in s.split() if 'http' not in x])


# filters invalid characters. If the number of characters filtered is greater than (1 - MIN_VALID_CHAR_PERCENT), then return None.
def filter_invalid_chars(tweet):
    new_tweet = ''.join([char for char in tweet if char in VALID_CHARS])
    if len(new_tweet) / len(tweet) < MIN_VALID_CHAR_PERCENT:
        print('ignoring tweet (too few valid characters):', tweet)
        return None
    # elif len(new_tweet) < len(tweet):
    #     print('filtered tweet. Old:', tweet, 'New:', new_tweet)
    return new_tweet


# gets a list of strings representing the tweets in the given file.
# can limit the number of tweets to get using upto.
# replaces 'NEWLINE's with actual \n characters.
def get_tweets_list(filename, upto=None):
    f = open(filename, 'r')
    lines = f.read().split('\n')[:upto]
    f.close()
    # replace NEWLINE's and ignore all lines that do not have spaces (because they are probably just a link)
    lines = [line.replace('NEWLINE', '\n') for line in lines if line.strip().find(' ') != -1]
    if SKIP_ELLIPSES:  # skip tweets with the '…' character, which indicates that it has been truncated
        lines = [line for line in lines if line.find('…') == -1]
    if SKIP_URLS:
        lines = [ignore_urls(line) for line in lines]
    if SKIP_RETWEETS:
        lines = [line for line in lines if line[:2] != 'RT']
    if SKIP_REPLIES:
        lines = [line for line in lines if line[0] != '@' and line[:2] != '"@']
    # check what percentage of characters are valid: if less than MIN_VALID_CHAR_PERCENT are valid, then ignore this tweet. Otherwise, delete invalid characters.
    lines = [filter_invalid_chars(line) for line in lines if filter_invalid_chars(line) is not None]
    return np.array(lines)


# gets most commonly occuring characters in datasets
def get_commonly_occuring_characters():
    threshold = 500  # If characters appear more than threshold times in all tweets in all datasets, it is printed
    news_org_tweets = get_tweets_list(NEWS_ORGS_DATA_FILE_NAME)
    trump_tweets = get_tweets_list(TRUMP_DATA_FILE_NAME)
    # see which characters exist
    chars_to_occurrence_map = defaultdict(lambda: 0)
    for tweet in news_org_tweets:
        for char in tweet:
            chars_to_occurrence_map[char] += 1
    for tweet in trump_tweets:
        for char in tweet:
            chars_to_occurrence_map[char] += 1
    chars_set = set()
    for char in chars_to_occurrence_map.keys():
        if chars_to_occurrence_map[char] > threshold:
            chars_set.add((char, chars_to_occurrence_map[char]))  # if we want to print (char, occurence_times) tuples
            # chars_set.add(char)                                     # if we want to print just the characters  
    return sorted(list(chars_set))


def main():
    news_org_tweets = get_tweets_list(NEWS_ORGS_DATA_FILE_NAME)
    trump_tweets = get_tweets_list(TRUMP_DATA_FILE_NAME)
    print('\n'.join(trump_tweets))

if __name__ == '__main__':
    main()