
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pickle


from keras.models import load_model

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', 15)
df = pd.read_csv('./crawling_data/hackers_reviews.csv')
print(df.head())
df.info()

X = df['reviews']
Y = df['category']

with open('./models/label_encoder.pickle', 'rb') as f:
    encoder = pickle.load(f)

labeled_Y = encoder.transform(Y)
onehot_Y = to_categorical(labeled_Y)


okt = Okt()
for i in range(len(X)):
    X[i] = okt.morphs(X[i], stem=True)
print(len(X))
stopwords = pd.read_csv('./stopwords.csv', index_col=0)
for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if X[j][i] not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)

with open('./models/hackers_token.pickle', 'rb') as f:
    token = pickle.load(f)     #미리 저장했떤 토큰으로 토큰아이저 진행하고
tokened_X = token.texts_to_sequences(X)
for i in range(len(tokened_X)):
    if len(tokened_X[i]) > 5114:     #20개보다 더 긴 제목은. 20개 이후는 다 짤라서. 앞에 20개만
        tokened_X[i] = tokened_X[i][:5114]
X_pad = pad_sequences(tokened_X, 5114)

model = load_model('./models/news_category_classfication_model_0.973.h5')    #여기서 숫자는 정확도
preds = model.predict(X_pad)
label = encoder.classes_
category_preds = []
for pred in preds:
    category_pred = label[np.argmax(pred)]
    category_preds.append(category_pred)
df['predict'] = category_preds


#맞은것만 트루로 바꾸기
df['OX'] = False         #확인할때 나오는 것. 두개 나오니까..
for i in range(len(df)):
    if df.loc[i, 'category'] == df.loc[i, 'predict']:
        df.loc[i, 'OX'] = True



df.info()
print(df.head(30))
print(df['OX'].value_counts())
print(df['OX'].mean())

print(df.loc[df['OX']==False])

