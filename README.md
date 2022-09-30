# Sentiment-Analysis

Sentiment analysis is the method of identifying emotions from a sentence based on the usage of words by a person. The
emotions can be classified as positive, neutral, or negative. The social media is flooded with people voicing their opinions
on things around them every day. 

In twitter there are a few challenges: the maximum word limit of a “tweet” is of 140 characters, hence the public tends to
use slangs or short-forms or emoticons to express their views. To analyse the tweets, we need to do pre-processing, that
will include the following:
1. Removal of @user string, and the preceding text before the actual tweet.
2. Removal of ‘#’ (hash-tags)
3. Replacing of slangs and abbreviations with actual words.
4. Removal of repeated character. For eg, three or more consecutive ‘o’s will be replaced by two ‘o’s.

After the pre-processing is done, Lexicon based Analyser is used for the polarity detection of the tweets and to generate
features that can be used for training a machine-learning classifier. Lexicon based analysis is based on breaking down the
text into tokens of word and to check for the presence of nouns, adjectives, adverbs, etc in the text, and negative and
positive words. Feature generation includes features like number of positive words, number of negative words, special
keywords, presence of negation, emoticons, etc.

### How to run:
python application.py
