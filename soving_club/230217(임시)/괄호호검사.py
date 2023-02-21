'''
        N, M = map(int, input().split())

(1)스택을 이용해 괄호가 정상적으로 표시되어 있는지 검사하는 알고리즘에 대해 간단히 설명하라.
    스택은 LIFO 구조를 가진다. 제일 마지막에 push된 데이터가 가장 먼저 pop된다는 뜻이다.
    이러한 스택을 이용해 괄호가 정상적으로 표시되어 있는지 검사하는 알고리즘의 원리는 다음과 같다.
    먼저 '(' 를 만나면 push 하고 ')' 를 만나면 pop을 한다.
    만약 괄호 쌍이 맞지 않는다면 즉시 break한다. 괄호 쌍이 맞지 않는다는것은 정상적이지 않기때문이다.
    괄호는 여는괄호와 닫는괄호가 항상 짝을 이루어야하기때문에 마지막에 push된 데이터가 가장 먼저 pop되는
    스택의 특징을 이용해 괄호가 정상적으로 표시되어 있는지 검사 할 수 있는 것이다.
    '''

'''
(2)위의 문자열을 스택을 이용해 검사하는 과정에 대해, 나머지 단계의 스택 내부 상태를 표시하고 간단히 설명하라. 마지막에는 괄호가 정상인지 오류인지와 그 이유를 설명해야 한다.
    스택은 [  ]로 표시하고, 저장 원소의 구분은 쉼표나 빈 칸으로 표시한다.
'''
'''
[ ( ]    # 여는 괄호를 만나 push
[ ( , ( ]    # 여는 괄호를 만나 push
[ ( ]    # 닫는 괄호를 만나 pop
입력
N, M = map(int, input().split())
arr = list(map(int, input().split())
sample_input.txt
출력
['('] # 여는 괄호를 만나 push
['(', '('] # 여는 괄호를 만나 push
['('] # 닫는 괄호를 만나 pop
['(', '('] # 여는 괄호를 만나 push
['('] # 닫는 괄호를 만나 pop
[] # 닫는 괄호를 만나 pop
스택에 ~ 괄호 쌍이 정상이다. #검사 성공

['('] # 여는 괄호를 만나 push
['(', '('] # 여는 괄호를 만나 push
['(', '(', '('] # 여는 괄호를 만나 push
['(', '('] # 닫는 괄호를 만나 pop
['(', '(', '('] # 여는 괄호를 만나 push
['(', '('] # 닫는 괄호를 만나 pop
['('] # 닫는 괄호를 만나 pop
스택에 ~ 괄호의 쌍이 올바르지 않음 # 검사 실패
'''


