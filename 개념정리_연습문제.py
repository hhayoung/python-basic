# *** 함수, 객체지향프로그래밍, 파일입출력, 모듈과 패키지 개념  정리 및 연습문제 ***

# 1. print(), sum(), range()와 같은 함수를 무슨 함수라고 하나요.
내장함수
내장(built-in) 함수  <->  사용자 정의(custom) 함수

# 2. 함수를 정의하는 키워드를 쓰세요.
def

# 3. 주어진 input에 대해 의도된 output을 전달하는 역할을 하는 것을 프로그래밍에서는 무엇이라고 하나요?
함수
: 반복되는 기능을 묶어서 정의해놓는 것. 개발자들이 편하게 사용하려고

# 4. 리스트, 튜플과 같은 원소의 개수를 output하는 함수명을 적으세요.
len()

# 5. 함수에 전달되는 입력을 무엇이라고 하는지 아는대로 적으세요.
매개변수, 인수, 인자, 파라미터
argument, parameter

# 6. 매개변수를 지정하지 않을 경우, 지정된 기본값으로 대체되는데 이러한 인자를 무엇이라고 하나요?
defalut Parameter(기본 인자) 

# 7. 위의 문제에 해당하는 내장 함수의 예를 들어보세요.
print()
기본으로 sep=' ', end='\n', file=sys.stdout, flush=False


# 8. 함수의 종료를 명시하는 키워드는 무엇인가요?
return

# 9. 위 문제의 키워드가 생략된 경우 반환값은 무엇인지 적으세요
None

# 10. 함수의 반환값은 어디로 리턴되나요?
함수를 호출한 곳
함수 호출자(caller)

# 11. 다음 중 틀린 표현은 몇 번째 인가요?
#   def test(a, b, c = 1)
  def test(a, b = 1, c)
#   def test(a = 1, b = 1, c = 3)
두번째. 디폴트 인자 뒤로 일반 인자 올 수 없음.
항상 기본 인자는 맨 뒤로 와야한다. 

# 12. 키워드 파라미터를 관례적으로 어떻게 표현하는지 직접 함수의 선언부를 작성해보세요
# (인수의 갯수는 고정되지 않음, 함수명은 임의로 정하세요)
def func(**kwargs):
고정되지 않은 매개변수.
**kwarges = 딕셔너리 형태로 들어감
*args = 튜플 형태로 하나씩 들어감

# 13. 특정 코드 블록(함수 안)에서 선언된 변수를 무엇이라고 하나요?
지역변수(Local Variable)

# 14. 프로그램 종료 전까지 유지되는 변수를 무슨 변수라고 하나요?
전역변수(Global Variable)

# 15. 위와 같은 변수의 범위를 영어로 무엇이라고 하나요?
Variable scope

# 16. 14번, 15번 답 중 우선순위가 높은 것(먼저 적용되는 것)은?
지역변수(Local Variable)

# 17. 파라미터를 튜플 형태로 전달하는 함수의 선언부를 작성해보세요. (인자의 갯수가 고정되지 않음, 함수명은 임의로..)
def return_tuple(*args):
    tup = ()
    for i in args:
        tup += (i,)
    return tup

# 18. 두개의 입력을 받아 합, 차, 곱의 결과를 튜플로 동시에 반환하는 함수를 정의 하고 실행해보세요.
def Cal(a,b):
    plus = a+b
    minus = a-b
    mul = a*b
    return (plus, minus, mul)

print(Cal(2,3))


# 19. 다음과 같은 함수를 정의하고 실행해보세요.(조건문을 이용)
'''
    함수명 : return_fruit
    입력 : color
    기능 : 
           color가 red 이면 apple을 반환
           color가 yellow 이면 banana를 반환
           color가 green 이면 water melon을 반환
           위의 color가 아니면 I don't know를 반환    
'''
def return_fruit(color):
    if color=='red':
        return 'apple'
    elif color=='yellow':
        return 'banana'
    elif color=='green':
        return 'water melon'
    else:
        return "I don't know"

print(return_fruit('red'))


