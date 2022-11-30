from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time
import datetime

category = ['real estate agent','TOEIC','housing manager','Korean history']
# pages= [60,17,10,22]
pages= [60,130,10,20]
options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_reviews = pd.DataFrame()
for i in range(1, pages[1]+1):               #page
# for i in range(1, pages[1]+1):
    reviews = []
    url = 'https://champ.hackers.com/?r=champstudy&c=community%2Fcm_toeic%2Ftoeic_review&func=&order=favorite&me=&qna_id=&anker=Y&p={}&file=https%3A%2F%2Fwww.youtube.com%2Fembed%2FmNvYB1kXxlY&img=%2F%2Fgscdn.hackers.co.kr%2Fchamp%2Fimg%2Fplayer%2Fhacsong.png&width=250px&height=150&s_key=1&s_value='.format(i)
    driver.get(url)
    time.sleep(0.2)
    print('디버그', i)
    for j in range(6, 16):  #게시글
        x_path = '//*[@id="procForm"]/div[6]/div[1]/div[3]/table/tbody/tr[{}]/td[3]/a'.format(j)
        driver.find_element('xpath', x_path).send_keys(Keys.ENTER)
        time.sleep(0.5)
        try:
            review_xpath = '//*[@id="teachAnker"]/div[4]'
            review = driver.find_element('xpath', review_xpath).text
            review = re.compile('[^가-힣 ]').sub(' ', review)
            reviews.append(review)
            driver.back()
            print('디버그 ',i,j-5)
        except NoSuchElementException as e:
            try:
                review_xpath = '//*[@id="teachAnker"]/div[4]'
                review = driver.find_element('xpath', review_xpath).text
                review = re.compile('[^가-힣 ]').sub(' ', review)
                reviews.append(review)
                driver.back()
                print('디버그 ', i, j - 5)
            except NoSuchElementException as e:
                print('error', i, j - 5)
        except:
            print('error', i, j - 5)
    if i % 10 == 0:  # 10페이지마다 데이터 저장
        df_section_reviews = pd.DataFrame(reviews, columns=['reviews'])
        df_section_reviews['category'] = category[1]
        df_reviews = pd.concat([df_reviews, df_section_reviews], ignore_index=True)
        df_reviews.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[1], i), index=False)
        df_reviews = pd.DataFrame()
        reviews = []
