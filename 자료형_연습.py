# 자료형 연습문제 

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('apple;orange;banana;lemon')
print('apple','orange','banana','lemon',sep=";")

# 3. 화면에 * 기호 100개를 표시하세요.
print('*'*100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
str_q4 = "30"
print(int(str_q4))
print(float(str_q4))
print(complex(str_q4))
print(str(str_q4))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
str_q5 = "Niceman"
print(str_q5[4:])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
str_q6 = "Strawberry"
print(str_q6[::-1])

print(list(reversed(str_q6)))


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
str_q7 = "010-7777-9999"
print(str_q7.replace('-',''))

print(str_q7[0:3]+str_q7[4:8]+str_q7[9:13])

# 정규표현식(Regular Expression)
import re
print(re.sub('[^0-9]','',str_q7))       # 0에서 9가 아닌거는 다 공백으로 바꾸겠다는 뜻.


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
str_q8 = "http://daum.net"
print(str_q8[7:])

idx = str_q8.index('http://')
print(str_q8[idx+7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
str_q9 = "NiceMan"
print(str_q9.upper())
print(str_q9.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
str_q10 = "abcdefghijklmn"
print(str_q10[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
list_q11 = ["Banana", "Apple", "Orange"]
list_q11.remove('Apple')
print(list_q11)



# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
tuple_q12 = (1,2,3,4)
print(list(tuple_q12))

print([s for s in tuple_q12])       # tuple_q12에서 하나씩 뽑아와서 s에 저장하고 s 출력


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
dict_q13 = { '성인' : 100000, '청소년' : 70000, '아동' : 30000 }
print(dict_q13)

dic = {}                # 비어있는 dict에 넣어주는 방법도 있음.
dic['성인'] = 100000
dic['청소년'] = 70000
dic['아동'] = 30000
print(dic)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
dict_q13['소아'] = 0
print(dict_q13)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(dict_q13.keys())
print(list(dict_q13.keys()))


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(dict_q13.values())
print(list(dict_q13.values()))


# *** 결과 값만 정확하게 출력되면 됩니다. ^^
