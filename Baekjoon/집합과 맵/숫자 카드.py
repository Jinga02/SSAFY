'''
숫자 카드

문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

예제 입력 1
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
예제 출력 1
1 0 0 1 1 0 0 1
'''
import sys

input = sys.stdin.readline

N = int(input())
Nnum = set(map(int, input().split()))  # 상근이가 가지고 있는 카드

M = int(input())
Mnum = list(map(int, input().split()))  # 확인 할 카드

# result = dict()  # 가지고 있는지 아닌지 1과 0으로 구분하기 위한 딕셔너리

for i in Mnum:
    if i in Nnum:  # 가지고 있으면 1
        print(1, end=' ')
    else:  # 가지고 있지 않으면 0
        print(0, end=' ')

###처음에는 Nnum도 list로 받았는데 시간초과로 인해 실패했다.
set은 list와 다르게 인덱스가 없다.
그렇기때문에 if문을 통해 비교를 할때도 한번에 비교를 하기 때문에 list보다 빠르다.
혹시 제가 잘못 알고 있다면 알려주시면 감사하겠습니다.

### 느낀 점
자료형의 정의와 특징에 대해 정확히 알아야 하는데 대충 공부하고 문제를 풀어 이런 실수를 한 것 같다.
지금도 모자란 실력이니 문제를 많이 푸는것에 급급하지 않고 기초를 더욱 단단하게 해야겠다.