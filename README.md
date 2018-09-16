
SI 507 
Homework 5: OAuth and Caching <br />
Name:Ran Bi<br />
section day/time: 004 Monday 7-8:30p<br />

FILENAME 1: hw5_twitter.py
- a program to analyze the twitter timeline of a selected user to list their most frequently used words
- input arguments: \<a twitter username\> \<number of tweets to analyze\>
- output: user name, number of tweets analyzed and the five most frequent words that 
- sample:<br />
	xxxx$ python3 hw5_twitter.py umsi 25 <br />
	USER: umsi <br />
	TWEETS ANALYZED: 25 <br />
	5 MOST FREQUENT WORDS: umichTECH(16) to(13) and(13) the(12) of(10) <br />

FILENAME 2(for Extra Credit 1): hw5_twitter_ec1.py
- a program that analyzes two twitter users' tweets to find words they have in common and words that are unique to each user
- input arguments: \<twitter username 1\> \<twitter username 2\> \<number of tweets to analyze\> <br />
p.s. if there is no argument passed for number of tweets, it will be assigned to 20
- output: username 1, username 2, number of tweets analyzed, the five most frequent different for user1, the five most frequent different for user2, and five most frequent common words
- sample:<br />
	xxxx$ python3 hw5_twitter_ec1.py umsi umichTECH 10 <br />
	USER 1: umsi <br />
	USER 2: umichTECH <br />
	TWEETS ANALYZED: 10 <br />
	5 MOST FREQUENT DIFFERENT WORDS FOR USER 1: QuasiCon(3) our(3) today(3) Session(2) Panel(2) <br />
	5 MOST FREQUENT DIFFERENT WORDS FOR USER 2: your(6) see(3) info(3) settings(2) new(2) <br />
	5 MOST FREQUENT COMMON WORDS: the(4) in(3) a(3) to(3) you(2) <br />

p.s.<br />
For hw5_twitter.py and hw5_twitter_ec1.py, you will need to create your own secrets.py file that includes:<br />
CONSUMER_KEY = \<your twitter consumer key\> <br />
CONSUMER_SECRET = \<your twitter consumer secret\> <br />
ACCESS_KEY = \<your twitter access token\> <br />
ACCESS_SECRET = \<your twitter access token secret\> <br />

