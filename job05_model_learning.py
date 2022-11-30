import numpy as np
import matplotlib.pyplot as plt
from keras.models import *
from keras.layers import *

X_train, X_test, Y_train, Y_test = np.load(
    './models/news_data_max_20_wordsize_12027.npy', allow_pickle=True)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

model = Sequential()
model.add(Embedding(12027, 300, input_length=20))         #라벨은 서로 계산해봐야 의미가 없는 것.
                                                        #형태소를 숫자 라벨로 바꾼 것. 토큰라이저
                                                        #라벨 > 계산을 할 수 있게 만드는 것이 임베딩
#300차원이라는 것 => 단어하나당 300개의 좌표가 만들어진다는 말


model.add(Conv1D(32, kernel_size=5, padding='same', activation='relu'))
        #콘브레이어는 예를들어 문장이 젤 긴게 20개,
        #1D는 1차원,
model.add(MaxPool1D(pool_size=1))
model.add(GRU(128, activation='tanh', return_sequences=True))   #문장이라는게 순서를 가지고 있기 때문에
                                                         #리턴 시퀀시스는 앞단의 GRU가 뭘 리턴할 것인가.
model.add(Dropout(0.3))
model.add(GRU(64, activation='tanh'))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['accuracy'])
fit_hist = model.fit(X_train, Y_train, batch_size=128,
                     epochs=10, validation_data=(X_test, Y_test))

model.save('./models/news_category_classfication_model_{}.h5'.format(
    np.round(fit_hist.history['val_accuracy'][-1], 3)))

plt.plot(fit_hist.history['accuracy'], label='accuracy')
plt.plot(fit_hist.history['val_accuracy'], label='val_accuracy')
plt.legend()
plt.show()





#conv2D





