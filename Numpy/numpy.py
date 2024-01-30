# -*- coding: utf-8 -*-

import numpy as np

liste = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
arraylist = np.array(liste)
print(arraylist)

dizi = np.array([1,2,3,4,5,6,7,8])
print(dizi)
print(dizi.shape)#array boyutu

dizi2 = dizi.reshape(2,4)
print("şekil:",dizi2.shape),
print("Boyut:",dizi2.ndim)
print("Veri Tipi:",dizi2.dtype.name)
print("Boy:",dizi2.size)
print("type:",type(dizi2))


dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(dizi2D)

sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

bir_dizi = np.ones((3,4))
print(bir_dizi)

bos_dizi = np.empty((3,4))
print(bos_dizi)

dizi_aralik = np.arange(10,50,5)#10 dan 5'er 5'er 50ye
print("aralik:", dizi_aralik)

dizi_bosluk = np.linspace(10,20,5)#10-20 arasını 5 eşit parçaya boluyo
print(dizi_bosluk)

kosegen_matris = np.eye(10)#10x10 kosegen birim matris
print(kosegen_matris)

float_array = np.float32([[1,2],[3,4]])
print(float_array)

a = np.array([[1,3,5],[7,9,11]])
b = np.array([[2,4,6],[8,10,12]])

print(a+b)
print(a-b)
print(a*b)

print(np.sum(a))
print(np.max(a))
print(a.argmax())#max sayinin indexi
print(np.min(a))
print(np.mean(a))#ortalaması
print(np.median(a))

rastgele_dizi = np.random.random((3,3))#0-1 arasında random 3x3 luk matris
print(rastgele_dizi)

print(np.random.randn(4))#dizi donduruyo rastegele tek noyutlu
print(np.random.randn(4,4))#4x4 luk random matris
print(np.random.randint(1,10,5))#[1,10) araliginda 5 elemanlı tek boyutlu dizi

dizi = np.array([1,2,3,4,5,6,7,8,9])
print(dizi[0:4])#dizinin ilk 4 elemanı
print(dizi[::-1])#dizinin tersi

print(a[1,1])#1.satır 1. sutun indexlemeler 0 a 0 dan baslar
print(a[:,1])#butun satırlar 1. sutun sadece
print(a[1,1:])#1. satırın 1sutunundan sonrakiler
print(a.shape[:2])#vektorun yukseklik ve genisligini donuyo
vector = a.ravel() # vektor haline getiriyo
print(vector)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.zeros((3,3))
print(x.shape[0])
print(x.size)
print(x[1,1])
ttt = np.zeros(10)
ttt = np.arange(9, 1 ,-1)
print(ttt)

matrix = np.array([[1,2,54,89,56],[9,8,75,6,47]])
for satir in matrix:
    for eleman in satir:
        print(eleman)
print(np.where(matrix==47))#(array([1]), array([4])) 2.satir 5.sutun
print(matrix <20)
new_matrix = matrix[matrix < 20]                                           #  *
print(new_matrix)

for i in np.arange(x.shape[0]-1, -1, -1):
    for j in np.arange(x.shape[1]-1, -1, -1):
        y[x.shape[0]-1-i,x.shape[1]-1-j] = x[i,j]   #kısaca y = x[::-1] matrisin tersi

print(y)