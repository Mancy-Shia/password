i = 3
i = int(i)
while i:
    password = input()
    i = i - 1
    if password == 'a123456':
        print("登入成功")
        break
    else:
        print('密碼錯誤!')
        if i>0:
            print('還有', i, '次機會')
