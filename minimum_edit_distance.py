# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import Counter
import numpy as np
import pandas as pd

absolute_path = os.path.dirname(__file__)
relative_path = "shakespeare.txt"
full_path = os.path.join(absolute_path, relative_path)
print(full_path)

# UNQ_C1 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# GRADED FUNCTION: process_data
def process_data(file_name):
    """
    Input:
        A file_name which is found in your current directory. You just have to read it in.
    Output:
        words: a list containing all the words in the corpus (text file you read) in lower case.
    """
    words = []  # return this variable correctly

    with open(file_name) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+', file_name_data)

    return words


# DO NOT MODIFY THIS CELL
word_l = process_data(full_path)
vocab = set(word_l)  # this will be your new vocabulary
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")


