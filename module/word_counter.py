"""
word count module will take the string and return the word count of each word.
"""
from collections import Counter

def word_count_method(text_str: str, word: str)-> dict:
    """
    word_count_method will take a string and word as input and return its count 
    in given string.

    Parameters
    ----------

    text_str: str
        string from which we find the specific word count.
    word: str
        word to find the count.
    
    Return
    ------
        return dictionary as output with count of specific number.
    """
    output_dict = {}
    word_counts = Counter(text_str.split())
    # for word, count in word_counts.items():
    #     output_dict[word] = count
    output_dict[word] = word_counts[word]
    return output_dict
