# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:59:51 2021

@author: Hasan
"""
# Veri Yapıları 11. ders 
# Binary Tree

class Node:
    def __init__(self, data):
        self.left   = None
        self.right  = None
        self.parent = None  # yeni
        self.data   = data
   
    def insert(self, data):
        if self.data:                           # karılaştırma yaparak ekle
            if data < self.data:                # küçükse sola       düğümdeki ve ekleneceği karşılaştırıyor. 
                if self.left is None:           # sol boşsa sola ekle
                    self.left = Node(data)
                    self.left.parent = self     # yeni
                else:
                    self.left.insert(data)      # sol boş değilse sol alt-ağaca ekle
            elif data > self.data:              # büyükse sağa
                if self.right is None:          # sağ boşsa sağa ekle
                    self.right = Node(data)
                    self.right.parent = self    # yeni
                else:                           # sağ boş değilse sağ alt-ağaca ekle
                    self.right.insert(data)
        else:
            self.data = data                    # ağacın ilk düşümü
            
    # Ağacı yazdır
    def PrintTree(self):
        
        #print( self.data,end='-')      # preorder= Kök + Sol + Sağ
       
        if self.left:
            self.left.PrintTree()
       
        print( self.data,end='-')       # inorder= Sol + Kök + Sağ
        
        if self.right:
            self.right.PrintTree()
            
        #print( self.data,end='-')      # postorder= Sol + Sağ + Kök
                
        
    def sizeTree(self): 
        if self.left and self.right:
            return 1 + self.left.sizeTree() + self.right.sizeTree()
        elif self.left:
            return 1 + self.left.sizeTree()
        elif self.right:
            return 1 + self.right.sizeTree()
        else:
            return 1
    
    def depth(self):
        if self.left and self.right:
            l = self.left.depth()
            r = self.right.depth()
            return 1 + max(l,r)
        elif self.left:
            return 1 + self.left.depth()
        elif self.right:
            return 1 + self.right.depth()
        else:
            return 1

# Use the insert method to add nodes

root = Node(25)
root.insert(12)
root.insert(10)
root.insert(22)
root.insert(5)
root.insert(36)
root.insert(30)
root.insert(40)
root.insert(28)
root.insert(38)
root.insert(48)
root.PrintTree()


"""
# 25,36,20,10,5,22,40,48,38,30,22,12,28
root = Node(25)
root.insert(36)
root.insert(20)
root.insert(10)
root.insert(5)
root.insert(22)
root.insert(40)
root.insert(48)
root.insert(38)
root.insert(30)
root.insert(12)
root.insert(28)
print(root.sizeTree(),root.depth())
"""
"""
Ağaç Uygulamaları

** Ağaçtan Düğüm Silme 
    * 1. durum 0 12 nin silinmesi (Yaprak düğüm ise direkt sil)
        12 bellekten silinecek parent ı null gösterecek
    
    * 30 un silinmesi (sağ ya da sol kol boş ise direkt düğüm silinir.Dolu kol yerine gelir.)
        30 u sileceğiz. 28 i 30 un yerine koyacağız.ağaç yine sıralı olacak.
    * 36 nın silinmesi (ara düğüm silinecekse)    
        *yöntem 1 : sol koldaki en büyük düğüm ya da sağ koldaki en küüçük düğüm
        *yöntem 2 : sağ veya sol kol dengei olsun diye derinlik (veya eleman sayısı) fazla olan koldaki düğüm silinen düğüm yerine getirilir.

** Ağaç Üzerinde Gezinme 













"""
























 
