def digitalTransfer(m,y):   
    if int(m) < 1 or int(m) > 999999999:
        return ('請輸入1~999999999的數字')
    elif int(m[:1]) == 0:
        return ('第一個字請別輸入0')
    else:
        for i in range(len(m)):
            a = number[int(m[i])]
            ans.append(a)
            ans.append(leng[len(m)-y])
            y = y+1
        ans.append('元整')
        return 1

number = {0:'零',1:'壹',2:'貳',3:'參',4:'肆',5:'伍',6:'陸',7:'柒',8:'捌',9:'玖',}
leng = {0:'',1:'拾',2:'佰',3:'仟',4:'萬',5:'拾',6:'佰',7:'仟',8:'億'}
ans = []
money = input('請輸入1~999999999的數字')
y = 1
Transfer = digitalTransfer(money,y)
if Transfer == 1:
    for i in range(len(ans)):
        print (ans[i],end='')
else:
    print(Transfer)
