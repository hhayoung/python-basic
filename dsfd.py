from selenium import webdriver as wd

# 아래 3가지 모듈을 한 묶음으로 많이 사용
# ('기대조건이 될 때까지 기다리겠다는 의미'로 활용)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

import xlsxwriter as xw

#이미지다운할때 필요
from io import BytesIO
import urllib.request as req

# 인스턴스 = 클래스() 생성자 호출해서 초기화해준 것.
chrome_options = Options()
# print(type(chrome_options))

# Headless 모드(브라우저를 띄우지 않고 사용하는 모드) - 테스트하다보면 계속 브라우저 뜨는게 귀찮음
chrome_options.add_argument('--headless')

# webdriver 설정(Chrome, Firefox, ie ...) - Headless 모드로 설정됨
browser = wd.Chrome('./webdriver/chromedriver.exe', options=chrome_options)
# -> options을 설정해주면 브라우저가 이제 뜨지 않음.



# 엑셀 처리하기 위한 workbook(엑셀전체) 생성. 그 다음이 -> worksheet
workbook = xw.Workbook('./crawl_result.xlsx')

# 워크시트 생성
worksheet = workbook.add_worksheet()



# 일반모드(브라우저 띄움)
# browser = wd.Chrome('./webdriver/chromedriver.exe')

# 브라우저 내부 대기시간 설정
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1280, 760)

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 페이지 내용 확인하기
# print(f'page content : {browser.page_source}')

# 더보기 클릭하기
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
# 페이지를 다 못불러왔는데 클릭되면 에러가 나니까, 다 로딩될때까지 3초간 기다리겠다.
# 3초동안 안되면 에러겠지만, 보통 3초는 긴 시간

# 특정한 태그 딱 하나의 값만 필요할 때는 분석할 필요 없이
# 개발자도구 -> 그 태그 우클릭 -> Copy -> Copy Selector or Copy Xpath
# //*[@id="dlMaker_simple"]/dd/div[2]/button[1] <- Xpath 카피해온 거

# 현재는 브라우저를 계속 띄우면서 확인할 수 있지만, 보통 브라우저를 안띄우고
# 개발하니까 수시로 프린트로 확인하기
# print(f'page content : {browser.page_source}')

# 원하는 상품 클릭하기
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()
# 원하는 상품 페이지 확인
# print(f'page content : {browser.page_source}')

# 2초간 렌더링 할 수 있게 시간을 준다.
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링할 페이지 수
target_page = 1 # 3페이지까지만 가져옴.

# 엑셀의 행번호
row_num = 1

while cur_page <= target_page:
    
    # bs4 초기화
    bs = BeautifulSoup(browser.page_source, 'lxml')
    # 클릭하자마자 소스를 가져와서 브라우저가 데이터를 가져오기도 전에 분석한 것.
    # 그래서 원하는 데이터를 못 가져온 것. -> 렌더링할 시간을 줘야 한다. 
    # time 모듈 사용

    # 소스코드 정리해서 보기(분석해야될 코드들 출력)
    # print(bs.prettify)

    # 중간중간 광고상품들을 걸러내고 가져와야 한다.(분석 잘 하기)
    # ctrl + F 해서 클래스명이 하나인지 여러개인지도 분석

    prod_list = bs.select('div.main_prodlist.main_prodlist_list > ul > li')
    # print(prod_list)  # 리스트 안에 담겨서 옴
    
    # 페이지 번호 출력
    print(f'************** Page : {cur_page} **************')
    print()
    

    # 원하는 정보 추출(계속 추출)
    for li in prod_list:
        if not li.find('div',class_='ad_caster'):
            
            # 상품명, 가격 엑셀에 저장
            prod_name = li.select('p.prod_name > a')[0].text.strip()
            prod_price = li.select('p.price_sect > a')[0].text.strip()

            img_attr = li.select('a.thumb_link > img')[0].get('data-original')
            img_src = li.select('a.thumb_link > img')[0]['src']
            # 이미지
            time.sleep(2)
            # 이미지 요청 후 바이트로 변환
            img_data = BytesIO(req.urlopen(img_attr if img_attr else img_src).read())

            # 엑셀 저장
            worksheet.write(f'A{row_num}',prod_name)
            worksheet.write(f'B{row_num}',prod_price)
            
            worksheet.insert_image(f'C{row_num}',prod_name, {'image_data':img_data})
            
            row_num += 1
            
        print()
    print()
    
    cur_page += 1

    if cur_page > target_page:
        print('크롤링 성공!!')
        break
        
    # 페이지 클릭(공부차원으로 By.CSS_SELECTOR로 변경)
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,f'div.number_wrap > a:nth-child({cur_page})'))).click()
    
    # 클릭하자마자 for문이 다시 돌아버리니까 
    # 2초간 대기
    time.sleep(2)
    
    # number_wrap 클래스명을 가진 div 태그 안에 a 태그 7개
    # 총 페이지가 7페이지까지 있어서 a태그도 7개까지 있는데
    # 그 중에 2랑 3페이지 가져올 때, nth-child(2), nth-child(3) 
    # 이런식으로 가져오면 될 듯. nth-child(cur_page)
    
    
browser.quit()

# close()를 해줘야지만 생성된다.
workbook.close()