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

## Get tweets
# input
username1 = sys.argv[1]
username2 = sys.argv[2]
num_tweets = sys.argv[3] if len(sys.argv) >= 4 else 20
consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

# OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)

# get tweets from api
baseurl = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
params1 = {'screen_name':username1, 'count':num_tweets}
params2 = {'screen_name':username2, 'count':num_tweets}
resp1 = requests.get(baseurl, params1, auth=auth)
resp2 = requests.get(baseurl, params2, auth=auth)
r1_json=json.loads(resp1.text)
r2_json=json.loads(resp2.text)

# gather tweet text
tokenized_list1=[]
tokenized_list2=[]
for i in r1_json:
    text=i['text']
    n_text=nltk.word_tokenize(text)
    tokenized_list1=tokenized_list1+n_text

for i in r2_json:
    text=i['text']
    n_text=nltk.word_tokenize(text)
    tokenized_list2=tokenized_list2+n_text


## Analyze most frequent common words
# function that ignores stop words
def ignore_word(list_of_words):
    word_keep = []
    for word in list_of_words:
        if (word not in ['','http','RT','https'] and word[0].isalpha()):
            word_keep.append(word)
    return word_keep

# function that gets frequency distribution
def freq_dict(l):
    d=dict()
    for i in l:
        d[i]=d.get(i, 0) + 1
    return d

# ignore stop words and get frequency distribution
tokenized_list_ignored1=ignore_word(tokenized_list1)
tokenized_list_ignored2=ignore_word(tokenized_list2)
freq_word1=freq_dict(tokenized_list_ignored1)
freq_word2=freq_dict(tokenized_list_ignored2)

# get common words
common_keys=set(freq_word1).intersection(freq_word2)
common=dict()
common_five=[]
for key in common_keys:
    common[key]=min(freq_word1[key],freq_word2[key])

common_sorted=sorted(common.items(), key=lambda kv: kv[1], reverse=True)
for i in common_sorted[0:5]:
    ii='{}({})'.format(i[0],i[1])
    common_five.append(ii)

common_five_str=' '.join(common_five)


## Analyze most frequent different words
# removes words shared by two users
def common_key_remove(common_keys, the_dict):
    for key in common_keys:
        if key in the_dict:
            del the_dict[key]

common_key_remove(common_keys,freq_word1)
common_key_remove(common_keys,freq_word2)
freq_word1_sorted=sorted(freq_word1.items(), key=lambda kv: kv[1], reverse=True)
freq_word2_sorted=sorted(freq_word2.items(), key=lambda kv: kv[1], reverse=True)

# get frequent diffent words
user1_diff_five=[]
user2_diff_five=[]
for i in freq_word1_sorted[0:5]:
    ii='{}({})'.format(i[0],i[1])
    user1_diff_five.append(ii)

for i in freq_word2_sorted[0:5]:
    ii='{}({})'.format(i[0],i[1])
    user2_diff_five.append(ii)

user1_diff_five_str=' '.join(user1_diff_five)
user2_diff_five_str=' '.join(user2_diff_five)


## Output
print('USER 1:', username1)
print('USER 2:', username2)
print('TWEETS ANALYZED:', min(len(r1_json),len(r2_json)))
print('5 MOST FREQUENT DIFFERENT WORDS FOR USER 1:', user1_diff_five_str)
print('5 MOST FREQUENT DIFFERENT WORDS FOR USER 2:', user2_diff_five_str)
print('5 MOST FREQUENT COMMON WORDS:', common_five_str)
