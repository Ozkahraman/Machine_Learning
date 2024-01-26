#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
veriler = pd.read_csv("veriler.csv")
print(veriler)

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy', 'kilo']]
print(boykilo)

x= 10

#%%   BOS OLAN DATALARA OTOMATIK DEGER ATAMA
from sklearn.impute import SimpleImputer
eVeriler = pd.read_csv("eksikveriler.csv")

imputer = SimpleImputer(missing_values=np.nan,strategy='mean')#ortalama deger hesaplayan ve missing valuelaraı o ortalamaya gore dolduracak olan bir araç yarattık

Yas = eVeriler.iloc[:,1:4].values#index/location-based iloc ile belirtilen satır ve sütun konumlarından gelen veriyi seçiyoruz
print(Yas)
imputer = imputer.fit(Yas[:,1:4])#fit yöntemi, onundeki kulllanıldıgı fonksiyonun işlemini gerçekleştir demektir makineye ogretme komutu-her sütunun ortalamasını hesaplamak için kullanılır
Yas[:,1:4] = imputer.transform(Yas[:,1:4])#fit ile ogrendigi seyi transformla uyguatıyoruz yani eksik olan kısımları ortalama degere gore dolduracak
print(Yas)#ortalama =28.45

sonuc1 = pd.DataFrame(data = Yas, index=range(22), columns=['boy', 'kilo', 'yas'])
print(sonuc1) 

#%%   KATEGORIK VERILERI NUMERIK HALE GETIRME TR=1, US=2, FR=0 
from sklearn import preprocessing

veriler = pd.read_csv("veriler.csv")
ulkeler = veriler.iloc[:,0:1].values #!! eger ilocun icini [:,0] diye kullanırsak array olarak alıyor tek satır [:,0:1] olarak kullanırsak tek sutun alıyo!!
print(ulkeler[:,0:1])

le = preprocessing.LabelEncoder()#label encoder sınıfı olusturuldu
ulkeler[:,0] = le.fit_transform(veriler.iloc[:,0])#ulkelere gore sayısal degelerler atandı
print(ulkeler)

ohe = preprocessing.OneHotEncoder()
ulkeler = ohe.fit_transform(ulkeler).toarray()#ulkeler dizisinin icine array olarak entegre edildi
print(ulkeler)

sonuc2 = pd.DataFrame(data = ulkeler, index=range(22), columns=['fr', 'tr', 'us'])#datası ulkeler olan satır sayısı 22 sutun degerleri ['fr', 'tr', 'us'] olan dataFrame
print(sonuc2)

cinsiyet = veriler.iloc[:,4:5]
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index=range(22), columns=['cinsiyet'])
print(sonuc3)

s = pd.concat([sonuc2,sonuc1], axis=1)#sonuc2 ve sonuc1 matrislerini column lar yan yana gelecek şekilde birleştiriyoruz axis = 1 column / axis = 0 index 
print(s)

d = pd.concat([s, sonuc3], axis=1)
print(d)


#%%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0) #verileri test ve egitim icin boluyoruz

from sklearn.preprocessing import StandardScaler 

sc = StandardScaler()

X_train = sc.fit_transform(x_train)#verileri olcekliyoruz
X_test = sc.fit_transform(x_test)

