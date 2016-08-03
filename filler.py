from itertools import *
from more_itertools import *

def pair(x):
	'''
	引数x(リスト形式)を二つずつのペアに分け、fill関数に渡す
	'''
	for two in list(pairwise(x)):   #2つずつにわける
		print(two)
		if two[-1]-two[0]>1:
			for i in range(two[0]+1,two[-1]):   #rangeの逆順コピーを取り出す
				x.insert(x.index(two[-1]),i)
				print('insert',i)
		else:print('OK!')
	return x



'''TEST'''
li=[[1,5,6],[1,3],[0,1,8,11,16],[1,6,8,9,10,11,15]]
for x in li:
	print(pair(x))
	# print(bool(pair(x)==list(range(x[0],x[-1]+1))))
