import sys
import json
import numpy as np
import operator

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def CalculateHashtag(tweet_file):

    # Opening the Output file
    output_file = tweet_file

    # new lists
    hashtag_dict = {}
    top_ten = 10

    # Parsing every line in output file into json.loads
    for line in output_file:
        try:
            output_data = json.loads(line)
        except:
            continue

        if "entities" in output_data and output_data["lang"]=="en":
            if "hashtags" in output_data["entities"]:
                hashtag_list = output_data["entities"]["hashtags"]
                for hashtag in hashtag_list:
                    tag = hashtag["text"]
                    tag_encode = tag.encode('utf-8', 'ignore')
                    if tag_encode in hashtag_dict:
                        hashtag_dict[tag_encode] +=1
                    else:
                        hashtag_dict[tag_encode] = 1

    #store sorted dictionary
    sorted_dict = sorted(hashtag_dict.items(), key= operator.itemgetter(1), reverse=True)

    #print sorted_dict
    for i in range(top_ten):
        print sorted_dict[i][0], sorted_dict[i][1]


def main():

    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])

    #Calculate Frequencies
    CalculateHashtag(tweet_file)

if __name__ == '__main__':
    main()
