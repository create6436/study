def is_balanced(expression):
    stack = []  # 괄호를 저장할 스택을 초기화합니다.
    mapping = {')': '(', ']': '[', '}': '{'}  # 괄호 짝을 나타내는 매핑 딕셔너리입니다.

    for char in expression:
        if char in '([{':
            stack.append(char)  # 열린 괄호면 스택에 추가합니다.
        elif char in ')]}':
            if not stack or stack[-1] != mapping[char]:
                return False  # 닫힌 괄호인데 스택이 비어있거나 매칭되는 열린 괄호가 아니라면 균형이 깨진 것입니다.
            stack.pop()  # 괄호 짝이 맞는 경우 스택에서 열린 괄호를 제거합니다.

    return not stack  # 모든 괄호를 확인한 후 스택이 비어있다면 균형이 잘 맞춰진 것입니다.


def main():
    while True:
        input_str = input()  # 문자열을 입력받습니다.
        if input_str == '.':
            break  # 입력이 '.'이면 프로그램을 종료합니다.

        result = is_balanced(input_str)  # 입력된 문자열의 균형을 확인합니다.
        if result:
            print("yes")  # 균형이 맞다면 "yes"를 출력합니다.
        else:
            print("no")  # 균형이 깨졌다면 "no"를 출력합니다.

if __name__ == "__main__":
    main()