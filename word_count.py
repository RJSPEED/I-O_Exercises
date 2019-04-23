"""LOGICAL APPROACH:
1. Create fx that takes a str and remove non-word chars, and stores in a list
2. Create a subsequent fx that takes the words in the list and pops a dict
   with word and related count
3. Create a final fx that outputs dict data in a table   

UNFINISHED: 1) Sort output and create table 2) Add try and accept logic re filename entry

"""
import re
import json
import collections

def string_format(input_string):
        #Use re.sub to identify all chars that are not in range a-z or A-Z
        #and then replace with a blank space, arguments = match pattern, replace
        #string, search string. Used casefold to remove capitalisation.
        return re.sub("[^a-zA-Z]","", input_string).casefold()

def counter_output(counter):
        print(counter)
        with open('bmy_count.json', 'w') as file_object:
                json.dump(counter, file_object, indent=2)


def word_count(filename):
    word_count_dict = {}
    text_list =[]
    formatted_list =[]
    with open(filename, 'r') as file_object:
        #Read entire file
        whole_text = file_object.read()
        #Add items split by blank space into list
        text_list = whole_text.split()
        #Next loop through list elements, feeding values into string_format fx
        #that removes none word chars and return the formatted value. Populate 
        #another list with formatted values.
        for i in text_list:
                formatted_list.append(string_format(i))
        #print(formatted_list)        
        #Use collections.counter to pop a dict of the unique words and their 
        #counts.
        #INFO: A Counter is a dict subclass for counting hashable objects. It's
        #an unordered collection where elements are stored as dictionary keys
        #and their counts are stored as dictionary values. Counts are allowed
        #to be any integer value including zero or negative counts.
        counter=collections.Counter(formatted_list)
        counter_output(counter)
        #print(counter)
        #print(sorted(counter.values()))
        
 
#word_count("rjs_test.txt")
word_count("test.txt")
#word_count("mobydick.txt")