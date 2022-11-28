from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

# 공인중개사: https://land.hackers.com/site/?st=guide&idx=50&etype=eland&tree_no=312&sub_no=318&sub_menu_no=803&page=10&islnb=y&division=1
# 전기기사(17) : https://pass.hackers.com/?r=pass&?r=pass&c=exam/review&g_id=1
# 주택관리사: https://house.hackers.com/site/?c=review&site=2&tree_no=438
# 한국사: https://history.hackers.com/?r=history&c=exam/review


category = ['real estate agent','electrical engineer','housing manager','Korean history']
pages= [60,17,10,22]
