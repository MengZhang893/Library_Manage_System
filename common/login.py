from common.signup import user_signup
import hashlib

def login():
    print('****欢迎来到图书管理系统****')
    user_status = input('您是否已经注册-yes/no：')
    if user_status == 'no':
        print('您还未注册，请先注册以后在登录！')
        user_signup()
    else:
        user_name = input('请输入用户名：')
        user_password = input('请输入密码：')
        with open('../member_data/member.txt','r') as f:
            result = f.readlines()
            user_info_list  = []
            for i in result:
                user_info_list.append(eval(i.strip()))
            for i in user_info_list:
                # print(i,type(i),i['username'],i['password'])
                if user_name == i['username'] and hashlib.md5(user_password.encode('utf-8')).hexdigest() == i['password']:
                    # print(hashlib.md5(user_password.encode('utf-8')).hexdigest())
                    print('登录成功')
                    break
                else:
                    print('登录失败，用户名或密码错误')
                    break





if __name__ == '__main__':
    login()