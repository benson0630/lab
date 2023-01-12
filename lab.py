number = {0:'零',1:'壹',2:'貳',3:'參',4:'肆',5:'伍',6:'陸',7:'柒',8:'捌',9:'玖',}
leng = {0:'',1:'拾',2:'佰',3:'仟',4:'萬',5:'拾',6:'佰',7:'仟',8:'億'}
ans = []
money = input('請輸入1~999999999的數字')
y = 1
if int(money) < 1 or int(money) > 999999999:
    print('請輸入1~999999999的數字')
elif int(money[:1]) == 0:
    print('第一位數字請別輸入0')
else:
    for i in range(len(money)):
        a = number[int(money[i])]
        ans.append(a)
        ans.append(leng[len(money)-y])
        y = y+1
    ans.append('元整')
    for i in range(len(ans)):
        print (ans[i],end='') 
    
