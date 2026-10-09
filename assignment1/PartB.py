import sys
from PartA import tokenize

def count_common_tokens(file_path_1, file_path_2):
    token1_set = set(tokenize(file_path_1))
    token2_list = tokenize(file_path_2)
    count = 0
    
    for token in token2_list:
        if token in token1_set:
            count += 1
            token1_set.discard(token)
        if not token1_set:
            break
    return count

def main():
    print(count_common_tokens(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
    main()
