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



# PROBLEMS WITH THE ABOVE SCRIPT:

# 1. Words with uppercase characters are treated as new words:
#    At line 20, this 'for' loop compares each word in the WORDS_LIST to the value of the current line enacted on by the string function 'lower()'. This would seem to give the script the case-agnostic feature the description describes, however if a given line, in its lowercase form, is not found in the word list, the line is appended to the wordlist as it was read from the file, without the 'lower()' string function being called. The creates the issue that any word in the WORD_LIST that has an uppercase character will not match with any line read from the file, and hence every line from the file that initially has an uppercase character will be added to the word list with the default initial frequency of '1'. Thus, the output displays every instance of a word with an uppercase character as being unique, even when it is not in even a case sensitive sense.

# 2. Threshold not observed:
#    At line 31. we have a 'for' loop which iterates through the WORDS_LIST as returned by the built-in function 'sorted()'. At line 32, we have a threshold test, however this threshold test is insufficient for a couple of reasons. First, if you look at the index in 'word[0]', this index will access word itself and not its frequency. And on the other end of this comparison, 'threshold' is the string of the command line argument sys.argv[2], and not an integer. Hence, all that is really happening here is a string comparison between the ascii values of the two first characters in the two strings. Since the ascii value of every integer is less than the ascii value of every alphabetical string, both upper and lower case, the continue statement will never be reached, the print statement will always be reached, and in effect the threshold will never be observed for any word, no matter the frequency. Every word will be displayed.

# 3. Threshold form check insufficient.
#    The threshold validation at line 9 will tolerate any string, as long as the first character is not a non-digit character. With the script as it is, where the threshold is not correctly checked just prior to each number's display, this will not be an issue. However, if we go on to correct the threshold check, and want it to work correctly, then we must tighten the validation process. At some point, our threshold will be converted into an integer for the threshold check, and we must ensure that the string representation of threshold from sys.argv[2] not only can be converted into an integer, but that it is converted into the integer we want. For instance, if sys.argv[2] is given as a floating point number like '25.5', the built-in function 'int()' will convert this to the integer 25. While this may very well be fine, we must make sure the user knows that their input has been rounded down, or perhaps we might even consider rejecting this argument by tightening the validation process to not accept strings which have a decimal point or are not in the 'pullback' of the 'int()' function i.e. they are not in the image of 'float()' when considering a domain of all integers.


# Final remarks: Fixing the script requires not only addressing the three above concerns, but addressing them in the correct way, as they conceal subtleties that would be flaws in the code in their own right, but in this case are contained within  broader flaws. First, a manner of recording words in a uniform, case agnostic manner is necessary. This will allow for the same word to be counted, no matter what case its characters are in. Also, the lines read from the file will need to be converted in this uniform manner before comparison can take place, otherwise matching words of different cases can not be detected, and a new word is erroneously added to the WORDS_LIST. Having a universal representation of each word, such as all lowercase or all uppercase, will allow the 'sorted()' function to accurately put the words into alphabetical order for their enumeration and display. Secondly, for the threshold comparison at line 32, we need to fix the index of the left hand side from 'word[0]' to 'word[1]' in order to access the frequency instead of the word itself. Also, we must convert the string 'threshold' in this comparison into an integer, either at the line 32 itself or earlier in the script. This will ensure that threshold is recognized and obeyed.