# 20. 위의 문제를 아래 예시된 딕셔너리를 이용하여 함수를 정의하세요.
'''
fruit_dic = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'water melon'
}
'''
def return_fruit(dic,select):
    if select == 'red':
        return dic['red']
    elif select == 'yellow':
        return dic['yellow']
    elif select == 'green':
        return dic['green']
    else:
        return "I don't know"

print(return_fruit(fruit_dic,'red'))

# 정답
fruit_dic = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'water melon'
}
def return_fruit(color):
    return fruit_dic.get(color, "I don't know")
res = return_fruit('red')
print(res)

딕셔너리 get() 함수를 쓰면 안전하게 값을 가져올 수 있다.
get(key, default)를 넣었을 때 value값을 가져오는 함수.
해당 키값이 없을 때 나오는 값

# 21. 입력 값 보다 작은 Fibonacci 수열을 출력하는 함수를 작성하세요
# 함수명 : fibonacci
# 피보나치 수열 : 0번째 원소를 0, 1번째 원소를 1로 두고 시작하여, 다음 2번째 원소는 앞의 두수의 합 1(0+1)을 놓고,
#                3번째 원소는 앞의 두수의 합 2(1 + (0+1))을, 4번째 원소는 역시 앞의 두수의 합 3(1 + 2)을 배치하는 방식으로
#                나열되는 수열을 말한다.
#              e.g) 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

def fibonacci(num):
    a, b = 0, 1
    i = 0
    print(a,b,end=' ')
    while i<num:
        a, b = b, a+b
        print(b,end=' ')
        i += 1
        
# print(fibonacci(10)) - None이 반환되어버림.
fibonacci(10)


# 22. 위의 문제에서 수열을 리스트에 출력하도록 함수를 수정하세요.
리스트에 값을 넣어두고 실습을 하는데 그렇게 안하고, 리스트에 하나씩 넣어서 실습하는거에 익숙해져야한다.
def fibonacci(num):
    a, b = 0, 1
    _list = [a,b]
    i = 0
    while i<num:
        a, b = b, a+b
        _list.append(b)
        i += 1
    return _list

print(fibonacci(10))

# 23. 인자의 갯수가 하나 또는 두개만 허용된다고 가정하고, 하나인 경우는 제곱을 두개인 경우에는 두수의 곱을 반환하는 
#     함수를 정의해보세요. 함수명(var_arg)
def var_arg(*args):
    if len(args)==1:
        return args[0] ** 2
    else:
        return args[0] * args[1]

print(var_arg(5))
print(var_arg(5,2))


# 24. a, b 두수 중 큰 값을 출력하는 코드를 삼항연산자(조건부 표현식)를 이용하여 작성하세요.
a = 10
b = 5

print('a가 더 큰 수' if a>b else 'b가 더 큰 수')
print('a :', a) if a > b else print('b :', b)

# 25. 23번 문제를 default parameter와 파이썬 삼항 연산자(조건부 표현식)를 이용하여 함수를 정의하세요.
# 함수명 : default_arg

??????????????????????
def default_arg(x,y=None):
    return x * (y if y else x)

print(default_arg(10))
print(default_arg(10,2))

# 26. 모듈(또는 객체) 안에 어떤 함수나 변수가 있는지 이름들을 확인하는 내장 함수는 무엇인지 쓰세요.
# dir()
dir()

# 27. m_test 모듈안에 두수의 합을 리턴하는 함수(add)와, name 변수를 선언하는 모듈을 만든 후,
#     26번 답(내장함수)을 이용하여 m_Test모듈안의 이름들을 출력하는 코드를 작성하여 실행하세요.
'''
# m_test.py

def add(x, y):
    n = x + y
    return n

name = '홍길동'  

'''

import m_test
print(dir(m_test))


# 28. 위에서 만든 모듈을 mt라는 별칭을 이용하여 add함수를 호출하여 결과값을 출력하는 코드를 작성하세요.
import m_test as mt
result = mt.add(5,3)
print(result)

# 29. 람다함수의 키워드를 쓰세요.
lambda

# 30. 람다함수와 일반함수의 차이점에 대해서 간략히 정리해보세요.
일반함수는 선언을 하자마자 메모리에 올라가서 공간을 차지하는데,
람다함수는 메모리의 공간을 차지하지 않는다. 
간단하게 한 번 쓰고 말 함수라면 람다함수를 사용하는 게 효율적이다.

