def factorization(n):
    factors = []
    i = 2

    while i * i <= n:  # i가 n의 제곱근보다 작거나 같을 때까지 반복
        if n % i == 0:  # n을 i로 나눴을 때 나머지가 0인 경우
            factors.append(i)  # i는 n의 소인수 중 하나
            n //= i  # n을 i로 나눈 몫으로 업데이트
        else:
            i += 1  # i를 1 증가하여 다음 숫자로 넘어감

    if n > 1:  # 남은 n이 1보다 크면, 이것도 소인수 중 하나
        factors.append(n)  # 남은 n을 소인수 리스트에 추가

    return factors

def main():
    N = int(input("소인수분해 할 숫자:"))  # 사용자로부터 숫자 입력 받기
    if N == 1:  # 입력받은 숫자가 1인 경우 소인수분해 결과 없음
        return

    result = factorization(N)
    print(result)

if __name__ == "__main__":
    main()
