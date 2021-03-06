import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def getscore(sent_file):
    # Dictionary to store the scores
    tweet_score = {}
    # Getting scores from the sentiment file and storing it in a dictionary
    for line in sent_file:
        term, score = line.split("\t")
        tweet_score[term] = int(score)
    return tweet_score


def calculateSentiment(tweet_score, tweet_file):
    # Opening the Output file
    output_file = tweet_file

    # Parsing every line in output file into json.loads
    for line in output_file:

        try:
            output_data = json.loads(line)
        except:
            continue
        # Sum of tweet is initialized to 0
        tweet_sum = 0

        # Pulling only 'text' of the tweet from the output
        if "text" in output_data:
            tweettext = output_data["text"]  # Storing the text of the tweet line
            tweettext_encode = tweettext.encode('utf-8', 'ignore')  # Encoding it to a utf-8 format or ignoring it
            split_tweet = tweettext_encode.split(" ")  # Splitting the tweet by words

            # Running a loop in the words
            # If word is the dictionary, it picks up the score for that word or else takes 0
            for word in split_tweet:
                if word in tweet_score:
                    tweet_sum = tweet_sum + tweet_score.get(word.lower(), 0)
            print tweet_sum

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Storing the dictionary returned from getscore function
    tweet_score = getscore(sent_file)

    #Calculating sentiment
    calculateSentiment(tweet_score, tweet_file)

if __name__ == '__main__':
    main()
