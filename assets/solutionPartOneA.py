#!/usr/bin/python2

import re
import sys

(filename, threshold) = sys.argv[1:3]

# Validate arguments
if (re.match("\D", threshold)):
   print "The threshold must be a number."
   sys.exit(1)

# Read file and tally word frequencies
# Original case of word does not matter: "the" = "The" = "THE"
fh = open(filename)
file = fh.read()
words = []  #### WORDS_LIST
for line in file.split('\n'):
   found = 0
   for word in words:
      if word[0] == line.lower(): ## COMPARE WORDS TO LOWERCASE LINE
         found = 1
         word[1] += 1

   # initialize a new word with a frequency of 1
   if found == 0:  ## FOUND ZERO BLOCK
      words.append([line, 1])

# Print words and their frequencies, sorted alphabetically by word.  Only
# print a word if its frequency is greater than or equal to the threshold.
for word in sorted(words):
   if word[0] < threshold: continue
   print "%4d %s" % (word[1], word[0])



