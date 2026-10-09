import sys
import heapq

def tokenize(text_file_path):
    file = open(text_file_path, encoding="utf-8", errors="ignore")
    tokens = list()
    """
    O(n) time complexity
    Iterate through each char
    If char is alnum, concat to str
    If char is not alnum,
        if word str is not empty, append to tokens and reset word
    after finish iteration, if word str is not empty, append last token to tokens
    """
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

def compute_word_frequencies(tokens):
    """
    O(m) time complexity 
    use hashmap, if token in hashmap, increment that key by 1. if token not in hashmap, create new key with token
    """
    hashmap = dict()
    for token in tokens:
        if token not in hashmap:
            hashmap[token] = 1
        else:
            hashmap[token] += 1
    return hashmap


def print_frequencies(frequencies):
    """
    O(k log k) time complexity
    Use max heap (negative since default heap is min heap)
    push all freq and tokens into max heap (heapify)
    pop everything from heap from most to least
    """
    max_heap = list()
    for token, count in frequencies.items():
        heapq.heappush(max_heap, (-count, token))
    while max_heap:
        neg_count, token = heapq.heappop(max_heap)
        print(f"{token} - {-neg_count}")
        


def main():
    tokens = tokenize(sys.argv[1])
    freq = compute_word_frequencies(tokens)
    print_frequencies(freq)


if __name__ == "__main__":
    main()
