from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time
import datetime
# 카테고리 = [공인중계사, 토익, 공무원,학점은행]
category = ['real estate agent','toeic','public official','Korean history']
# pages = [60,1000이상,289,42]
# 게시글 = [20,10,10,10]
#  총    =[1200,만개이상,2890,1095]
# pages= [60,10,10,20]
options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_reviews = pd.DataFrame()
for i in range(1, 290):              #page
    reviews = []
    url = 'https://gosi.hackers.com/html/mmove.htm?id=exam_passnote_new&m=&cate=&cate2=&cate3=&cate4=&cate5=&cate6=&idx=&user_id=&search_opt=&search_txt=&hb_year=&page={}'.format(i)
    driver.get(url)
    time.sleep(0.2)
    print('디버그 ', i)

    # if i == 1:
    #     for j in range(4, 19):  #게시글
    #         x_path = '//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/a/span[2]'.format(j)
    #         driver.find_element('xpath', x_path).click()
    #         time.sleep(0.5)
    #         review_xpath = '//*[@id="wrapper"]/div[4]/div[2]/div/div/div[2]'
    #         review = driver.find_element('xpath', review_xpath).text
    #         review = re.compile('[^가-힣 ]').sub(' ', review)
    #         reviews.append(review)
    #         driver.back()
    #         print('디버그 ', i, j - 1)
    #
    #          except ElementClickInterceptedException as e:  # 에러를 살리기 위해서. 하나도 안 놓치기 위해서. 에러가 나더라도 크롤링을 하게
    #          try:
    #
    # else:
    for j in range(2, 17):
        x_path = '//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/a/span[2]'.format(j)
        driver.find_element('xpath', x_path).click()
        time.sleep(0.5)
        review_xpath = '//*[@id="wrapper"]/div[4]/div[2]/div/div/div[2]'
        review = driver.find_element('xpath', review_xpath).text
        review = re.compile('[^가-힣 ]').sub(' ', review)
        reviews.append(review)
        driver.back()
        print('디버그2 ', i, j - 1)



        # if i!=1:
        #     j-=2
        #     x_path = '//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/a/span[2]'.format(j)
        # else:
        #     x_path = '//*[@id="wrapper"]/div[4]/div[2]/div[13]/div[1]/div/div/table/tbody/tr[{}]/td[1]/a/span[2]'.format(j)

        # if i % 10 == 0:
        #     df_section_reviews = pd.DataFrame(reviews, columns=['reviews'])
        #     df_section_reviews['category'] = category[3]
        #     df_reviews = pd.concat([df_reviews, df_section_reviews], ignore_index=True)
        #     df_reviews.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[0], i), index=False)
        #     df_reviews = pd.DataFrame()
        #     reviews = []




    # if i % 10 == 0:
    #     df_section_reviews = pd.DataFrame(reviews, columns=['reviews'])
    #     df_section_reviews['category'] = category[0]
    #     df_reviews = pd.concat([df_reviews, df_section_reviews], ignore_index=True)
    #     df_reviews.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[0],i),index=False)
    #     df_reviews = pd.DataFrame()
    #     reviews = []



        #driver.back()
        # search_box = driver.find_element_by_xpath('//*[@id="p_content"]/div/div[3]/table/tbody/tr[{}]/td[3]/span'.format(j))
        # driver.find_element_by_xpath('//*[@id="p_content"]/div/div[3]/table/tbody/tr[{}]/td[3]/span'.format(j)).click()
        # print('디버그 02')


        # selected_tag_a = driver.selected_tag_a.find_element_by_xpath('// *[ @ id = "p_content"] / div / div[3] / table / tbody / tr[{}] / td[3] / span'.format(j))
        # selected_tag_a.click()
    #     # //*[@id="p_content"]/div/div[3]/table/tbody/tr[72]/td[3]/span
    #     # // *[ @ id = "p_content"] / div / div[3] / table / tbody / tr[54] / td[3] / span
    #     # // *[ @ id = "p_content"] / div / div[3] / table / tbody / tr[55] / td[3] / span
    #     # // *[ @ id = "p_content"] / div / div[3] / table / tbody / tr[53] / td[3] / span
    #     url = 'https://land.hackers.com/site/?st=guide&id=guide_board_view&islnb=y&etype=eland&no={}&tree_no=312&sub_no=318&sub_menu_no=965&idx=guide_board_view&page={}'.format(j, i)
    #     for k in range(1, 5):    # x_path
    #        for l in range(1, 6):   # x_path
    #            x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(k, l)
    #            try:
    #                 title = driver.find_element('xpath', x_path).text
    #                 print(title)
    #                 title = re.compile('[^가-힣 ]').sub(' ', title)
    #                 titles.append(title)
    #            except NoSuchElementException as e:                                         #에러를 살리기 위해서. 하나도 안 놓치기 위해서. 에러가 나더라도 크롤링을 하게
    #                try:
    #                     x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt/a'.format(k, l)    #dt뒤에 [2]숫자같은게 있으면 안됨
    #                     title = driver.find_element('xpath', x_path).text
    #                     title = re.compile('[^가-힣 ]').sub(' ', title)
    #                     titles.append(title)
    #                except:                               #여기가서 프린트하고. 다음 것으로 넘어간다. 크롤링이 멈추는게 아닌.
    #                     print('error', i, j, k, l)
    #            except:
    #                 print('error', i, j, k, l )
    #
    #
    #
    #
    # if j % 10 == 0: #j가 10에 배수가 될때마다 한번씩 한다. 10페이지마다 한번씩 저장하겠다.
    #     df_section_title = pd.DataFrame(titles, columns=['r'])
    #     df_section_title['category'] = category[i]
    #     df_title = pd.concat([df_title, df_section_title], ignore_index=True)
    #     df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[i], j),
    #                     index=False)
    #     titles = []                    #에러가 날 경우에 시간


#time.sleep(10)

# # for i in range(0, 6):
#     titles = []
#     for j in range(1, pages[i]):
#
#         x_path = ''