#!/usr/bin/python
# -*- coding: utf-8 -*-
import statistics
print "Dwse arithmous gia na vrethei h tipikh apoklish, oi arithmoi prepeina einai xwrismenoi me komma p.x. 7,345,5,26,7"
stringinput=raw_input()
lista=stringinput.split(",")
lista=map(int,lista)
megethos=len(lista)
if megethos<5:
    print "Edwses 4 h ligoterous arithmous sinepws ama vgaloume tis 2 mikroteres kai tis 2 megaliteres times den menei kapoia timh gia na vrethei h tipikh apoklisi"
else:
    mikroteros=min(lista)
    lista.remove(mikroteros)
    mikroteros=min(lista)
    lista.remove(mikroteros)
    megalhteros=max(lista)
    lista.remove(megalhteros)
    megalhteros=max(lista)
    lista.remove(megalhteros)
    tat=statistics.pstdev(lista)
    print "H tipikh apoklish twn timwn einai:", tat

#gia na doulepsei auto to programma prepei na kanete install thn viviliothikh statistics
