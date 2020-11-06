def palindrome(word):
    word = word.replace(' ','').lower()
    word_invert = word[::-1]
    if(word == word_invert):
        return True
    else:
        return False


def run():
    word = input("Enter a word : ")
    is_pali = palindrome(word)

    if is_pali == True:
        print("Is Palindrome")
    else:
        print("Is not Palindrome")


if __name__ == "__main__":
    run()
