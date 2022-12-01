##전처리/다중분류기

##카데고리 컬럼은, 라벨링 한다음에, 원핫 인코더 해야함.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pickle

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling_data/hackers_reviews.csv')
print(df.head())
print(df.category.value_counts())
df.info()

X = df['reviews']       #컬럼명을 써준거다.
Y = df['category']     #이것도

encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y)
print(labeled_Y[:5])
print(encoder.classes_)

with open('./models/label_encoder.pickle', 'wb') as f:
    pickle.dump(encoder, f)
onehot_Y = to_categorical(labeled_Y)
print(onehot_Y[:5])


#형태소 단위로 잘라주기
#명사 하나만 뽑아내는 것 : 형태소
#okt : 자바언어


okt = Okt()
okt_morph_X = okt.morphs(X[1111], stem=True)
print(X[1111])
print(okt_morph_X)


for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)

    if i % 100 == 0:
        print('.', end='')
    if i % 1000 == 0:
        print()

#조사 버려주기: 한글자 버려주기(물론 한글자 단어도 있지만ㅋ)


stopwords = pd.read_csv('./stopwords.csv', index_col=0)
for j in range(len(X)):     #x다섯개만 보는 것. 줄 다섯개까지
    words = []       #빈리스트 워드를 만들고
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in stopwords['stopword']:   #스탑워즈 : 자연어 처리업계에서 불용어를 부를 때.
                words.append(X[j][i])
    X[j] = ' '.join(words)    #뛰어쓰기를 이어서 하나의 문장을 만들어주는 것.
    # print(X[j])

token = Tokenizer()    #각각의 형태소를 숫자로 라벨링.
token.fit_on_texts(X)       #뭔가 바꿔주는 애들은 핏트랜스폼해야 #종이백
tokened_X = token.texts_to_sequences(X)
wordsize = len(token.word_index) + 1      #0까지 포함한 갯수
# print(tokened_X)
# print(wordsize)

#토큰 저장
with open('./models/hackers_token.pickle', 'wb') as f:
    pickle.dump(token, f)



max_len = 0
for i in range(len(tokened_X)):
    if max_len < len(tokened_X[i]):
        max_len = len(tokened_X[i])
print(max_len)

X_pad = pad_sequences(tokened_X, max_len)

X_train, X_test, Y_train, Y_test = train_test_split(
   X_pad, onehot_Y, test_size=0.1)

print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./models/hackers_reviews_max_{}_wordsize_{}.npy'.format(max_len, wordsize), xy)




#슬라이싱 한것 모두 X로 바꿔주기.



