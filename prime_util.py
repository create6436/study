# 주어진 숫자가 소수인지 검사하는 함수
def is_prime(num):
    if num < 2:  # 2보다 작은 숫자는 소수가 아님
        assert False, f"{num} is not a prime number."

    i = 2
    while i * i <= num:  # i가 num의 제곱근보다 작거나 같을 때까지 반복
        if num % i == 0 or num % (i + 2) == 0:
            assert False, f"{num} is not a prime number."
        i += 1
    return True   # 위의 조건들을 모두 통과하면 소수로 간주

if __name__ == "__main__":
    num = int(input("소수인지 검사할 숫자:"))
    if is_prime(num):
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")