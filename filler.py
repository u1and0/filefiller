def chunks(l, n):
	'''
	l:リスト
	n:数字
	lからnずつgenerate
	'''
	for i in range(len(l)):
		yield l[i:i + n]

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




x=[[0,3,4,5,5],[0,2,4,6,8,10],[0,5]]
for i in x:
	fill(i)
	print(x)
	print('\n')
