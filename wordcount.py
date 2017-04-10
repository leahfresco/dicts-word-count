from string import punctuation
import sys
from collections import Counter
from operator import itemgetter

# Opens text file
try:    
    filename = sys.argv[1]

    text_file = open(str(filename))

    # Counter for letter counts
    word_counts = Counter()

    # Iterates through file line by line
    for line in text_file:
        # Strips new line character at the end of each line
        line = line.rstrip()
        # Splits line by space into list of words in that line
        phrase = line.split(" ")
        for word in phrase:
            # Formats word to not include punctuation and be lowercase
            word = word.translate(None, punctuation)
            word = word.lower()
            word_counts[word] += 1

    # Sorts words alphabetically ascending
    word_counts = sorted(word_counts.items())

    # Sorts counts of words descending
    word_counts = sorted(word_counts, key=itemgetter(1), reverse=True)

    # Prints words
    for word, count in word_counts:
        print word, count

# Error for when file given is non-existant
except IOError:
    print "File not found"

# Error for when second argument is not provided on command line
except IndexError:
    print "Please define a file"