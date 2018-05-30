#coding:utf-8
import csv
class ToSaveFile(object):

    def __init__(self):
        pass


    def reduce_rows(self,lis):
        lis = lis.strip().strip('\r\n').strip('\n')
        return lis.encode('utf-8')
        #最好用gb2312,因为windows系统默认中文系统为gb2312


    '''
       
       将获取信息保存为csv文件
        
    '''
    def save_to_csv(self,path,lis):
        if lis == None:
            return False
        try:

            with open(path,'ab') as f:
                lis = map(self.reduce_rows,lis)
                # print lis
                print 'save success'
                wri = csv.writer(f)
                wri.writerow(lis)

            return True
        except Exception as e:
            print str(e)
            return False

