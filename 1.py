for weishu in range(6,21):
    sum1 = sum(94 ** k for k in range(6, weishu+1 ))
    print("总共字典数%d"%sum1)
    print("%d 位数这种速率要" % weishu+str(sum1 / (830000 * 30 * 60 * 24))+"天" )
