def letter_starting_most_unique_words():
    '''returns the letter that starts maximum number of unique words in the datafile'''

    # ask the user for the name of the file
    filename = input("Enter the name of the file: ")

    # open the file
    with open(filename) as f:
        # read the file and save all the words in the file
        words = f.read().split()

    # create a set named unique_word
    unique_word = set()

    # loop through all the words, and add them to the set
    for word in words:
        # make sure to use casefold() method on each word
        # this is to make sure that all words are checked
        # in a way so that capital letters in the word dont matter
        unique_word.add(word.casefold())

    # create a dictionary to count the frequency of all first letters
    first_letter_counter = {}

    # loop through all the unique words,
    # and count the frequencies of all the first letters
    for word in unique_word:
        letter = word[0]
        if letter in first_letter_counter:
            first_letter_counter[letter] += 1
        else:
            first_letter_counter[letter] = 1

    # iterate through the dictionary of all the first letter frequencies
    # and find the max frequency
    max_count = 0
    for letter, count in first_letter_counter.items():
        if count >= max_count:
            max_count = count
            max_letter = letter

    # return the required letter with its count
    return [max_letter, max_count]


# call the function and print it's output
print(letter_starting_most_unique_words())



