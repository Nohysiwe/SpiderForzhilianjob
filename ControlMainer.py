#coding:utf-8
from Dowloader import Dowload
from Parser import Parse
from ToSaveFiler import ToSaveFile
import time
import random
import csv
class ControlMain(object):

    def __init__(self):
        self.Dowload = Dowload()
        self.Parse = Parse()
        self.ToSaveFile = ToSaveFile()
        self.info_lis = [u'职位月薪',u'工作地点',u'发布日期',u'工作性质',u'工作经验',u'最低学历',u'招聘人数',u'职位类别',u'公司名称',u'公司规模',u'公司性质',u'公司行业',u'公司主页',u'公司地址']





        '''
        
            整个爬虫的调度函数
        
        '''

    def control_main(self,city, keyword, need_pages, in_sg = '4c07fc8dd08a43329a538ac5ce11423f', page = 1, region=None):

        jobs_info_urls_lis = []


        # 特别说明下这里，计算机系统默认的中文编码是gb2312得文件命名的时候改下，但是我的文件里面内容是utf-8编码格式
        keyword2 = keyword.decode('utf-8').encode('gb2312')

        city2 = city.decode('utf-8').encode('gb2312')

        url_csv_name = '%s_%s_urls.csv'%(keyword2,city2)

        job_csv_name = '%s_%s.csv'%(keyword2,city2)

        first_page_response = self.Dowload.get_url_page(city,keyword,in_sg,page,region)

        keyword_pages,first_page_show_urls = self.Parse.parse_url_page(first_page_response)


        #for url in first_page_show_urls:

        get_save_urls_info = self.ToSaveFile.save_to_csv(url_csv_name, first_page_show_urls)

        if not get_save_urls_info:
            return False
            print '第一页无urls'

        if keyword_pages == 0:
            return False
            print '查询无此相关的招聘信息'

        if keyword_pages < need_pages:
            need_pages = keyword_pages
            print '抱歉该相关的招聘信息数量只有%s页' %need_pages

        get_save_jobs_info = self.ToSaveFile.save_to_csv(job_csv_name,self.info_lis)


        #将所有的urls保存进文件

        for i in range(2,need_pages+1):
            time.sleep(random.uniform(2,3))
            try:

                page_response = self.Dowload.get_url_page(city,keyword,in_sg,i,region)

                keyword_pages,page_show_urls = self.Parse.parse_url_page(page_response)

                #for url in page_show_urls:

                get_save_urls_info = self.ToSaveFile.save_to_csv(url_csv_name, page_show_urls)

            except Exception as e :

                print '好像其中某一次录入urls失败了（%s）'%str(e)

                continue


        #读取jobs详细信息页面的url
        with open(url_csv_name,'rb') as f:

            reader =csv.reader(f)

            for i in reader:
                jobs_info_urls_lis.append(i)


        #将每页的job详细信息保存到文件
        for i in jobs_info_urls_lis:

            for j in i:
                time.sleep(random.uniform(2, 3))
                try:

                    job_page_response = self.Dowload.get_text_page(j)

                    job_page_show_info = self.Parse.parse_text_page(job_page_response)

                    get_save_jobs_info = self.ToSaveFile.save_to_csv(job_csv_name,job_page_show_info)

                except Exception as e:

                    print '好像其中某一次录入job信息失败了（%s）' % str(e)
                    continue


        return '结束了'










