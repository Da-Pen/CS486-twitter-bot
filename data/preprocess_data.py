import numpy as np

# CONSTANTS
NEWS_ORGS_DATA_FILE_NAME = './newsorgs_data'
TRUMP_DATA_FILE_NAME = './donald_trump_data'
SKIP_URLS = True
SKIP_ELLIPSES = False

def ignore_urls(s):
    return ' '.join([x for x in s.split() if 'http' not in x])

# gets a list of strings representing the tweets in the given file.
# can limit the number of tweets to get using upto.
# replaces 'NEWLINE's with actual \n characters.
def get_file_contents_list(filename, upto=None):
    f = open(filename, 'r')
    lines = f.read().split('\n')[:upto]
    f.close()
    # replace NEWLINE's and ignore all lines that do not have spaces (because they are probably just a link)
    lines = np.array([line.replace('NEWLINE', '\n') for line in lines if line.strip().find(' ') != -1])
    if SKIP_ELLIPSES:  # skip tweets with the '…' character, which indicates that it has been truncated
        lines = np.array([line for line in lines if line.find('…') == -1])
    if SKIP_URLS:
        lines = np.array([ignore_urls(line) for line in lines])
    return lines


def main():
    pass    # do nothing for now
    # news_org_string_tweets = get_file_contents_list(NEWS_ORGS_DATA_FILE_NAME)  # for now just get the first 10 items
    # print(len(news_org_string_tweets))
    # for tweet in news_org_string_tweets:
    #     print(tweet)

if __name__ == '__main__':
    main()