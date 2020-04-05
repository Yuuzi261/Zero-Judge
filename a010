# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:24:43 2019

@author: ASUS
"""
import sys

def main():
    for s in sys.stdin:
        a = int(s)
        count = 0
        div = 2
        while a != 1:
            while a%div == 0:
                a/=div
                count+=1
            if count == 1:
                print(div,end = '')
            elif count > 1:
                print(div,'^',count,sep = '',end = '')
            if a != 1 and count != 0:
                print(' * ',end = '')
            div+=1
            count = 0
    
        print('\b\b  ')
    
    
    
main()
