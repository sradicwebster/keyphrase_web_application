# references to flair commented out
#from flair.embeddings import Sentence
#from flair.models import SequenceTagger
from nltk.tokenize import TreebankWordTokenizer as twt
import dill

class PublicationKeyPhrase:
    def __init__(self, text):
        self.text = text

    # references to flair commented out
    '''
    def get_key_phrases_flair(self):

        model = SequenceTagger.load('path to model.pt')
        sentence = Sentence(self.text)
        model.predict(sentence)
        tagged = sentence.to_tagged_string().split(' ')

        kp_words = []
        for i, word in enumerate(tagged):
            if word == '<B>':
                kp_words.append(tagged[i-1:i+1])
            elif word == '<I>':
                kp_words.append(tagged[i-1:i+1])

        index_b = []
        for i, word in enumerate(kp_words):
            if kp_words[i][1] == '<B>':
                index_b.append(i)

        key_phrase = []
        for i, num in enumerate(index_b):
            if i < len(index_b)-1:
                key_phrase.append(' '.join([kp_words[j][0] for j in range(num,index_b[i+1])]))
            else:
                key_phrase.append(' '.join([kp_words[j][0] for j in range(num,len(kp_words))]))

        return key_phrase
    '''

    def get_key_phrases_hmm(self):

        with open('hmm_tagger.dill', 'rb') as f:
            tagger = dill.load(f)

        tokens = list(twt().tokenize(self.text))
        tagged_words = tagger.tag(tokens)

        kp_words = []
        for i, word in enumerate(tagged_words):
            if word[1] == 'B':
                kp_words.append(tagged_words[i])
            elif word[1] == 'I':
                kp_words.append(tagged_words[i])

        index_b = []
        for i, word in enumerate(kp_words):
            if word[1] == 'B':
                index_b.append(i)

        key_phrase = []
        for i, num in enumerate(index_b):
            if i < len(index_b) - 1:
                key_phrase.append(' '.join([kp_words[j][0] for j in range(num, index_b[i + 1])]))
            else:
                key_phrase.append(' '.join([kp_words[j][0] for j in range(num, len(kp_words))]))

        return key_phrase
