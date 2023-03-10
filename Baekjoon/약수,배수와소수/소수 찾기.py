'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
예제 출력 1
3
'''

N = int(input())
num = list(map(int, input().split()))
result = 0
for i in range(len(num)):
    cnt = 0
    for j in range(1, num[i] + 1):
        if num[i] % j == 0:  # 약수 구하기
            cnt += 1
    if cnt == 2:  # 약수가 2개뿐이라면 자신과 1만 약수인것이니 소수 이다.
        result += 1
print(result)
