# 문자열의 길이를 입력 받으면 랜덤한 문자열을 출력하는 프로그램을 작성
import random

def random_string1(n):
    result = ""
    for _ in range(n):
        rand = chr(random.randint(65, 90))
        result += rand

    return result

def random_string2(n):
    result = ""
    for _ in range(n):
        rand = chr(random.randint(97, 122))
        result += rand

    return result

def random_string3(n):
    result = ""
    for _ in range(n):
        rand = chr(random.randint(48, 57))
        result += rand

    return result

def random_string4(n):
    result = ""
    for _ in range(n):
        rand = random.randint(0, 1)
        if rand == 0:
            # 대문자
            result += chr(random.randint(65, 90))
        else:
            # 소문자
            result += chr(random.randint(97, 122))

    return result

def random_string5(n):
    result = ""
    for _ in range(n):
        # 0 ~ 2
        rand = random.randint(0, 2)
        if rand == 0:
            # 대문자
            result += chr(random.randint(65, 90))
        elif rand == 1:
            # 소문자
            result += chr(random.randint(97, 122))
        else:
            # 숫자
            result += chr(random.randint(48, 57))

    return result

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
    print(random_string1(n))
    print(random_string2(n))
    print(random_string3(n))
    print(random_string4(n))
    print(random_string5(n))
    # print(random_string(n, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=-"))
    print(random_string(n, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=- ") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="]))
    # print(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=-") + ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "y="])