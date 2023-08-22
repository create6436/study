from Baekjun_11653 import factorization
from random import randint
from prime_util import is_prime

#랜덤으로 소인수분해할 숫자 생성
def random_number():
    return randint(1, 10000000)

def test_factorization():
    test_cases = [random_number() for _ in range(30)]

    for test_case in test_cases:
        my_answer = factorization(test_case)  # factorization 함수 호출하여 소인수분해 결과 저장

        reconstructed_result = 1  # 소인수분해 결과를 다시 계산할 변수 초기화
        for factor, count in my_answer.items():  # 소수인수와 그 개수를 반복
            reconstructed_result *= factor ** count  # 소수인수와 그 개수를 이용하여 결과 계산하기

        # 소인수분해 결과를 다시 계산한 값과 원래 숫자를 비교하여 테스트
        assert reconstructed_result == test_case, f"Wrong answer. my_answer: {my_answer}, answer: {test_case}"

        # 소수가 맞는지 검사
        for factor in my_answer.keys():  # 소수인수만 검사
            assert is_prime(factor), f"{factor} is not a prime number."

        print("test_case:", test_case, "/ my_answer:", my_answer)

if __name__ == "__main__":
    test_factorization()
    print("Everything passed")