'''
삼성시는 버스 노선을 일반, 급행, 광역 급행으로 구분해 새롭게 바꾸려고 한다. 모든 정류장은 1번부터 1000번까지의 번호가 부여되어 있으며, 각 노선은 A에서 B번 정류장까지 다음 규칙에 따라 운행한다.
- 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B정류장에는 반드시 정차한다.
- 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.
- 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 짝수 번호 정류장에 정차하고, A가 홀수인 경우 A와 B사이의 모든 홀수 번호 정류장에 정차한다.
- 광역 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에, A가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차한다.
버스의 종류와 출발 도착 정류장에 대한 정보가 주어질 때, 최대 몇 개의 노선이 같은 정류장에 정차하는지 알아내는 프로그램을 만들어보자.

[입력]
첫 줄에 테스트케이스의 개수 T가 주어진다. (1<=T<=1000)
다음 줄부터 각 테스트케이스 별로 첫 줄에 노선의 수 N이 주어지고(1<=N<=100), N개의 줄에 걸쳐 버스 타입 (1 일반, 2 급행, 3 광역 급행)과 출발 정류장 번호 A, 종점인 정류장 번호 B가 빈칸으로 구분되어 주어진다. (1<=A
1
3
1 2 5
2 3 10
3 2 9

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
#1 2
'''
# T = int(input())
# for i in range(1, T + 1):
#     N = int(input())
#     bus_list = [0] * 1001
#     for a in range(1, N + 1):
#         bus, sn1, en1 = map(int, input().split())
#         if bus == 1:
#             for j in range(sn1, en1 + 1):
#                 bus_list[j] += 1
#         elif bus == 2:
#             for k in range(sn1, en1 + 1):
#                 if sn1 % 2 == 0 and k % 2 == 0:
#                     bus_list[k] += 1
#                 elif sn1 % 2 == 1 and k % 2 == 1:
#                     bus_list[k] += 1
#         elif bus == 3:
#             for l in range(sn1, en1 + 1):
#                 if sn1 % 2 == 0 and l % 4 == 0 and l % 10 != 0:
#                     bus_list[l] += 1
#                 elif sn1 % 2 == 1 and l % 3 == 0 and l % 10 != 0:
#                     bus_list[l] += 1
#     print(f'#{i} {max(bus_list)}')

# ----------------------------------------------------------------- #
# 2023 - 02 - 24 복습

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bs = [0] * 1001
    for i in range(N):
        bn, sta, end = map(int, input().split())
        if bn == 1:
            for j in range(sta, end + 1):
                bs[j] += 1
        elif bn == 2:
            for k in range(sta, end + 1):
                if sta % 2 == 0 and k % 2 == 0:
                    bs[k] += 1
                elif sta % 2 != 0 and k % 2 != 0:
                    bs[k] += 1
        elif bn == 3:
            for l in range(sta, end + 1):
                if sta % 2 == 0 and l % 4 == 0 and l % 10 != 0:
                    bs[l] += 1
                elif sta % 2 != 0 and l % 3 == 0 and l % 10 != 0:
                    bs[l] += 1
    # print(bs)
    print(f'#{tc} {max(bs)}')
