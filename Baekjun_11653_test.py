from Baekjun_11653 import factorization
from random import randint

#랜덤으로 소인수분해할 숫자 생성
def random_number():
    return randint(1, 10000000)

#소인수분해 함수 테스트 코드
def test_factorization():
    test_cases = [random_number() for _ in range(10)]

    for test_case in test_cases:
        my_answer = factorization(test_case)  # factorization 함수 호출하여 소인수분해 결과 저장

        combined_result = 1  # 소인수분해 결과를 합치기 위한 변수 초기화
        for factor in my_answer:
            combined_result *= factor  # 소인수분해 결과를 하나씩 곱하여 합치기

        # 소인수분해 결과를 합친 값과 생성된 숫자를 비교하여 테스트
        assert combined_result == test_case, f"Wrong answer. my_answer: {my_answer}, answer: {test_case}"
        
        print("test_case:", test_case, "/ my_answer:", my_answer)


if __name__ == "__main__": 
    test_factorization()
