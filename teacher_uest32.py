'''
时间：2018年2月4日
作者：Jason
目标：爬取电子科技大学导师
版本：3.2
功能：所有导师的详细信息,加入代理IP,并存入mysql中
'''

import requests
from  bs4 import BeautifulSoup
import time
import pymysql

def teacher_urls():
    url1 = 'http://222.197.183.99/TutorList.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    res = requests.get(url1, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    target = soup.find_all('div', style="height: 16px; width: 100px; float: left")
    teacher_url = []

    for each in target:
        teacher_url.append(each.a['href'])
    return teacher_url

def teacher_information():
    teacher_url1 = teacher_urls()
    time.sleep(10)

    db = pymysql.connect("localhost", "root", "626626", "uest", charset="utf8")
    cursor = db.cursor()
    cursor.execute("drop table if exists teacher")
    sql = """create table teacher(
                     college_ID1 text,
                     college1 text,
                     teacher_ID1 text,
                     teacher_name1 text,
                     teacher_sex1 text,
                     teacher_birth1 text,
                     teacher_glory1 text,
                     teacher_position1 text,
                     teacher_degree1 text,
                     teacher_attribute1 text,
                     teacher_email11 text,
                     teacher_experience1 text,
                     teacher_introduce1 text,
                     teacher_research1 text,
                     teacher_article1 text,
                     teacher_doctor_id1 text,
                     teacher_doctor_name1 text,
                     teacher_master_id1 text,
                     teacher_master_name1 text)"""
    cursor.execute(sql)
    print("\n creat table successd ! \n")
    db.close()
.
    for i in teacher_url1:
        time.sleep(180)
        url2 = 'http://222.197.183.99/' + str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        res = requests.get(url2, timeout=10, headers=headers)
        s = requests.Session()
        s.cookies['cookie-name'] = 'cookie-value'
        soup = BeautifulSoup(res.text, 'html.parser')
        target = soup.find_all("span")
        result = [span.get_text() for span in target]
        college_ID = result[19]  # 学院ID
        college = result[20]  # 学院
        teacher_ID = result[21]  # 导师代码
        teacher_name = result[22]  # 导师姓名
        teacher_sex = result[23]  # 性别
        teacher_birth = result[24]  # 出生年月
        teacher_glory = result[25]  # 特称
        teacher_position = result[26]  # 职称
        teacher_degree = result[27]  # 学位
        teacher_attribute = result[28]  # 属性
        teacher_email = result[29]  # 电子邮件
        teacher_experience = result[30]  # 学术经历
        teacher_introduce = result[31]  # 个人简介
        teacher_research = result[32]  # 科研项目
        teacher_article = result[33]  # 发表文章
        teacher_doctor_id = result[34]  # 博士招生ID
        teacher_doctor_name = result[35]  # 博士专业
        teacher_master_id = result[34]  # 硕士招生ID
        teacher_master_name = result[35]  # 硕士专业

        db = pymysql.connect("localhost", "root", "626626", "uest", charset="utf8")
        cursor = db.cursor()
        sqls = """insert into teacher(college_ID1,college1,teacher_ID1,teacher_name1,teacher_sex1,teacher_birth1,teacher_glory1,teacher_position1,teacher_degree1,teacher_attribute1,teacher_email11,teacher_experience1,teacher_introduce1,teacher_research1,teacher_article1,teacher_doctor_id1,teacher_doctor_name1,teacher_master_id1,teacher_master_name1)
                                  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
        college_ID, college, teacher_ID, teacher_name, teacher_sex, teacher_birth, teacher_glory, teacher_position,
        teacher_degree, teacher_attribute, teacher_email, teacher_experience, teacher_introduce, teacher_research,
        teacher_article, teacher_doctor_id, teacher_doctor_name, teacher_master_id, teacher_master_name)
        try:
            cursor.execute(sqls)
            db.commit()
            print('提交成功')
        except:
            db.rollback()
            print('\n Some Error happend ! \n')
        db.close()

        print(teacher_name)
if __name__ == '__main__':
    teacher_information()
