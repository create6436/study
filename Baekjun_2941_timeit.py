import Baekjun_2941
import Baekjun_2941_test
import timeit

# 함수 실행 횟수
iterations = 1000000

# 변수 = timeit.timeit(stmt, setup, timer, number)
# stmt: 실행할 코드
# setup: import할 코드
# timer: 타이머로 사용할 함수
# number: stmt를 몇 번 실행할지 결정

# exam_time1 = timeit.timeit("Baekjun_2941.count_croatian_alphabet_1('c=c-dz=d-ljnjs=y='*10)", setup="import Baekjun_2941", number=iterations)
# print("count_croatian_alphabet_1:", exam_time1)

exam_time2 = timeit.timeit("Baekjun_2941.count_croatian_alphabet_2('c=c-dz=d-ljnjs=y='*10)", setup="import Baekjun_2941", number=iterations)
print("count_croatian_alphabet_2:", exam_time2)

exam_time3 = timeit.timeit("Baekjun_2941.count_croatian_alphabet_3('c=c-dz=d-ljnjs=y='*10)", setup="import Baekjun_2941", number=iterations)
print("count_croatian_alphabet_3:", exam_time3)

exam_time4 = timeit.timeit("Baekjun_2941.count_croatian_alphabet_4('c=c-dz=d-ljnjs=y='*10)", setup="import Baekjun_2941", number=iterations)
print("count_croatian_alphabet_4:", exam_time4)

