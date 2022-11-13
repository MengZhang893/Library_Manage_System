import hashlib
from common.login import login

path = '../member_data/member.txt'

def user_signup():
    '''
    此函数是为了登录图书管理系统，验证账号和密码
    :return:
    '''
    print('****欢迎登录图书管理系统****')
    print('****请输入要注册的账号密码：****')
    username = input('****请输入账号：')
    password = input('****请输入密码：')
    if len(password)<6:
        print('密码不能少于6位')
        rsignup = input('您是否要重新注册-yes/no:')
        if rsignup == 'yes':
            user_signup()
        else:
            print('退出程序')
            exit()
    else:
        rpassword = input('****请确认密码：')
        if rpassword == password:
            md5_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            md5_rpassword = hashlib.md5(rpassword.encode('utf-8')).hexdigest()
            print('用户注册成功')
            member_info = '{"username":"%s","password":"%s","rpassword":"%s"}\n'%(username,md5_password,md5_rpassword)
            # print(member_info)
            with open(path,'a',encoding='utf-8') as f:
                f.write(member_info)
            user_confirm = input('请问您是否要登录-yes/no:')
            if user_confirm == 'yes':
                login()
            else:
                print('当前程序已经退出，欢迎您下次再来。')
                exit()
        else:
            print('两次密码不一致')
            rsignup = input('您是否要重新注册-yes/no:')
            if rsignup == 'yes':
                user_signup()
            else:
                print('退出程序')
                exit()

if __name__ == '__main__':
    user_signup()


