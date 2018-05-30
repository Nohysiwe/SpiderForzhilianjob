#coding:utf-8
from ControlMainer import ControlMain
if __name__ == '__main__':
    lis = [  '杭州', '重庆', '南京', '天津', '青岛', '大连',
           '宁波']
    a= ControlMain()
    for i in lis :
        b = a.control_main(i,'软件工程师',100)
        print b