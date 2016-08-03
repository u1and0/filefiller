from itertools import *
from more_itertools import *
# def chunks(l, n):
# 	'''
# 	l:リスト
# 	n:数字
# 	lからnずつgenerate
# 	'''
# 	for i in range(len(l)):
# 		yield l[i:i + n]





def fill(x):
	'''
	引数x(リスト形式)を二つずつに分ける
	二つの要素間の差が<一定値>未満のときは
	要素間を穴埋めする要素を入れる
	'''
	x.append(x[-1]+1)
	for two in chunks(x,2):
		print(two)
		if two[-1]-two[0]>1:
			x.insert(x.index(two[-1]),two[0]+1)
			print('insert',two[0]+1)
	x.pop()





for zp in pairwise([0,3,4,5,9]):
	zp=list(zp)
	if zp[-1]-zp[0]>1:
		zp.insert(zp.index(zp[-1]),zp[0]+1)
		print('insert',zp[0]+1)
print(zp)



# liofli=[[0,3,4,5,9],[0,2,4,6,8,10],[0,5]]
# for li in liofli:
# 	print([i for i in pairwise(li)])





# for i in x:
# 	fill(i)
# 	print(x)
# 	print('\n')
