# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:34:59 2017

@author: Administrator
"""
movies=["The Holy Grail",'1975',"Terry Jones & Terry Gilliam",91,
            ["Graham Chapman",
                 ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print (each_item)
            

print_lol(movies)
#构建一个输出函数，在函数内判断每一个list项的属性，如果仍是list，那么就继续调用该函数
#调用完成后自动弹出
