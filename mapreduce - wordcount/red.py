#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018


# reducer wordcount
import sys
 
current_word = None
word = None
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    try:
        word, count = line.split('\t', 1)
    except:
        pass
 
    # convert count (currently a string) to int
    try:
        count = int(count)
    #except ValueError:
    except:
        # count was not a number, so silently
        # ignore/discard this line
        continue
 
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            #print '%s\t%s' % (current_word, current_count)
            print(current_word + "\t" + str(current_count))
        current_count = count
        current_word = word
 
# do not forget to output the last word if needed!
if current_word == word:
    #print '%s\t%s' % (current_word, str(current_count))
    print(current_word + "\t" + str(current_count))
