""" ---------------------------------------------------
    Code Word Generation Class
----------------------------------------------------"""

import numpy as np
import pandas as pd

class Code_Gen():

    k_variable = 0
    r_word_length = 0
    simulation_length = 0
    code_words = []

    def __init__(self, k_valid_words , r_word_length ,l_words):
        '''This init refers the inputs wit the document symbols
        k_valid_words: k (code words based on rate R)
        r_word_lengh : R (rate)
        l_words      : L (simulation length)
        '''
        self.k_variable = k_valid_words
        self.rate = r_word_length 
        self.simulation_length = l_words
        self.code_words = [] #keep empty for now



