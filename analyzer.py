import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positive_set = set()
        file = open(positives, "r")
        
        for line in file:
            if line.startswith(';') == False:
                self.positive_set.add(line.rstrip("\n"))
        file.close()
        
        self.negative_set = set()
        file = open(negatives, "r")
        
        for line in file:
            if line.startswith(';') == False:
                self.negative_set.add(line.rstrip("\n"))
        file.close()
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        for word in tokens:
            if word.lower() in self.positive_set:
                score +=1
            elif word.lower() in self.negative_set:
                score -=1
            else:
                continue
            
        
        return score
                
