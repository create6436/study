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
encoding_table = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=", "x="]

def count_croatian_alphabet_2(word):
    cnt = sum([word.count(alphabet) * (len(alphabet) - 1) for alphabet in encoding_table])
    return len(word) - cnt

def overlapping_encoding(encoding_table):
    for i, encoding1 in enumerate(encoding_table):
        for j, encoding2 in enumerate(encoding_table):
            if i != j and encoding1.endswith(encoding2[0]):
                return True
    return False



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
    import random_string

    # 겹치는 경우가 있는지 체크
    has_overlap = overlapping_encoding(encoding_table)
    if has_overlap:
        print("인코딩 테이블 리스트에 겹치는 경우가 있습니다.")
    else:
        print("인코딩 테이블 리스트에 겹치는 경우가 없습니다.")

    m = int(input("문자열의 길이를 입력하세요:  "))
    word = random_string.random_string(m, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="])
    print(word)
    result = count_croatian_alphabet_3(word)
    print("코르아티아 알파벳을 포함한 문자열의 길이:", result)
