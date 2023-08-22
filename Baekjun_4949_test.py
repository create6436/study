from Baekjun_4949 import is_balanced

def test_is_balanced():
    # 균형이 맞는 경우
    assert is_balanced("()") == True
    assert is_balanced("[]") == True
    assert is_balanced("({[]})") == True
    assert is_balanced("[{()}]") == True
    assert is_balanced("(([]))") == True

    # 균형이 깨진 경우
    assert is_balanced("(") == False
    assert is_balanced(")") == False
    assert is_balanced("[") == False
    assert is_balanced("]") == False
    assert is_balanced("{") == False
    assert is_balanced("}") == False
    assert is_balanced("({)}") == False
    assert is_balanced("([)]") == False
    assert is_balanced("[{]}") == False
    assert is_balanced("()(") == False
    assert is_balanced(")(") == False
    assert is_balanced("[[[]]]]") == False
    assert is_balanced("[[[[[[[]]]]") == False

if __name__ == "__main__":
    test_is_balanced()
    print("Everything passed")