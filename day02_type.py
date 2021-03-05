# 파이썬의 데이터 타입(자료형)
# 데이터 타입, 숫자형, 숫자형 연산
'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열

컬렉션 타입 ***중요
list : 리스트
tuple : 튜플
set : 집합
dict : 사전
'''

# 데이터타입(Data Type)
v_str1 = 'GoodMan'
v_bool = True
v_str2 = 'Good Night'
v_float = 10.0
v_int = 7
v_list = [v_str1, v_str2]
v_dict = {
    "name" : '홍길동',
    "age" : 28
}
v_tuple = 3,6,8
v_set = { 7, 8, 9 }

# 데이터 Type 출력
print(type(v_str1))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_list))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))


# 변수 이름 규칙
'''
숫자로 시작하는 변수 이름 X
77aa(x)

변수는 소문자로 시작하는 것이 관례

예약어 사용할 수 없다.
class(x), int(x), def(x), ...
'''
# 숫자형 연산자
'''
+, -, *, /, %(나머지연산자), //(정수형 몫)
abs(x) : 절대값
pow : 제곱
x**y : 제곱
'''
print(10%3)
print(10/2)     # 실수형
print(10//2)    # 정수형

# 정수 선언
i = 77
ii = -21
big_int = 88888888888888888888888888888888888   # python은 어마어마한 숫자 변수에 담을 수 있다
print(i)
print(ii)
print(big_int)

# 실수 선언
f = 0.893823    # 그냥 소수점 넣으면 실수 선언 되는거
f2 = 3.1212
f3 = -3.9
f4 = 9/3        # 나누기 결과는 실수
print(f)
print(f2)
print(f3)
print(f4)

print("**************************")
print("i + ii : ", i+ii)
print("f + f2 : ", f+f2)
print("f + f3 : ", f+f3)
print("i + f2 : ", i+f2)    # 실수와 정수 = 실수

# 자료형(type) 출력함수 : type()
print(type(i), type(f))

# 형변환(casting)
# int, float, complex
a = 5.
b = 4
c = 10

result = a + b      # 실수형 타입
print(result)
print(int(result))  # 실수 -> 정수로 형변환
print(float(c))     # 정수 -> 실수로 형변환
print(complex(3))   # 정수 -> 복소수 형태로 (3+0j)
print(int(True))
print(int(False))

print('3')
print(int('3'))     # 이게 가능

# 수치연산 함수
print(abs(-7))      # 절대값
n, m = divmod(100,8)
print(n,m)          # 12 4 몫 나머지

import math         # math 패키지에는 수학에서 사용하는 많은 것들이 존재한다.
# ceil(), floor()   아주 많이 사용하는 거니까 알아두자
print(math.ceil(5.3))   # 올림
print(math.floor(3.8))  # 내림

print(round(3.5))
