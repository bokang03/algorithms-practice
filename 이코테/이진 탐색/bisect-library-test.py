from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(left_index)
    print(right_index)
    return right_index - left_index  # 총 개수


if __name__ == '__main__':
    # a = [1,2,4,4,8]
    # x = 4
    #
    # print(bisect_left(a, x)) # 정렬된 순서를 유지하며 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환 : 2
    # print(bisect_right(a, x)) # 정렬된 순서를 유지하며 배열 a에 x를 삽일할 가장 오른쪽 인덱스 반환 : 4

    a = [1,2,3,3,3,3,4,4,8,9]
    print(count_by_range(a, 4, 4))
    print("------------------------------")
    print(count_by_range(a, -1, 3)) # [-1, 3] 범위에 있는 데이터 개수 출력

