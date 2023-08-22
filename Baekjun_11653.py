from prime_util import is_prime

# 소인수분해 함수
def factorization(n):
    factors = {}  # 결과를 저장할 딕셔너리

    i = 2
    while i * i <= n:  # i가 n의 제곱근보다 작거나 같을 때까지 반복
        if n % i == 0:  # n을 i로 나눴을 때 나머지가 0인 경우 (즉, i가 n의 소인수인 경우)
            if i not in factors:
                factors[i] = 1  # i를 소인수로 추가하고 개수를 1로 초기화
            else:
                factors[i] += 1  # 이미 소인수로 추가된 i라면 개수를 1 증가
            n //= i  # n을 i로 나눈 몫으로 업데이트하여 작은 숫자로 계속 진행
        else:
            i += 1  # i가 n의 소인수가 아니라면 i를 1 증가하여 다음 숫자로 넘어감

    if n > 1:  # 남은 n이 1보다 크면, 이것도 소인수 중 하나 (n은 자신의 제곱근보다 큰 소인수를 가짐)
        if n not in factors:
            factors[n] = 1  # 남은 n을 소인수로 추가하고 개수를 1로 초기화
        else:
            factors[n] += 1  # 이미 소인수로 추가된 n이라면 개수를 1 증가
       
        # 남은 n이 소수인지 검사
        if not is_prime(n):
            assert False, f"{n} is not a prime number."

    return factors

def main():
    N = int(input("소인수분해 할 숫자:"))  # 사용자로부터 숫자 입력 받기
    if N == 1:  # 입력받은 숫자가 1인 경우 소인수분해 결과 없음
        return

    result = factorization(N)
    print(result)

if __name__ == "__main__":
    main()
