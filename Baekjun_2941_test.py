from Baekjun_2941 import count_croatian_alphabet_1, count_croatian_alphabet_2, count_croatian_alphabet_3
from random_string import random_string
from EncodingTable import make_encodingTable

encoding_table = make_encodingTable()

def test_count_croatian_alphabet_1():
    test_cases = [(random_string(10, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]), 10)]

    for word, answer in test_cases:
        my_answer = count_croatian_alphabet_1(word, encoding_table)
        assert my_answer == answer, f"Wrong answer. my_answer: {my_answer}, answer: {answer}"


def test_count_croatian_alphabet_2():
    test_cases = [(random_string(10, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=", "x="]), 10)]
    
    for word, answer in test_cases:
        my_answer = count_croatian_alphabet_2(word, encoding_table)
        assert my_answer == answer, f"Wrong answer. my_answer: {my_answer}, answer: {answer}"


def test_count_croatian_alphabet_3():
    test_cases = [(random_string(10, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]), 10)]

    for word, answer in test_cases:
        my_answer = count_croatian_alphabet_3(word, encoding_table)
        assert my_answer == answer, f"Wrong answer. my_answer: {my_answer}, answer: {answer}"


# encoding_table = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# test_v1 = [alphabet for alphabet in encoding_table]
# assert encoding_table == test_v1
# assert id(encoding_table) != id(test_v1)

# test_v2 = ["ljes=njak".count(alphabet) for alphabet in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]]
