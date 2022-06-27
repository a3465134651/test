import random
number = random.randint(1,100)
#print(number)
guess = input('請猜1到100之間1個數字:')
guess2 = int(guess)
i = 0
while guess2 != number :
	i = i + 1
	print('這是你猜的第', i ,'次')
	if guess2 < number:
		guess2 = int(input('答案比你猜的大，再猜看看:'))
	elif guess2 > number:
		guess2 = int(input('答案比你猜的小，再猜看看:'))
print('答對了!，菱菱好棒!')
