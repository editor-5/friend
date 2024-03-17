# Selenium 임포트
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome(r"C:\Users\gas00\chromedriver-win64")

# 사이트 접속하기
driver.get('https://codeit.kr')
