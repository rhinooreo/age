driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	
	raise SystemExit

age = int(input('請問你的年齡？'))
if driving == '有':
	if age >= 18:
		print('恭喜你通過測驗！')
	else:
		print('奇怪 你怎麼有開過車？')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了啊，怎麼還不去考？')
	else:
		print('很好，再過幾年就可以考駕照了！')