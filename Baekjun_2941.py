import random_string
import EncodingTable

class CountCroatianAlphabet:
    def __init__(self, encoding_table) -> None:
        self.encoding_table = encoding_table
        assert EncodingTable.check_encodingTable(encoding_table), "Encoding table is not valid."

    def count_croatian_alphabet(self, word):
        return count_croatian_alphabet_2(word, self.encoding_table)

def count_croatian_alphabet_1(word, encoding_table):
    count = 0
    i = 0

    while i < len(word):
        found = False
        for alphabet in encoding_table:
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
def count_croatian_alphabet_2(word, encoding_table):
    cnt = sum([word.count(alphabet) * (len(alphabet) - 1) for alphabet in encoding_table])
    return len(word) - cnt


# 크로아티아 알파벳을 찾는 함수 count_croatian_alphabet_3()을 구현하기
# 단 반복문, 람다식, 내장함수를 사용하지 않고 구현하기
def count_croatian_alphabet_3(word, encoding_table):
    count = 0    

    for alphabet in encoding_table:
        count += word.count(alphabet)
        word = word.replace(alphabet, "▁")

    count += len(word.replace("▁", ""))
    return count


def count_croatian_alphabet_4(word, encoding_table):
    count = 0    

    for alphabet in encoding_table:
        count += word.count(alphabet)
        word = word.replace(alphabet, "▁")

    count += len(word) - word.count("▁")
    return count


if __name__ == "__main__":
    for _ in range(10):
        encoding_table = EncodingTable.make_encodingTable()
        print("encoding_table: ", encoding_table)
        try:
            counter = CountCroatianAlphabet(encoding_table)
        except AssertionError as e:
            continue
        break

    for _ in range(10):
        m = int(input("문자열의 길이를 입력하세요:  "))
        word = random_string.random_string(m, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=-") + encoding_table)
        print("word: ", word)
        result = counter.count_croatian_alphabet(word)
        print("코르아티아 알파벳을 포함한 문자열의 길이:", result)
