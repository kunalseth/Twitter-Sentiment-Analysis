import sys
import json
import numpy as np

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def CalculateFrequency(tweet_file):

    # Opening the Output file
    output_file = tweet_file

    # new lists
    term_dict = {}


    # Parsing every line in output file into json.loads
    for line in output_file:
        try:
            output_data = json.loads(line)
        except:
            continue

        if "text" in output_data and output_data["lang"]=="en":
            tweettext = output_data["text"]  # Storing the text of the tweet line
            tweettext_encode = tweettext.encode('utf-8', 'ignore')  # Encoding it to a utf-8 format or ignoring it
            split_tweet = tweettext_encode.split(" ")  # Splitting the tweet by words

            for term in split_tweet:
                if term in term_dict:
                    term_dict[term] +=1
                else:
                    term_dict[term] = 1


    # print term_dict
    # print len(term_dict)

    for c in sorted(term_dict, key=term_dict.get):
        print c, ' ', float(term_dict[c])/float(len(term_dict))

def main():

    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])

    #Calculate Frequencies
    CalculateFrequency(tweet_file)

if __name__ == '__main__':
    main()
