'''
N X N크기의 농장이 있다.
이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.
   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
1 X 1크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.
3 X 3크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16 (3 + 2 + 5 + 4 + 2)이다.
5 X 5크기의 농장에서 자라는 농작물의 수확하여 얻을 수 있는 수익은 25 (3 + 2 + 1 + 1 + 2 + 5 + 1 + 1 + 3 + 3 + 2 + 1)이다.
농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

[제약 사항]
농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)
농작물의 가치는 0~5이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
1
5
14054
44250
02032
51204
52212

출력
#1 23
'''
# 1회차 풀이
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     farm = [list(map(int, input())) for _ in range(N)]
#     arr = [[0] * N for _ in range(N)]   # 마름모 모양을 만들 배열
#     start = (N - 1) // 2    # 시작점
#     end = (N - 1) // 2      # 시작점은 항상 1개라서 start와 같은 값으로 시작
#     x = (N - 1) // 2 + 1    # 열의 범위가 작아지는 지점
#     money = 0   #
#     for i in range(0, x):
#         for j in range(start, end + 1):
#             arr[i][j] = 1
#         start -= 1
#         end += 1
#     for k in range(x, N):
#         start += 1
#         end -= 1
#         for l in range(start + 1, end):
#             arr[k][l] = 1
#
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y] == 1:
#                 money += farm[x][y] # 마름모 모양의 수익을 money에 합산
#
#     print(f'#{tc} {money}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     farm = [list(map(int, input())) for _ in range(N)]
#     start = (N - 1) // 2  # 시작점
#     end = (N - 1) // 2  # 시작점은 항상 1개라서 start와 같은 값으로 시작
#     money = 0
#     for i in range(N):
#         for j in range(start, end + 1):
#             money += farm[i][j]
#         if i >= (N-1)//2:   # 열의 범위가 작아지는 지점
#             start += 1
#             end -= 1
#         else:
#             start -= 1
#             end += 1
#     print(f'#{tc} {money}')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2023 03 02 복습
# range 범위를 잘 활용하자
# 사용할 변수를 잘 생각해서 만들자
from pprint import pprint

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # pprint(farm)
    arr = []
    ge = 0
    st, end = N // 2, N // 2
    for i in range(N):
        if i < N // 2:
            # print(farm[i][st:end + 1])
            arr.append(farm[i][st:end + 1])
            st -= 1
            end += 1
        else:
            # print(farm[i][st:end + 1])
            arr.append(farm[i][st:end + 1])
            st += 1
            end -= 1
    # print(arr)
    for j in arr:
        for k in j:
            ge += k
    print(f'#{tc} {ge}')
