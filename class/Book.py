class Book:
    def __init__(self, code, title, author, publisher):
        self.code = code
        self.title = title
        self.author = author
        self.publisher = publisher
        
    def book_info(self):
        print('도서코드 : ', self.code)
        print('도서명 : ', self.title)
        print('저자 : ', self.author)
        print('출판사 : ', self.publisher)


def set_info():
    code = input('도서코드 : ')
    title = input('도서명 : ')
    author = input('저자 : ')
    publisher = input('출판사 : ')
    print()
#     print(code, title, author, publisher)
    book = Book(code, title, author, publisher)
#           └ 입력받은 값 객체로 만들어주기
    return book
    
def print_book_info(book_list):
    print('-------------------')
    for book in book_list:
        book.book_info()
        print('-------------------')

def delete_book(book_list, title):
    for idx, book in enumerate(book_list):
        if book.title == title:   # 사용자가 입력한 title과 책 객체에 있는 title 비교
            del book_list[idx]
    
def load_book(book_list):
    with open('./book_db.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()  # 리스트 형태로 바뀜
        num = len(lines)/4  # 정보 4가지니까 4로 나눠주면 책이 몇권인지 알수 있음
        num = int(num)

        for i in range(num):
            code = lines[4*i].strip()
            title = lines[4*i+1].strip()
            author = lines[4*i+2].strip()
            publisher = lines[4*i+3].strip()
            book = Book(code, title, author, publisher)
            book_list.append(book)

        
def repo_book(book_list):
    with open('./book_db.txt', 'w', encoding='utf8') as f:
        for book in book_list:
            f.write(book.code + '\n')
            f.write(book.title + '\n')
            f.write(book.author + '\n')
            f.write(book.publisher + '\n')
        # 각 정보들 한 줄씩 저장 됨 
            
def menu_display():
    print('===================')
    print('1. 도서 정보 입력')
    print('2. 도서 정보 출력')
    print('3. 도서 삭제')
    print('4. 종료')
    print('===================')

    menu = input('메뉴 선택 : ')
    return int(menu)

def run():

    book_list = []
    load_book(book_list)

    while True:
        menu = menu_display()
        if menu == 1:
            book = set_info()
            book_list.append(book)
        elif menu == 2:
            print_book_info(book_list)
        elif menu == 3:
            title = input('삭제할 도서명을 입력하세요')
            delete_book(book_list, title)
        elif menu == 4:
            repo_book(book_list)
            print('종료합니다')
            break
        else:   
            print(' 1~4 숫자만 입력하세요')
    
    
if __name__=='__main__':
    run()
    



