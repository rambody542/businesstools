from selenium import webdriver
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    # 브라우저를 열어서 페이지 가져오기
    driver = webdriver.Chrome()
    driver.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2))
    
    # 페이지가 로드될 때까지 기다리기 (여기서는 간단하게 5초 기다림)
    driver.implicitly_wait(5)
    
    # 페이지의 HTML 가져오기
    content = driver.page_source
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(content, 'html.parser')
    
    # 필요한 정보 추출
    containers = soup.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)
    
    # 브라우저 닫기
    driver.quit()

get_exchange_rate('usd', 'krw')