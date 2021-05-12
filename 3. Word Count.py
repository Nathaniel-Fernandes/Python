# Date: 12 May 2021
# Author: Nathaniel Fernandes
# Description: When run, the user is asked to enter a phrase and we'll calculate how many words are in it!
# Difficulty: 2/10

# A. Ask for input and format response
phrase = input("How is your day going?: ")
split_phrase = phrase.split(" ")

#B. Count the number of words
num_words = 0
for i in range(0, len(split_phrase)): # make sure that double/triple spaces only count as 1 word
    if split_phrase[i] != "":
        num_words += 1

# C. Response
# Modify response if only 1 word so grammar makes sense
if num_words == 1:
    print("Wow! You just entered 1 word")
else:
    print("Wow! You just entered %d words" % num_words)

# Lessons Learned
# 1. You can split a string by a character with the ".split()" function
# 2. Use len() to calculate the length of an array