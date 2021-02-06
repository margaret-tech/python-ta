import sys
import os


def palindrome(s):
    # your code goes here
    print("Word to test: ", s)
    # remove spaces
    word_no_space = s.replace(" ", "")
    # convert to uppercase
    new_word = word_no_space.upper()
    print("New is: ", new_word)
    # convert word to list of characters
    word_list = list(new_word)
    print("New as list: ", word_list)
    # create a copy of word list
    reverse_word_list = word_list.copy()
    # reverse the characters in the word list
    reverse_word_list.reverse()
    print("Reverse as list: ", reverse_word_list)
    # compare reversed list and original list
    if word_list == reverse_word_list:
        return True
    else:
        return False


def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
