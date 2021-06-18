def iskPalindrome(word):
    word = str(word)
    return word == word[::-1]


if __name__ == '__main__':
    print(iskPalindrome('1234321'))
    print(iskPalindrome(1215))
