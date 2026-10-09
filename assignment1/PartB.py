import sys
from PartA import tokenize


def count_common_tokens(file_path_1, file_path_2):
    """
    O(n1 + n2) time complexity
    Tokenize each file once, convert to a set and return the length of set intersection
    """
    
    tokens_1 = set(tokenize(file_path_1))
    tokens_2 = set(tokenize(file_path_2))
    return len(tokens_1 & tokens_2)

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    print(count_common_tokens(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
