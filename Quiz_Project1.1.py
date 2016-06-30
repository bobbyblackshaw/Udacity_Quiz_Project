# IPND Stage 2 Final Project

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:01:51 2016
Last Edited on Wed Jun 29 23:18:00 2016
@author: robertblackshaw
"""
##############################################################################
'''A list of numbered spaces to be passed in to the quiz function.'''
set_list = ["___1___", "___2___", "___3___", #doesn't change
            "___4___", "___5___", "___6___"]
fill_in_numbers  = ["___1___", "___2___", "___3___", #changes with inputs
                    "___4___", "___5___", "___6___"]
##############################################################################
'''lists with the answers to each difficulty string'''
easy_answers = ["mercury", "venus", "earth", "mars"]
medium_answers = ["coffee", "morning", "caffeine", "light", "dark"]
hard_answers = ["spacex", "rocket", "cargo", "elon musk", "tesla", "paypal"]

##############################################################################
'''The strings used for the quiz'''
easy_string = '''The four closest planets to our Sun in order are 
___1___, ___2___, ___3___, ___4___.'''

medium_string = '''___1___ is a good drink to have in the ___2___. 
It has ___3___ which helps people wake up. ___4___ roast coffee has more 
caffeine than ___5___ roast.'''

hard_string = '''___1___ is the first private ___2___ company to 
deliver ___3___ to the International Space Station. ___4___ is the 
CEO of ___1___, as well as ___5___ motors, and co-founded ___6___.'''
##############################################################################

def fin_check(word, fill_in_numbers):
    '''Checks if a word in fill_in_numbers is asubstring of the word
passed in.'''
    for fin in fill_in_numbers:
        if fin in word:
            return fin
    return None
##############################################################################

def log_entries(fill_in_numbers, word, new):
    '''Replaces the blank space numbers in fill_in_numbers with the 
entry given by the user. This is so if there are multiple occurences of a
blank space number, the word already used can be easily accessible
input:  list of numbered spaces, a numbered space, a word inputted by the user
no output: just modifies the list fill_in_numbers'''
    if fin_check(word, fill_in_numbers) != None and word in fill_in_numbers:
        index_of_number = fill_in_numbers.index(word)                               
        fill_in_numbers[index_of_number] = new  #updates fill_in_numbers
                                                
        
##############################################################################

def start(fill_in_numbers):
    '''Prompts the user to pick a difficulty and returns the corresponding 
string and the answers'''
    print '''Select a difficulty by typing it in. Options are: easy, 
medium, and hard.'''
    while True:
        difficulty = raw_input("Enter here:  ")
        if difficulty.lower() == "easy":
            return easy_string, easy_answers
        elif difficulty.lower() == "medium":
            return medium_string, medium_answers
        elif difficulty.lower() == "hard":
            return hard_string, hard_answers
        else:
            print "Not a valid answer. Try again."
            continue

##############################################################################
def ask_and_check(replacement, difficulty):
    #prompt the user
    user_input = raw_input("Space Number " + replacement + ":  ")
    user_input = user_input.lower()
    #check if it is right
    while user_input != difficulty[set_list.index(replacement)]:
        #if not correct, try again until right
        user_input = raw_input("Incorrect, try again. Space Number" 
                                + replacement + ":  ")
        print "\n"
        user_input = user_input.lower()
    return user_input


##############################################################################


def quiz(fill_in_numbers): 
    '''This the the quiz. It prints the unfilled in quiz paragraph and 
prompts the user. The user answers the questions to fill in the blanks'''
    fin_string, difficulty = start(fill_in_numbers) #gets string and answers
    print fin_string
    fin_string = fin_string.split() #makes the string a list
    for word in fin_string:
        replacement = fin_check(word, set_list)
        if replacement != None: #checks if word is a numbered space
            if replacement not in fill_in_numbers: 
                #if it is, check if it has been answered already
                index_of_number = set_list.index(replacement)
                word = fill_in_numbers[index_of_number]  
                #if it has, assign to word the entry that has
                #replaced the numbered space already
            else:                                       
                user_input = ask_and_check(replacement, difficulty)
                log_entries(fill_in_numbers, replacement, user_input) 
                #make this a function
                '''word = word.replace(replacement, user_input)
                fin_string = " ".join(fin_string)
                if word[-1] == "." or word[-1] == ",": #check for punctuation
                    word = word[:-1]
                fin_string = fin_string.replace(replacement, word)
                print fin_string
                fin_string = fin_string.split()'''
                
quiz(fill_in_numbers)
