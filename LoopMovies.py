# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:20:34 2017

@author: Administrator
"""

movies=["The Holy Grail",'1975',"Terry Jones & Terry Gilliam",91,
            ["Graham Chapman",
                 ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
for each_item in movies:
    if isinstance(each_item,list):
        for each in each_item:
            if isinstance(each,list):
                for each1 in each:
                    print(each1)
            else:
                print(each)
    else:
        print (each_item)
#三重循环解决三层list嵌套问题
#接下来 我们需要将这个三层嵌套改为函数
