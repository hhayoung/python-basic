
# 기본 출력
print('hello python')
print("hello python")
print()
print('''hello python''')
print("""hello python""")

# saparator 옵션
print('T','E','S','T',sep='/')

# separator를 이용해서 TEST 출력
print('T','E','S','T',sep='')

# 2020-07-14 출력
print('2020','07','14',sep='-')

# test@naver.com
print('test','naver.com',sep='@')

print('------------- end 옵션 ---------------')
# end 옵션의 default 값은 \n
print('welcome To',end='\n')
print('welcome To',end='')
print('Test')

# format 사용
print('{} and {}'.format('You','Me'))
print('{0} and {1} and {0}'.format('You','Me'))
print('{var1} and {var2}'.format(var1='You',var2='Me'))

# %d, $f, $s
print("%s의 나이는 %d" %('홍길동', int(33)))
print('Test1: %5d, Price: %4.2f' %(766,543.123))
print('Test1: {a:5d}, Price: {b:4.2f}'.format(a=766,b=6543.123))

'''
Escape 코드

\n : 개행
\t : xoq
\\ : \
\' : '
\" : "

'''
print('국어 \t 영어 \t 수학')
print('국어 \' 영어 \' 수학')