# 주어진 숫자가 소수인지 검사하는 함수
def is_prime(num):
    if num < 2:  # 2보다 작은 숫자는 소수가 아님
        return False

    if num == 2:  # 2는 소수
        return True

    if num % 2 == 0:  # 짝수는 소수가 아님 (2를 제외하고 모든 짝수는 소수가 아님)
        return False

    i = 3
    while i * i <= num:  # i가 num의 제곱근보다 작거나 같을 때까지 반복
        if num % i == 0:  # num이 i로 나누어 떨어지면 소수가 아님
            return False
        i += 2  # 홀수만을 대상으로 반복 검사 (짝수는 위에서 걸러짐)

    return True  # 위의 조건들을 모두 통과하면 소수로 간주


if __name__ == "__main__":
    num = int(input("소수인지 검사할 숫자:"))
    if is_prime(num):
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")