# 정답
일회성(코드상에서 한 번만 사용할 때), 익명성(lambda는 함수 이름이 없다.)

# 31. 람다 함수가 유용하게 사용되는 3개의 함수를 적으세요.
filter(): 특정 조건을 만족하는 요소만 남겨두고 필터링
map(): 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트를 반환하는 함수
reduce(): 차례대로 앞 2개의 원소를 가지고 연산 후 그 연산의 결과가 또 다음 연산의 입력으로 진행됨.
          따라서, 마지막까지 진행되면 최종 출력은 한 개의 값만 남는다.

# 32. 주어진 리스트에서 5(포함) ~ 10(포함)사이의 값을 출력하는 코드를 작성하는데
#     위의 문제 3개의 함수 중 하나를 이용하여 작성하세요.
nums = [1,2,3,6,8,9, 10, 11, 13, 15]

def ft(n):
    if n>=5 and n<=10:
        return n
    
list(filter(ft, nums))
print(list(filter(lambda n : n>=5 and n<=10,nums)))
뒤에 리스트에서 조건에 만족하는 것만 출력. 

# 33. 31번 문제 3개의 함수 중 하나를 이용하여 다음과 같이 369 게임에 맞게 코드를 작성하세요.
# [1, 2, '박수', 4, 5, '박수', 7, 8, '박수'] (1 ~ 10범위)
nums = [1,2,3,4,5,6,7,8,9,10]

def tsn(n):
    if n%3==0:
        return '박수'
    else:
        return n

print(list(map(tsn,nums)))

print(list(map(lambda x:'박수' if x%3==0 else x, range(1,10))))

# 34. 위의 문제에서 범위를 1 ~ 20까지 했을 때 코드를 작성하세요. (find함수 사용)
# [1, 2, '박수', 4, 5, '박수', 7, 8, '박수', 10, 11, 12, '박수', 14, 15, '박수', 17, 18, '박수'] (1 ~ 20범위)
# find() : 문자열에서 해당 문자의 index를 반환, 만일 없으면 -1을 반환 
# e.g> 'abcde'.find('b') 실행 후 확인해보세요.

def tsn(n):
    n = str(n)
    if n.find('3')==0 or n.find('3')==1:
        return '박수'
    elif n.find('6')==0 or n.find('6')==1:
        return '박수'
    elif n.find('9')==0 or n.find('9')==1:
        return '박수'
    else:
        return int(n)

print(list(map(tsn,range(1,20))))
print(list(map(lambda x:'박수' if str(x).find('3')>=0 or str(x).find('6')>=0 or str(x).find('9')>=0 else x, range(1,20))))

# 35. 리스트 컴프리핸션과 람다 함수를 이용하여 구구단을 가로로 출력하는 리스트를 만들어 보세요
# e.g> ['2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', ... ]

리스트 내포 => [ 표현식 for(바깥for문) ~ for(안쪽for문) ~]

함수명(인자)
lambda함수(인자)
lambda함수는 이름이 없으니까 그냥 lambda를 쓰고 뒤에 인자 넣어준 느낌

람다 함수 => lambda 매개변수 : return 값

print([(lambda x,y: f'{x}x{y}={x*y}')(x,y) for x in range(2,10) for y in range(1,10)])

# 36. 리스트 컴프리핸션과 람다 함수를 이용하여 구구단을 가로로 출력하는 리스트를 만들어 보세요
# e.g> ['2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6', ... ]


# 38. 단위 테스트용으로 사용되는 구문을 적으세요.
# if __name__ == '__main__':
통합 테스트를 해야하는데 일일히 하나씩 해 볼수 없기 때문에
시간이 너무 오래 걸리기 때문에
각각 모듈별로 각각 단위별로 다 해놓으면 전체적인 통합테스트 할 때 더 편하다.

# 39. 다음 예시대로 실행 후 결과를 출력하고 __name__ 내장변수에 대해 생각해보세요.
'''
# greet.py 

def greeting():
    print('hello!!')

print('greet의 __name__ :', __name__)
----------------------

# greet.py를 import 하여 다음과 같이 실행한 후 결과를 확인하세요.

import greet

print('현재 모듈의 __name__ :', __name__)
greet.greeting()

'''
출력결과:
greet의 __name__: greet
현재 모듈의 __name__: __main__
hello!! 

