import sys


def tokenize(text_file_path):
    file = open(text_file_path, encoding="utf-8")
    tokens = list()
    for line in file:
        word = str()
        for char in line:
            if char.isalnum():
                word += char.lower()
            else:
                if word:
                    tokens.append(word)
                    word = str()
        if word:
            tokens.append(word)

    file.close()
    return tokens

def computeWordFrequencies(tokens):
    pass


def print_frequencies(frequencies):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
