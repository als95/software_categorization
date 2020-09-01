import codecs

import gensim as gensim
from nltk.corpus import stopwords
import re

from sklearn.feature_extraction.text import CountVectorizer


class WordVecModeler:
    def __init__(self, word_dim):
        self.word_dim = word_dim
        self.word_model = None
        self.doc_x = None
        pass

    def load_word_vec(self, word_model_name):
        self.word_model = gensim.models.KeyedVectors.load_word2vec_format(word_model_name, binary=True)
        return self.word_model

    def get_vector_from_word(self, word):
        if self.word_model is None:
            raise ModuleNotFoundError("불러와진 모델이 없습니다. load_word_vec 을 먼저 호출해주세요")
        if word in self.word_model:
            return self.word_model[word]
        else:
            return None


