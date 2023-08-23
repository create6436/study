from Baekjun_2630 import count_color_paper  # count_color_paper 함수를 가져옵니다.
from new_example import create_example  # create_example 함수를 가져옵니다.

def test_count_color_paper1():
    # 테스트 케이스 1: 예제 입력
    example_input_1 = [
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1]
    ]
    N = len(example_input_1)
    expected_white_result_1 = 9
    expected_blue_result_1 = 7

    # count_color_paper 함수를 호출하여 실제 결과와 비교
    white_result_1, blue_result_1 = count_color_paper(example_input_1, N)
    assert white_result_1 == expected_white_result_1, f"Expected: {expected_white_result_1}, Actual: {white_result_1}"
    assert blue_result_1 == expected_blue_result_1, f"Expected: {expected_blue_result_1}, Actual: {blue_result_1}"

def test_count_color_paper2():
    # 테스트 케이스 2: 무작위 예제
    N = 8
    # create_example 함수를 호출하여 예제 입력 생성
    example_input_2 = create_example(N)
    expected_white_result_2, expected_blue_result_2 = count_color_paper(example_input_2, N)

    # 예제 입력을 반전시킴
    example_input_2_swapped = [[1 - cell for cell in row] for row in example_input_2]

    # count_color_paper 함수를 호출하여
    # 예제를 입력한 결과와 반전시킨 예제를 입력한 결과에서
    # 하얀색과 파란색 색종이 개수가 서로 바뀌는지 확인
    white_result_2, blue_result_2 = count_color_paper(example_input_2_swapped, N)

    print("Expected: ", expected_white_result_2, expected_blue_result_2)
    print("Actual: ", white_result_2, blue_result_2)

    assert white_result_2 == expected_blue_result_2, f"Expected: {expected_blue_result_2}, Actual: {white_result_2}"
    assert blue_result_2 == expected_white_result_2, f"Expected: {expected_white_result_2}, Actual: {blue_result_2}"

if __name__ == "__main__":
    test_count_color_paper1()
    test_count_color_paper2()
    print("Everything passed")
