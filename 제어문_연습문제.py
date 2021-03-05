# 제어문 연습문제

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for x in q1:        # q1 또는 q1.keys()
    if x == '가을':
        print(q1[x])    # 값은 키로 접근할 수 있다.

for k, v in q1.items():
    if k == '가을':
        print(v)        # items() 이용


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for x in q2:
    if q2[x] == '사과':
        print('사과가 있습니다.')

for k, v in q2.items():
    if v == '사과':
        print(k,v)
        break
else:
    print('사과없음')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.(점수는 임의로 지정하여 테스트)
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 54

if score>=81 and score<=100:        # and 뒤에 조건을 더 안써줘도 된다. score>=81 하면 위에 다 포함이니까
    print('A학점')
elif score>=61 and score<=80:
    print('B학점')
elif score>=41 and score<=60:
    print('C학점')
elif score>=21 and score<=40:
    print('D학점')
elif score>=0 and score<=20:
    print('E학점')
else:
    print('점수를 제대로 입력해주세요.')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4 = [12, 6, 18]
_max = q4[0]
for x in q4[1:]:
    if x > _max:
        _max = x
print('가장 큰 숫자는 ',_max) 


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'
if s[7] == '1' or s[7] == '3':
    print('남자')
elif s[7] == '2' or s[7] == '4':
    print('여자')

# 다른 방법
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q6 = ["갑", "을", "병", "정"]

for x in q6:
    if x == '정':
        continue
    print(x)

# 리스트 내포
q66 = [x for x in q6 if x != '정']
print(q66)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
for i in range(1,101):
    if i%2:
        print(i, end=' ')
print()

# 리스트 내포
q77 = [x for x in range(1,101) if x%2==1] # x % 2 != 0
print(q77)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q8 = ["nice", "study", "python", "anaconda", "!"]

for x in q8:
    if len(x) >= 5:
        print(x)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q9 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for x in q9:
    if x.islower():
        print(x)

q99 = [x for x in q9 if x.islower()]
print(q99)

for x in q9:
    if x.isupper():
        continue
    else:
        print(x)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q10 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for x in q10:
    if x.islower():
        print(x.upper())
    else:
        print(x.lower())

# 리스트 내포
q1010 = [x.upper() if x.islower() else x.lower() for x in q10]
print(q1010)

# [ s.upper() if s.islower() else s.lower() for s in q10 ]
# 조건 ? 참 : 거짓
