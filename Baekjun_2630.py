from new_example import create_example

def count_color_paper(paper, N):
    white_count = 0  # 하얀색 색종이 개수를 세기 위한 변수
    blue_count = 0   # 파란색 색종이 개수를 세기 위한 변수
    
    # Base case: 종이가 한 가지 색으로 칠해져 있으면 개수를 증가시킴
    if all(all(x == paper[0][0] for x in row) for row in paper):
        if paper[0][0] == 0:
            white_count += 1  # 하얀색이면 하얀색 색종이 개수 증가
        else:
            blue_count += 1   # 파란색이면 파란색 색종이 개수 증가
    else:
    # 종이를 네 개의 사각형으로 분할
        half = N // 2
        upper_left = [row[:half] for row in paper[:half]]  # 왼쪽 위 사분면
        upper_right = [row[half:] for row in paper[:half]]  # 오른쪽 위 사분면
        lower_left = [row[:half] for row in paper[half:]]  # 왼쪽 아래 사분면
        lower_right = [row[half:] for row in paper[half:]]  # 오른쪽 아래 사분면
    
    # 각 사분면에 대해 재귀적으로 하얀색과 파란색 색종이 개수 계산
        white_upper_left, blue_upper_left = count_color_paper(upper_left, half)
        white_count += white_upper_left
        blue_count += blue_upper_left
    
        white_upper_right, blue_upper_right = count_color_paper(upper_right, half)
        white_count += white_upper_right
        blue_count += blue_upper_right
    
        white_lower_left, blue_lower_left = count_color_paper(lower_left, half)
        white_count += white_lower_left
        blue_count += blue_lower_left
    
        white_lower_right, blue_lower_right = count_color_paper(lower_right, half)
        white_count += white_lower_right
        blue_count += blue_lower_right
    
    return white_count, blue_count

if __name__ == "__main__":
    # 전체 종이의 한 변 길이
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]  # 종이의 각 행에 색 정보 저장

    # 하얀색과 파란색 색종이 개수 계산
    white_result, blue_result = count_color_paper(paper, N)

    # 결과 출력
    print(white_result)
    print(blue_result)
