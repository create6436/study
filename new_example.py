import random

def create_example(N, seed=None):
    if seed is not None:
        random.seed(seed)  # 랜덤 시드 설정

    example = [[0] * N for _ in range(N)]  # N x N 크기의 종이 생성

    # 예제를 무작위로 생성
    for i in range(N):
        for j in range(N):
            example[i][j] = random.choice([0, 1])

    return example

if __name__ == "__main__":
    create_example(8)