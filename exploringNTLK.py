# Author: VIJAYALAKSHMI GUNASEKARAPANDIAN
# Here, I explore analyzing text using the python package ntlk
# The objective is to write a function named analyze(book_name)
# based onnltkthat takes the name of a novel
# (in this case a particular novel accessible though nltk),
# to analyze it and print a summary of word count, char count,
# longest sentence, etc. 

import re
import nltk
from nltk.corpus import gutenberg
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 


def analyze(book_name):
    ps = PorterStemmer()
    wordlist = {}
    vocab_size = []
    max_sentence_len, max_word_len, max_len, cur_len = 0, 0, 0, 0
    longest_word, longest_sentence, max_fam = '', '', ''
    print("# chars =",len(gutenberg.raw(book_name)))
    print("# words =",len(gutenberg.words(book_name)))
    print("# sentences =",len(gutenberg.sents(book_name)))
    book_sentences =  gutenberg.sents(book_name)
    max_sentence_len = max(len(s) for s in book_sentences)
    longest_sentence = [s for s in book_sentences if len(s) == max_sentence_len][0]
    max_word_len = max(len(w) for w in gutenberg.words(book_name))
    print("Longest word ='",[w for w in gutenberg.words(book_name) if len(w) == max_word_len][0],"'")
    print("Longest sentence ='",longest_sentence[0], ' ', longest_sentence[1], \
          ' ', longest_sentence[2], '...', longest_sentence[max_sentence_len-1] \
          if (longest_sentence[max_sentence_len-1]).isalpha() else \
          longest_sentence[max_sentence_len-2],"'(",max_sentence_len,"words)")
    for w in gutenberg.words(book_name): 
        if ps.stem(w) in wordlist.keys():
            wordlist[ps.stem(w)].append(w)
            wordlist[ps.stem(w)] = list(dict.fromkeys(wordlist[ps.stem(w)]))
            cur_len = len(wordlist[ps.stem(w)])
            if cur_len > max_len:
                max_len = cur_len
                max_fam = ps.stem(w)
        else:    
            wordlist[ps.stem(w)] = [w]
    [vocab_size.append(li) for li in wordlist if li.isalpha()]
    print(len("Vocab size ",vocab_size))
    print("Largest stem family ", "'",max_fam,"':")
    print(wordlist[max_fam])
            
    
