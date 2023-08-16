import random_string
import random

# def test_random_string1():
#     n = random.randint(1, 100)
#     assert len(random_string.random_string1(n)) == n

# def test_random_string2():
#     n = random.randint(1, 100)
#     assert len(random_string.random_string2(n)) == n

# def test_random_string3():
#     n = random.randint(1, 100)
#     assert len(random_string.random_string3(n)) == n

# def test_random_string4():
#     n = random.randint(1, 100)
#     assert len(random_string.random_string4(n)) == n

# def test_random_string5():
#     n = random.randint(1, 100)
#     assert len(random_string.random_string5(n)) == n

def test_random_string():
    n = random.randint(1, 100)
    candidates = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ")
    result = random_string.random_string(n, candidates)

    print("예상 길이:", n)
    print("실제 길이:", len(result))
    assert len(result) == n

     # 생성된 문자열이 candidates 리스트 내 문자만 포함하는지 테스트
    for char in result:
        assert char in candidates

    # 빈 candidates 리스트로 테스트
    empty_candidates = []
    empty_result = random_string.random_string(n, empty_candidates)
    assert len(empty_result) == 0

    # n = 1로 테스트
    single_char_result = random_string.random_string(1, candidates)
    assert len(single_char_result) == 1

    print("test_random_string passed")


if __name__ == "__main__":
    for _ in range(100):
        test_random_string()
