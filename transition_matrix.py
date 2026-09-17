"""
已知：有一个隐藏的路径π，路径上包含状态 States 以及转移矩阵 Transition。HMM 的模型由符号Σ、状态 States 和转移矩阵 Transition 构成。
返回：这条路径的概率，即 Pr(π)。可以假设初始状态下的概率都是相等的
AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
--------
A   B
--------
    A   B
A   0.194   0.806
B   0.273   0.727

Pr(Π)=5.01732865318e-19
"""

import numpy as np
import re
'''
总共读取7行，有效数据是1.path 2.states 3.transition matrix
'''

#path
path:str=input().strip()

#去除分隔符
input()

#states
states=input().strip().split()

#去除分隔符
input()
input()

#transition matrix
def getnum(string:str):
    arr2:list=[]
    arr1:list=string.split()
    al1:int=len(arr1)
    for i in range(al1):
        if re.match(r"^[+-]?(?:\d+(?:\.\d*)?|\.\d+)$",arr1[i]):
            arr2.append(float(arr1[i]))
        else:
            continue
    return arr2

str1:str=input()
str2:str=input()
transition_matrix=np.array([getnum(str1),getnum(str2)])

#calculating the possibility
sl:int=len(path)
possibility:float=0.5
for i in range(sl-1):
    if path[i]=='A':
        if path[i+1]=='B':
            possibility*=transition_matrix[0][1]
        else:
            possibility*=transition_matrix[0][0]
    else:
        if path[i+1]=='B':
            possibility*=transition_matrix[1][1]
        else:
            possibility*=transition_matrix[1][0]
print(possibility)