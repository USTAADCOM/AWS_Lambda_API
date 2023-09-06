"""
word count module will take the string and return the word count of each word.
"""
from collections import Counter

def word_frequency_count_method(text_str: str)-> dict:
    """
    word_count_method will take a string and return the frequency of each word.

    Parameters
    ----------

    text_str: str
        string conatin the text data.
    
    Return
    ------
        return dictionary as output with count of each frequency.
    """
    output_dict = {}
    word_counts = Counter(text_str.split())
    for word, count in word_counts.items():
        output_dict[word] = count
    return output_dict
