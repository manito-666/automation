#执行excel用例直接在文档中生成结果写入，可以查看excel报告
# coding:utf-8
import os,json,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from util.data.Excelread import read_data,count_case,write_data
from config.log.mylog import log
from config.configHttp import ConfigHttp,RunMain
from config.readconfig import R

excelpath='/Users/wangzhipeng/PycharmProjects/automation/util/data/result.xlsx'
#从Excel读取到多条测试数据
def runn(path,sheets):
    r=RunMain()
    testdata=[]
    for sheet1 in sheets:
        max_row=count_case(sheet1,excelpath)
        for case_id in range(1,max_row):
            data=read_data(sheet1,path,case_id)
            title=data[3]
            method = data[4]
            url=ConfigHttp().set_url(data[9])
            datas = data[7]
            # headers=ConfigHttp.set_headers(R.get_http('headers'))
            headers=json.loads(R.get_http('headers'))
            r.request_log(method=method, url=url, datas=datas, headers=headers,title=title)
            rep = r.run_main(method=method,url=url,datas=datas,headers=headers).json()
            log.info('响应结果为:' + str(rep))
            # 将测试实际结果写入excel
            write_data(sheet1, case_id + 1, 12, rep['error_msg'])
            write_data(sheet1, case_id + 1, 8, str(rep))
            # 对比测试结果和期望结果
            if rep['error_msg'] == str(data[10]):
                log.info('测试通过')
                # 将用例执行结果写入Excel
                write_data(sheet1, case_id + 1, 10, 'Pass')
            else:
                write_data(sheet1, case_id + 1, 10, 'Fail')
                log.error('测试失败')
            testdata.append([method, url, datas, headers])
    return testdata

if __name__ == '__main__':
    runn(excelpath, ['sheet'])





#初始数据为test.xlsx,测试生成数据为result.xlsx

# def copy_excel(excelpath1, excelpath2):
#     '''复制excek，把excelpath1数据复制到excelpath2'''
#     wb2 = openpyxl.Workbook()
#     wb2.save(excelpath2)
#     # 读取数据
#     wb1 = openpyxl.load_workbook(excelpath1)
#     wb2 = openpyxl.load_workbook(excelpath2)
#     sheets1 = wb1.sheetnames
#     sheets2 = wb2.sheetnames
#     sheet1 = wb1[sheets1[0]]
#     sheet2 = wb2[sheets2[0]]
#     max_row = sheet1.max_row  # 最大行数
#     max_column = sheet1.max_column  # 最大列数
#
#     for m in list(range(1, max_row + 1)):
#         for n in list(range(97, 97 + max_column)):  # chr(97)='a'
#             n = chr(n)  # ASCII字符
#             i = '%s%d' % (n, m)  # 单元格编号
#             cell1 = sheet1[i].value  # 获取data单元格数据
#             sheet2[i].value = cell1  # 赋值到test单元格
#
#     wb2.save(excelpath2)  # 保存数据
#     wb1.close()  # 关闭excel
#     wb2.close()
#
#
#
# if __name__ == '__main__':
#     copy_excel('./text.xlsx','./result.xlsx')