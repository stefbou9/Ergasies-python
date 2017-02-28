#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Dwse mia protash gia eisodo"
protash=raw_input()
arithmosthavmastikwn=protash.count("!")
arithmosthavmastikwn=arithmosthavmastikwn-1
protash=protash.replace('!','',arithmosthavmastikwn)
print protash
