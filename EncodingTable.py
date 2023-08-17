import random
import random_string

def make_encodingTable():
    # 인코딩 테이블의 길이를 랜덤하게 설정
    length = random.randint(9, 10)  # 범위를 수정하여 길이 랜덤 설정
    encoding_table = []

    # 인코딩 테이블에 포함될 문자열을 랜덤하게 생성
    for _ in range(length):
        n = random.randint(2, 3)
        encoding_table.append(random_string.random_string(n, list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=-")))

    # 인코딩 테이블 검사
    return encoding_table

def check_encodingTable(encoding_table):
    for i, first in enumerate(encoding_table):
        for second in encoding_table[i + 1:]:
            if (first in second or second in first) or \
                (first[0] == second[-1] or second[0] == first[-1]):
                return False
    return True

# 인코딩 테이블 생성 및 검사
if __name__ == "__main__":
    encoding_table = make_encodingTable()
    print("encoding_table: ", encoding_table)