# 40. 다음 예시와 같이 학생의 수를 입력받아 학생의 점수와 평균, 평균과의 차이를 구하여 출력하는
# 프로그램을 구현하세요. (함수를 이용하여 구현하세요) 

# 참고 사항 : 전체적인 구현을 먼저 한 후 부분 부분 함수를 정의해보세요.

# 학생 수를 입력받는다.
# 학생의 점수는 리스트에 append() 함수를 이용하여 학생수 만큼 루프를 돌려 추가시킨다.
# 리스트의 평균을 구한다.
# 평균미만자 수 : 구한 평균 미만의 점수를 카운트 한다.(루프 활용)
# 반복문을 활용하여 출력한다.

''' [ 프로그램 실행 화면 ]

학생 수를 입력하세요 : 4

1번 학생의 점수 : 88
2번 학생의 점수 : 79
3번 학생의 점수 : 85
4번 학생의 점수 : 78
------------------------------
 번호 	 점수 	 평균과의 차이
------------------------------

   1 	  88 	 5.50

   2 	  79 	 -3.50

   3 	  85 	 2.50

   4 	  78 	 -4.50
------------------------------
전체 평균 :  82.5
------------------------------
평균 미만자 수 :  2
------------------------------
'''

????????????????? 했는데 함수로 나누면 됨.

# 41. 파일 입출력 시 자주 사용되는 3가지 모드를 쓰세요.
# 참고 사이트 : https://docs.python.org/3.7/library/functions.html#open 
'r'ead : 읽기 모드
'w'rite : 쓰기 모드
'a'ppend : 추가 모드


# 42. 파일을 모드별로 읽어올 때 사용하는 함수를 쓰세요.
open() 함수


# 43. 파일의 전체 내용을 읽을 때 사용하는 함수를 쓰세요.
read() 함수


# 44. 파일의 내용을 한 줄씩 읽을 때 사용하는 함수를 쓰세요.
readline() 함수


# 45. 파일을 모드별로 연 후 리소스(메모리)를 반환 하기 위해 반드시 사용하는 함수를 적으세요.
close()
리소스(자원) : 컴퓨터 자원 - CPU, RAM, 하드디스크, 이런 것들을 잡고 있으면 안 됨.
리소스는 한정되어 있다.

# 46. 리소스 반환을 자동으로 해주는 구문을 적으세요.
with open('주소써주고','모드') as f:


# 47. 파일에 내용을 쓸 때 사용하는 모드를 아는대로 적으세요.
a랑 w


# 48. 파일을 열 때 한글이 깨지는 현상을 막기 위해 사용하는 파라미터를 적으세요.
encoding = 'utf-8'


# 49. 파일 내용을 읽어올 때 앞뒤 공백을 없애주는 함수를 적으세요.
strip() 함수


# 50. 다음 예시대로 프로그램을 구현 해보세요.
'''
다음과 같이 score.txt를 만든다.(resource 폴더 안에)
# score.txt

90
80
78
88
67

위 파일의 점수를 리스트에 추가한다.
평균을 구한다.

출력
[ 90, 80, 78, 88, 67 ]
 
Average : **.***
'''

with open('./resource/score.txt','r') as f:
    score_list = []
    for line in f:
        score_list.append(int(line.strip()))
    print(score_list)
    score_avg = sum(score_list) / len(score_list)
    print('Average : ',score_avg)

# 51. 로또 번호를 랜덤하게 생성하여 파일에 저장하는 코드를 작성하여 실행하세요.

import random as r

with open('./resource/lotto.txt','a') as f:
    for i in range(6):
        f.write(str(r.randint(1,45)))
        f.write(' ')
    f.write('\n')

# 52. 객체지향 프로그래밍을 영문3글자로 표현하세요.
OOP(Object Oriented Programming)


# 53. 객체지향언어에서 '설계도'에 비유되는 것을 무엇이라고 하나요?
클래스


# 54. 객체지향 언어의 특징 중 오버라이딩과 관련 있는 것을 아는대로 쓰세요.
다형성, 상속성


