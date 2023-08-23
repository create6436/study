import random
import timeit

# sort algorithm 예제 모음
arr = [random.randint(0, 100) for _ in range(10)]
print("정렬 전 배열:", arr)

# 1. 버블 소트
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 배열의 마지막 요소는 이미 정렬됨. 각 반복에서 가장 큰 요소가 뒤로 이동하므로 범위를 줄여감
        for j in range(0, n - i - 1):
            # 현재 원소(arr[j])와 다음 원소(arr[j + 1])를 비교하여 정렬
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(arr)
print("버블 소트 후 배열:", arr)


# 2. 선택 소트
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # 아직 정렬되지 않은 부분에서 최소값을 탐색
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 최소값의 인덱스를 업데이트
        # 최소값을 정렬된 부분의 맨 앞으로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort(arr)
print("선택 소트 후 배열:", arr)


# 3. 삽입 소트
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 현재 비교 대상인 원소
        j = i - 1
        # key와 비교하여 삽입 위치를 찾아가면서 정렬된 부분을 뒤로 이동
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 적절한 위치에 key를 삽입

insertion_sort(arr)
print("삽입 소트 후 배열:", arr)


# 4. 병합 소트
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # 왼쪽 반을 재귀적으로 정렬
        merge_sort(right_half)  # 오른쪽 반을 재귀적으로 정렬

        i = j = k = 0
        # 두 개의 반을 합병하면서 정렬
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 요소들을 배열에 추가
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sort(arr)
print("병합 소트 후 배열:", arr)


# 5. 퀵 소트
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 피벗을 배열의 중간 값으로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 값들
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 값들
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 값들
    return quick_sort(left) + middle + quick_sort(right)  # 작은 값, 피벗, 큰 값 순서로 재귀적으로 정렬

sorted_arr = quick_sort(arr)
print("퀵 소트 후 배열:", sorted_arr)


# 6. 힙 소트
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 부모 노드(i)와 자식 노드(left, right) 중에서 가장 큰 값을 찾음
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # 자식 노드와 교환 후 재귀적으로 heapify

def heap_sort(arr):
    n = len(arr)
    # 힙 구조 생성: 마지막 노드의 부모부터 시작하여 heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 최대값을 뽑아내면서 배열을 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최대값(루트)을 배열의 맨 뒤로 이동
        heapify(arr, i, 0)

heap_sort(arr)
print("힙 소트 후 배열:", arr)


# 7. 기수 소트
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # exp(10의 거듭제곱)을 사용하여 각 자리의 값을 카운팅
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # 누적 카운트 배열 생성
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 배열을 역순으로 순회하며 output 배열에 정렬하여 저장
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # output 배열의 값을 arr로 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)  # 각 자리 수를 기준으로 정렬
        exp *= 10

radix_sort(arr)
print("기수 소트 후 배열:", arr)

# 함수 실행 횟수
iterations = 1000000

# 변수 = timeit.timeit(stmt, setup, timer, number)
# stmt: 실행할 코드
# setup: import할 코드
# timer: 타이머로 사용할 함수
# number: stmt를 몇 번 실행할지 결정

# 버블 소트
bubble_sort_time = timeit.timeit("bubble_sort(arr)", setup="from __main__ import bubble_sort, arr", number=iterations)
print("버블 소트 실행 시간:", bubble_sort_time)

# 선택 소트
selection_sort_time = timeit.timeit("selection_sort(arr)", setup="from __main__ import selection_sort, arr", number=iterations)
print("선택 소트 실행 시간:", selection_sort_time)

# 삽입 소트
insertion_sort_time = timeit.timeit("insertion_sort(arr)", setup="from __main__ import insertion_sort, arr", number=iterations)
print("삽입 소트 실행 시간:", insertion_sort_time)

# 병합 소트
merge_sort_time = timeit.timeit("merge_sort(arr)", setup="from __main__ import merge_sort, arr", number=iterations)
print("병합 소트 실행 시간:", merge_sort_time)

# 퀵 소트
quick_sort_time = timeit.timeit("quick_sort(arr)", setup="from __main__ import quick_sort, arr", number=iterations)
print("퀵 소트 실행 시간:", quick_sort_time)

# 힙 소트
heap_sort_time = timeit.timeit("heap_sort(arr)", setup="from __main__ import heap_sort, arr", number=iterations)
print("힙 소트 실행 시간:", heap_sort_time)

# 기수 소트
radix_sort_time = timeit.timeit("radix_sort(arr)", setup="from __main__ import radix_sort, arr", number=iterations)
print("기수 소트 실행 시간:", radix_sort_time)
