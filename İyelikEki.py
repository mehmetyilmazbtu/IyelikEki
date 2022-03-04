# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
i=0
cıkıs="exit"

sesli=("a","e","ı","i","o","ö","u","ü")
Ek_ın=("a","ı")
Ek_in=("e","i")
Ek_un=("o","u")
Ek_ün=("ö","ü")
print("\nÇıkış yapmak için 'exit' yazın\n")
while i<5:
    
    isim=input("İsim giriniz: ")
    if isim==cıkıs: 
        break
    elif isim[-1] in Ek_ın:
        print(isim,"\b'nın")
    elif isim[-1] in Ek_in:
        print(isim,"\b'nin")
    elif isim[-1] in Ek_un:
        print(isim,"\b'nun")
    elif isim[-1] in Ek_ün:
        print(isim,"\b'nün")
    else:
        if isim[-2] in Ek_ın:
            print(isim,"\b'ın")
        elif isim[-2] in Ek_in:
            print(isim,"\b'in")
        elif isim[-2] in Ek_un:
            print(isim,"\b'un")
        elif isim[-2] in Ek_ün:
            print(isim,"\b'ün")
        elif isim[-3] in Ek_ın:
            print(isim,"\b'ın")
        elif isim[-3] in Ek_in:
            print(isim,"\b'in")
        elif isim[-3] in Ek_un:
            print(isim,"\b'un")
        elif isim[-3] in Ek_ün:
            print(isim,"\b'ün")
        else:
            print("Girdiğiniz isim Türkçe kurallarına uymamaktadır.")
        
            
            