# 55. 객체지향 프로그래밍의 4가지 핵심 특징 중 다음 문구와 관계있는 것은?
# " 복잡한 것은 과감히 버리고, 필요한 것만 표현 하는 것"
추상화(다른 말로 모델링한다.)

# 캡슐화: 시스템에서 중요한 것이 날짜이다. 한번만 날짜가 바뀌면 난리가 나고 어마어마한 피해가 나는데
# 이 날짜에 아무나 접근해서 값을 바꿔버리면 안되기 때문에 접근을 못하게 캡슐화한다.
# 접근을 메소드로만 할 수 있게 하는 것.

# 56. 클래스를 정의하는 키워드는?
class


# 57. 클래스의 멤버(구성)를 아는대로 적으세요.
attribute(속성), method(함수)

# 정답
생성자, 소멸자, 메소드, 속성


# 58. attribute와 behavior를 뽑아내는 과정을 무엇이라고 하나요?

?????????????????
추상화, 객체 모델링

# 59. 오버라이드(Override)를 간단하게 표현해보세요
상속을 했을 때, 부모 클래스에 있는 함수를 자식 클래스에서 재정의 할 때 오버라이딩이라고 한다.
재정의

# 60. 클래스를 통해 만들어지는 객체를 다른 용어로 무엇이라고 하나요?
인스턴스(instance)

''' 문제 : 61 ~ 71 [ 예시 코드 ]
class Person:
    name = '아무개'

    def __init__(self, name):
        self.name = name    

    def _info(self):
        print('인스턴스 변수 : ', A)

    def info():
        print('클래스 변수 :', B)   
'''

# 61. 위의 예시 코드에서 인스턴스 변수와 클래스 변수를 구분해보세요.
클래스 변수 = name
인스턴스 변수 = self.name

# 62. 위의 예시 코드에서 인스턴스 메소드와 클래스 메소드를 구분해보세요.
인스턴스 메소드 = __init__() , _info()
클래스 메소드 = info()

# 63. 위의 예시 코드에서 인스턴스 변수에 접근하는 코드를 작성하세요.
p = Person('홍길동')
p.name

# 64. 위의 예시 코드에서 클래스 변수에 접근하는 코드를 작성하세요.
Person.name


# 65. 위의 예시 코드에서 A, B에 알맞는 코드를 작성하세요.
def _info(self):
        print('인스턴스 변수 : ', self.name)

def info():
        print('클래스 변수 :', Person.name)

# 66. self에 대해 간략하게 설명해 보세요.
self는 인스턴스 객체를 가져온다.
p = Person('홍길동')
이렇게 인스턴스를 만들 때 self에는 p가 들어온다.

# 정답
self는 만들어질 인스턴스(객체)를 의미하며,
인스턴스가 만들어지면 자동으로 파이썬에서 self에 전달해줌.

# 67. 위의 예시코드를 완성하여 인스턴스 메소드와 클래스 메소들를 호출해 보세요.
p._info()

Person.info()

# 68. Person 객체의 네임 스페이스를 확인하는 코드를 작성하세요.
Person.__dict__


# 69. Person 객체가 갖고 있는 변수 또는 메소드의 이름을 확인하기 위한 코드를 작성하세요.

?????????????????
print(dir(Persion))

# 70. 위의 Person 클래스를 상속 받는 학생(Student) 객체를 만들어 다음과 같이 동작할 수 있도록 만들고,
# 실행해 보세요.
#  study 메소드를 호출 시 : "홍길동님은 열심히 공부합니다." 
class Student(Person):
    def study(self):
        print(f'{self.name}님은 열심히 공부합니다.')
        
s1 = Student('홍길동')
s1.study()


# 71. 위의 Person 클래스를 상속 받는 선생(Teacher) 객체를 다음과 같이 동작할 수 있도록 만들어 보세요.
# teach 메소드를 호출 시 : "홍길동님은 열심히 학생을 가르칩니다.." 
class Teacher(Person):
    def teach(self):
        print(f'{self.name}님은 열심히 학생을 가르칩니다..')
        
t1 = Teacher('홍길동')
t1.teach()


# 수고하셨습니다.. ^^
