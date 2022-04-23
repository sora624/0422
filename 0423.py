pw = 'a123456'
t = 3

while True:
    question = input('Please input your password: ')
    if question == pw:
        print('Correct!')
        break

    else:
        t = t - 1
        print('Wrong Password, You have', t, 'times to try')
        if t == 0:
            print('Please try later')
            break

