#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Dwse mia akolouthia parenthesewn gia eisodo"
parentheseis=raw_input()
lista=list(parentheseis)
apanthsh="False"
megethos=int(len(lista))
megethos=megethos-1
arithmospar1=lista.count('(')
arithmospar2=lista.count(')')
s1=0
s2=0
if arithmospar1==arithmospar2:
    if lista[0]=="(":
        apanthsh="True"
        for i in range(0,megethos):
            if lista[i]=="(":
                s1=s1+1
            else:
                s2=s2+1
            if s1<s2:
                apanthsh="False"
                break
print apanthsh
