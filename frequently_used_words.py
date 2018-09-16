from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk

## if the package punkt is not installed on your computer, please uncomment the following section of code.
#import ssl
#try:
    #_create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
    #pass
#else:
    #ssl._create_default_https_context = _create_unverified_https_context
#nltk.download('punkt')

username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

## code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)

## caching
CACHE_FNAME = 'twitter_cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def params_unique_combination(baseurl, params):
    alphabetized_keys = sorted(params.keys(),reverse=True)
    res = []
    for k in alphabetized_keys:
        res.append('{}={}'.format(k, params[k]))
    return baseurl + '?'+ "&".join(res)

def make_request_using_cache(baseurl, params):
    unique_ident = params_unique_combination(baseurl,params)
    # look in the cache to see if already have this data
    if unique_ident in CACHE_DICTION:
        print('Fetching cached data...')
        print('----------------')
        return CACHE_DICTION[unique_ident]
    # if not, fetch the data afresh, add it to the cache, write the cache to file
    else:
        print('Making request for new data...')
        print('----------------')
        resp = requests.get(baseurl, params, auth=auth)
        CACHE_DICTION[unique_ident] = json.loads(resp.text)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close()
        return CACHE_DICTION[unique_ident]

# get Tweets
baseurl = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
params = {'screen_name':username, 'count':num_tweets}
# fetch tweets
r_json=make_request_using_cache(baseurl, params)
##write the json returned
#with open('tweet.json', 'w') as f:
    #json.dump(r_json,f,indent=2)

# analyze Tweets
def ignore_word(list_of_words):
    word_keep = []
    for word in list_of_words:
        if (word not in ['','http','RT','https'] and word[0].isalpha()):
            word_keep.append(word)
    return word_keep

tokenized_list=[]
freq_word_five=[]
# gather tweet data from the response of twitter api
for i in r_json:
    text=i['text']
    n_text=nltk.word_tokenize(text)
    tokenized_list=tokenized_list+n_text
# ignore stop words
tokenized_list_ignored=ignore_word(tokenized_list)
# get a frequency distribution of the tokenized list
freq_word=nltk.FreqDist(tokenized_list_ignored)
# 5 most frequently used words
for i in freq_word.most_common(5):
    ii='{}({})'.format(i[0],i[1])
    freq_word_five.append(ii)
freq_word_str=' '.join(freq_word_five)
print('USER:', username)
print('TWEETS ANALYZED:', len(r_json))
print('5 MOST FREQUENT WORDS:', freq_word_str)


if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
