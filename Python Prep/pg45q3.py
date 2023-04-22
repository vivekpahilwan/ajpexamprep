# define a function to convert a number to its word representation
def number_to_words(num):
    # define a dictionary that maps each digit to its word representation
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    # convert the number to a string and split it into digits
    digits = list(str(num))
    # convert each digit to its word representation
    words = [digit_words[digit] for digit in digits]
    # join the word representations together with spaces
    return ' '.join(words)

# test the function with some example inputs
print(number_to_words(1234))
print(number_to_words(456))
print(number_to_words(7890))
