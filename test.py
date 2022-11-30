from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time
import datetime
# 카테고리 = [공인중계사, 토익, 공무원,학점은행]
category = ['real estate agent','electrical engineer','housing manager','Korean history']
# pages = [60,1000이상,289,42]
# 게시글 = [20,10,10,10]
#  총    =[1200,만개이상,2890,1095]
pages= [60,10,10,20]
options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_reviews = pd.DataFrame()
for i in range(1, pages[0]+1):              #page
    reviews = []
    url = 'https://land.hackers.com/site/?st=guide&idx=50&etype=eland&tree_no=312&sub_no=318&sub_menu_no=803&page={}&islnb=y&division=1'.format(i)
    driver.get(url)
    time.sleep(0.2)
    print('디버그 ', i)


    for j in range(53, 73):  #게시글
        x_path = '//*[@id="p_content"]/div/div[3]/table/tbody/tr[{}]/td[3]/span'.format(j)
        driver.find_element('xpath', x_path).click()
        time.sleep(0.5)
        review_xpath = '//*[@id="p_content"]/div/div[1]/table/tbody/tr[2]/td'
        review = driver.find_element('xpath', review_xpath).text
        review = re.compile('[^가-힣 ]').sub(' ', review)
        reviews.append(review)
        driver.back()
        print('디버그 ',i,j-52)



    if i % 10 == 0:
        df_section_reviews = pd.DataFrame(reviews, columns=['reviews'])
        df_section_reviews['category'] = category[0]
        df_reviews = pd.concat([df_reviews, df_section_reviews], ignore_index=True)
        df_reviews.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[0],i),index=False)
        df_reviews = pd.DataFrame()
        reviews = []


 for l in range(1, 6):   # x_path
                x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(k, l)
                try:
                     title = driver.find_element('xpath', x_path).text
                     print(title)
                     title = re.compile('[^가-힣 ]').sub(' ', title)
                     titles.append(title)
                except NoSuchElementException as e:                                         #에러를 살리기 위해서. 하나도 안 놓치기 위해서. 에러가 나더라도 크롤링을 하게
                    try:
                         x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt/a'.format(k, l)    #dt뒤에 [2]숫자같은게 있으면 안됨
                         title = driver.find_element('xpath', x_path).text
                         title = re.compile('[^가-힣 ]').sub(' ', title)
                         titles.append(title)
                    except:                               #여기가서 프린트하고. 다음 것으로 넘어간다. 크롤링이 멈추는게 아닌.
                         print('error', i, j, k, l)
                except:
                     print('error', i, j, k, l )




















//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/


//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/a/span[2]
