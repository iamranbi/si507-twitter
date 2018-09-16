# Twitter Program
Two simple programs that access Twitter and only touch your own data and analyze.

## Files
1. frequently_used_words.py
- a program that analyzes the twitter timeline of a selected user to list their most frequently used words
<br> - input arguments: \<a twitter username\> \<number of tweets to analyze\>
<br> - output: user name, number of tweets analyzed and the five most frequent words

2. common_unique_words.py
- a program that analyzes two twitter users' tweets to find words they have in common and words that are unique to each user
<br> - input arguments: \<twitter username 1\> \<twitter username 2\> \<number of tweets to analyze\> <br />
<br> - output: username 1, username 2, number of tweets analyzed, the five most frequent different for user1, the five most frequent different for user2, and five most frequent common words
<br> - if there is no argument passed for number of tweets, it will be assigned to 20

## User Guide
### run frequently_used_words.py
`$ python3 frequently_used_words.py \<a twitter username\> \<number of tweets to analyze\>`
<br> e.g. `$ python3 frequently_used_words.py umsi 25`

### run common_unique_words.py
`python3 common_unique_words.py \<twitter username 1\> \<twitter username 2\> \<number of tweets to analyze\>`
<br> e.g. `python3 common_unique_words.py umsi umichTECH 10`

For frequently_used_words.py and common_unique_words.py, you will need to create your own secrets.py file that includes:
<br> - CONSUMER_KEY = \<your twitter consumer key\>
<br> - CONSUMER_SECRET = \<your twitter consumer secret\>
<br> - ACCESS_KEY = \<your twitter access token\>
<br> - ACCESS_SECRET = \<your twitter access token secret\>

