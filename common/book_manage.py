import time


class BookManage(object):
    def __init__(self):
        print('****欢迎进入图书管理系统---图书管理****')


    def add_book(self):
        self.book_name = input('请输入您要增加图书的名称:')
        self.book_author = input('请输入图书的作者：')
        add_time =time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
        book_info = '{"bookname":"%s","book_author":"%s","add_time":"%s"}\n'%(self.book_name,self.book_author,add_time)
        with open('../book_data/book_data.txt','a',encoding='utf-8') as f:
            f.write(book_info)
        print(f'新增图书成功:{book_info}')
        status = input('您是否要继续添加图书-y/n：')
        if status == 'y':
            self.add_book()
            f.close()
        else:
            print('退出当前新增图书模块')
            f.close()

    def find_books(self,book_name):
        with open('../book_data/book_data.txt','r') as f:
            book_list = []
            for i in f.readlines():
                book_list.append(eval(i.strip()))
            print(book_list)
            for i in book_list:
                if book_name == i['bookname']:
                    print(i)
                    continue
                # else:
                #     tips = input('**图书馆没有当前图书**\n您是否要进行添加--yse/no:')
                #     if tips == 'yes':
                #         self.add_book()
                #         break
                #     else:
                #         print('退出添加图书的模块')
                #         break









if __name__ == '__main__':
    a = BookManage()
    # a.add_book()
    a.find_books('西游记')