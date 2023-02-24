
def fectorail (n):
	if n ==1:
		return 1
	else:
		reslut=n*fectorail(n-1)
		return reslut
print(fectorail(n))
