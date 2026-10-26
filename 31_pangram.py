"""Program 31: Check whether a string is a pangram."""


def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if char.isalpha() and "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(is_pangram(text))