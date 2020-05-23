from flair.embeddings import Sentence
from flair.models import SequenceTagger
import numpy as np

class PublicationKeyPhrase:
    def __init__(self, text):
        self.text = text

    def get_key_phrases(self):

        model = SequenceTagger.load('/Users/hn19405/OneDrive - University of Bristol/Group Project/individual_project/flair_model/final-model.pt')

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

        #np.savetxt('test_ks.txt', key_phrase, fmt='%s')

        return key_phrase