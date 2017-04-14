#!/usr/bin/python2


__author__ = 'Taylor Lee'
__email__  = 'tdlee2@wisc.edu'


import re
import sys

# Assumptions: I'm assuming the that if a file is not existant or cannot be read, that the IOError is satisfactory.
# I'm also assuming that the input file is in the same format as the sample input file, and that each line consists of only letters, no whitepaces.
# Since I modified a script that was given, I'll assume that the correct number of arguments is given during execution.


(filename, threshold) = sys.argv[1:3]

if len(threshold) != re.search('\d*(\.0*)?',threshold).end():
    print 'argv[2], \"threshold\", is not an integer'
    print 'argv[2] must be a non-negative integer.'
    print 'Terminating...'
    sys.exit(1)


threshold = int(float(threshold))


try:
    clean_list = open(filename).read().strip().split('\n')
except IOError as error:
    print 'IOError: ' , error
    print 'Terminating'
    sys.exit(1)


frequency_dictionary = {}
for word in clean_list:
    if word.upper() in frequency_dictionary:
        frequency_dictionary[word.upper()] += 1
    else:
        frequency_dictionary[word.upper()] = 1

for uppercase_word in sorted(frequency_dictionary):
    if frequency_dictionary[uppercase_word] >= int(threshold):
        print '{0:>10}: {1}'.format(uppercase_word, frequency_dictionary[uppercase_word])
