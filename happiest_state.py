import sys
import json
import types
import operator

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


def calculateHappyState(tweet_score, tweet_file):
    state_sent_dict = {}
    state_count = {}
    average_state_score = {}
    sorted_average_state_score = {}

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
        if "text" in output_data and "place" in output_data and output_data["lang"]=="en":
            tweettext = output_data["text"]  # Storing the text of the tweet line
            tweettext_encode = tweettext.encode('utf-8', 'ignore')  # Encoding it to a utf-8 format or ignoring it
            split_tweet = tweettext_encode.split(" ")  # Splitting the tweet by words

            # Running a loop in the words
            # If word is the dictionary, it picks up the score for that word or else takes 0
            for word in split_tweet:
                if word in tweet_score:
                    tweet_sum = tweet_sum + tweet_score.get(word.lower(), 0)

        if "place" in output_data and type(output_data["place"]) is not types.NoneType:
            if "full_name" in output_data["place"] and type(output_data["place"]["full_name"]) is not types.NoneType:
                if "country_code" in output_data["place"] and type(output_data["place"]["country"]) is not types.NoneType:
                    if output_data["place"]["country"] == 'United States':
                        state_cc_name = output_data["place"]["full_name"].encode("utf-8")
                        full_det = state_cc_name.split()
                        state = full_det[-1]
                        if len(state) == 2:
                            if state_sent_dict.has_key(state):
                                state_sent_dict[state] = state_sent_dict[state] + tweet_sum
                                state_count[state] +=1
                            else:
                                state_sent_dict[state] = tweet_sum
                                state_count[state] = 1

    #Calculating averages
    for j in state_sent_dict:
        average_state_score[j] = state_sent_dict[j]/state_count[j]

    # print average_state_score

    #store sorted dictionary
    sorted_average_state_score = sorted(average_state_score.items(), key= operator.itemgetter(1), reverse=True)

    #print sorted_dict
    for i in range(1):
        print sorted_average_state_score[i][0], sorted_average_state_score[i][1]


def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Storing the dictionary returned from getscore function
    tweet_score = getscore(sent_file)

    #Calculating sentiment
    calculateHappyState(tweet_score, tweet_file)

if __name__ == '__main__':
    main()
