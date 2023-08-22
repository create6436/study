from Baekjun_2630 import count_color_paper, main
from new_example import create_example

def test_count_color_paper():
    main(8)
    example = create_example(8, seed=0)
    white_result, blue_result = count_color_paper(example, 8)
    
    # 예제 내의 색상 정보를 이용하여 결과와 비교
    actual_white = sum(row.count(0) for row in example)
    actual_blue = sum(row.count(1) for row in example)

    assert white_result == actual_white, f"Expected white: {white_result}, Actual white: {actual_white}"
    assert blue_result == actual_blue, f"Expected blue: {blue_result}, Actual blue: {actual_blue}"

if __name__ == "__main__":
    test_count_color_paper()
    print("Everything passed")
