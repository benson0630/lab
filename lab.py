number = {0:'零',1:'壹',2:'貳',3:'參',4:'肆',5:'伍',6:'陸',7:'柒',8:'捌',9:'玖',}
leng = {0:'',1:'拾',2:'佰',3:'仟'}
b = []
ans = input('請輸入1~999999999的數字')
y = 1
if int(ans) >=1 and int(ans) <=999999999:
    for i in range(len(ans)):
        a = number[int(ans[i])]
        b.append(a)
        b.append(leng[len(ans)-y])
        y = y+1
    b.append('元整')
    for i in range(len(b)):
        print (b[i],end='')
else:
    print('請輸入1~999999999的數字')
 
    
