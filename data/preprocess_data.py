import numpy

# CONSTANTS
NEWS_ORGS_DATA_FILE_NAME = './newsorgs_data'
TRUMP_DATA_FILE_NAME = './donald_trump_data'


# gets a list of strings representing the tweets in the given file.
# can limit the number of tweets to get using upto.
# replaces 'NEWLINE's with actual \n characters.
def get_file_contents_list(filename, upto=None):
    f = open(filename, 'r')
    lines = f.read().split('\n')[:upto]
    f.close()
    # replace NEWLINE's and ignore all lines that do not have spaces (because they are probably just a link)
    return [line.replace('NEWLINE', '\n') for line in lines if line.strip().find(' ') != -1]


def main():
    news_org_string_tweets = get_file_contents_list(NEWS_ORGS_DATA_FILE_NAME, 10)  # for now just get the first 10 items
    for tweet in news_org_string_tweets:
        print(tweet)


if __name__ == '__main__':
    main()