def gugudan_input(number):
    num = int(number)
    for i in range(1,10):
        print(f'{num} x {i} = {num*i}')

def gugudan_vertical():
    for i in range(2,10):
        for j in range(1,10):
            print(f'{i} x {j} = {i*j}')
        print()

def gugudan_horizontal():
    for i in range(1,10):
        for j in range(2,10):
            print(f'{j} X {i} = {j*i}',end='\t')
        print()


while True:
    print('''
        ============메뉴============
        1. 입력 단 출력
        2. 구구단 세로 출력
        3. 구구단 가로 출력
        4. 종료
        ============================
    ''')
    num = input('숫자를 입력하세요 : ')
    if num == '1':
        input_num = input('원하는 단 : ')
        gugudan_input(input_num)
    elif num == '2':
        gugudan_vertical()
    elif num == '3':
        gugudan_horizontal()
    elif num == '4':
        print('종료합니다...')
        break
    else:
        print('1~4까지의 숫자만 입력하세요')