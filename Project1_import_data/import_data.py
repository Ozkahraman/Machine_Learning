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
imputer = imputer.fit(Yas[:,1:4])#fit yöntemi, her sütunun ortalamasını hesaplamak için kullanılır
Yas[:,1:4] = imputer.transform(Yas[:,1:4])#fit ile ogrendigi seyi transformla uyguatıyoruz yani eksik olan kısımları ortalama degere gore dolduracak
print(Yas)#ortalama =28.45

#%%   KATEGORIK VERILERI NUMERIK HALE GETIRME TR=1, US=2, FR=3 
from sklearn import preprocessing

veriler = pd.read_csv("veriler.csv")
ulkeler = veriler.iloc[:,0:1].values #!! eger ilocun icini [:,0] diye kullanırsak array olarak alıyor tek satır [:,0:1] olarak kullanırsak tek sutun alıyo!!
print(ulkeler)
