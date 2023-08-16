import random_string

def count_croatian_alphabet_1(word):
    croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]
    count = 0
    i = 0

    while i < len(word):
        found = False
        for alphabet in croatian_alphabet:
            if word[i:i+len(alphabet)] == alphabet:
                count += 1
                i += len(alphabet)
                found = True
                break
        
        if not found:
            count += 1
            i += 1
    
    return count


# count_croatian_alphabet_2 = lambda word: len(word) - sum([word.count(alphabet) for alphabet in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]])
def count_croatian_alphabet_2(word):
    # check pre-conditions
    # encoding table 이 valid 한지 확인해야 함
    cnt = sum([word.count(alphabet) * (len(alphabet) - 1) for alphabet in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]])
    return len(word) - cnt


# 크로아티아 알파벳을 찾는 함수 count_croatian_alphabet_3()을 구현하기
# 단 반복문, 람다식, 내장함수를 사용하지 않고 구현하기
def count_croatian_alphabet_3(word):
    croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]
    count = 0    

    for alphabet in croatian_alphabet:
        count += word.count(alphabet)
        word = word.replace(alphabet, "▁")

    count += len(word.replace("▁", ""))
    return count


def count_croatian_alphabet_4(word):
    croatian_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]
    count = 0    

    for alphabet in croatian_alphabet:
        count += word.count(alphabet)
        word = word.replace(alphabet, "▁")

    count += len(word) - word.count("▁")
    return count


if __name__ == "__main__":
    word = input()
    result = count_croatian_alphabet_3(word)
    print(result)