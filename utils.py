"""----------------------------------------------------
    Utils modules: contains functions and 
    usefull methods
----------------------------------------------------"""

import numpy as np
import pandas as pd


def make_col(cols):
    '''Creates Columns
    '''
    col_n = cols
    col = []

    while col_n > 0:
        col.append('bit '+str(col_n))
        col_n =-1

    return col


def array_burst_gen(word_length, n_words):
    ''' Array burst Generator:
    :: Creates a number of "n_words" random
        binary arrays with "word_length" items.
    :: return file location of generated words
    '''
    data = []
    loops = n_words

    while loops > 0:
        data= np.append(data, np.random.randint(2, size = word_length))
        loops -= 1
        #should generate and array of arrays
    
    data = np.reshape(data,(n_words,word_length))   
    
    return data


def make_file(data, col, filename='teste.csv'):
    '''Create Dataframe from Array
    '''
    df_bits = pd.DataFrame(data, columns=make_col(col))
    df_bits.to_csv(filename)

    return 'done'



