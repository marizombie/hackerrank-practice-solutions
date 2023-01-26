import os


def get_all_substrings(s):    
    return [[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]

    
def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]
    
    
def sherlockAndAnagrams(s):    
    substrings = get_all_substrings(s)
    flattened_substrings = flatten(substrings)
    counter_dict = {}
    for substring in flattened_substrings:
        alph = ''.join(sorted(substring))
        if alph in counter_dict:
            counter_dict[alph] += 1
        else:
            counter_dict[alph] = 1
    
    filtered = [i*(i-1)//2 for i in counter_dict.values() if i > 1]
    print(filtered)
    return sum(filtered)           


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
