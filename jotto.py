#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:59:18 2018

@author: najmabachelani
"""
import collections 
import math as m
import random

# Initial file read
def read_w5 () :
    w5file = "word5.txt"
    with open(w5file) as fin :
        result = [x.rstrip("\n") for x in fin.readlines()]
    return result

w5 = read_w5()

# Determines the jotto score given two strings.
def jotto_score(a,b) :
    acnt = collections.Counter(a)
    bcnt = collections.Counter(b)
    total = 0
    for c in acnt :
        total += min(acnt[c], bcnt[c])
    return total

# Count the distribution of jotto scores given a word and a candidate set.
# Returns Counter dict of score->count.
def count_jotto(word, cand) :
    dist = collections.Counter([jotto_score(word, x) for x in cand])
    return dist

# Produces a set of words from candidate set that are score n from 
def select_jotto(word, cand, n) :
    return [x for x in cand if jotto_score(word,x) == n]

# Measure the entropy of a word in partitioning a candidate set. 
def word_entropy (word, cand) :
    dist = count_jotto(word, cand)
    # sum negative p log2(p)
    all_sum = sum(dist.values())    
    ent = 0
    for k in dist :
        v = dist[k]
        p = v / all_sum
        ent += - p * m.log2(p)
    return ent

# Count of the highest bin in a distrobution histogram of word vs candidate.
def word_max (word, cand) :
    return max(count_jotto(word, cand).values())

# warning: is n^2 on the size of the candidates
def find_best_entropy(cand) :
    best_value = 0
    best_word = cand[0]
    for w in cand :
        ent = word_entropy(w, cand)
        if ent > best_value :
            best_value = ent
            best_word = w
            print ("picked", best_word, best_value)
    return best_word
    
def find_best_max(cand) :
    best_value = 9999
    best_word = "nope"
    for w in cand :
        m = word_max(w, cand)
        if m < best_value :
            best_value = m
            best_word = w
            print ("picked", best_word, best_value)
    return best_word

class Game :    
    def __init__(self, full_wordlist=w5) :
        print ("initing Game")
        self.full_wordlist = full_wordlist
        self.reset()
    def __str__(self) :
        return( "The word is " + self.secret_word)

    def reset (self) :
        self.candidates = self.full_wordlist
        self.guess_count = 0
        self.guess_list = []
        self.reset_word()

    def score(self, w) :
        return jotto_score(w, self.secret_word)
    
    def reset_word (self) :
        self.secret_word = random.choice(self.full_wordlist)
  
#Satesless game
def interactive_game_weak() :
    game = Game()
    count = 0
    score = 0
    while score is not 5 :
        w = input("Guess a Word ")
        count += 1
        score = game.score(w)
        print ("Your score is ", score)
    print ("Done!", game)
    print ("Number of guesses is ",count)
    
#Guess the first one game
def interactive_game_cand() :
    game = Game()
    cand = w5
    count = 0
    score = 0
    while score is not 5 :
        print ("Number of candidates left", len(cand))
        print ("Candidates are ", cand[:55])
        w = input("Guess a Word ")
        if len(w) == 0:
            w = cand[0]
            print ("  OK, autopicking ", w)
        count += 1
        score = game.score(w)
        cand = select_jotto(w, cand, score)
        print ("Your score is ", score)
    print ("Done!", game)
    print ("Final set", cand)
    print ("Number of guesses is ",count)

#Guess the best entropy
def interactive_game_ent() :
    game = Game()
    cand = w5
    count = 0
    score = 0
    while score is not 5 :
        print ("Number of candidates left", len(cand))
        print ("Candidates are ", cand[:55])
        w = input("Guess a Word ")
        if len(w) == 0:
            w = find_best_entropy(cand)
            print ("  OK, autopicking ", w)
        count += 1
        score = game.score(w)
        cand = select_jotto(w, cand, score)
        print ("Your score is ", score)
    print ("Done!", game)
    print ("Final set", cand)
    print ("Number of guesses is ",count)

#Guess the best entropy
def interactive_game_max() :
    game = Game()
    cand = w5
    count = 0
    score = 0
    while score is not 5 :
        print ("Number of candidates left", len(cand))
        print ("Candidates are ", cand[:55])
        w = input("Guess a Word ")
        if len(w) == 0:
            w = find_best_max(cand)
            print ("  OK, autopicking ", w)
        count += 1
        score = game.score(w)
        cand = select_jotto(w, cand, score)
        print ("Your score is ", score)
    print ("Done!", game)
    print ("Final set", cand)
    print ("Number of guesses is ",count)

 
