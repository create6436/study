# 문자열의 길이를 입력 받으면 랜덤한 문자열을 출력하는 프로그램을 작성
import random


def random_string(n, candidates):
    result = ""

    if not candidates:
        return ""

    for _ in range(n):
        rand = random.randint(0, len(candidates) - 1)
        result += candidates[rand]

    return result


if __name__ == "__main__":

    n = 100
    print(random_string(n, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]))