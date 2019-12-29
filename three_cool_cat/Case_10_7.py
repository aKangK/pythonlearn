import json
import sys

def saveToJSON(filename,dicObject):
#定义写入JSON函数
    flag=False
    if type(dicObject)!=dict:
        return flag
    try:
        j_file=open(filename,'w')
        json.dump(dicObject,j_file,ensure_ascii=False)
        flag=True
    except:
        print('往%s写数据出错！'%(filename))
    finally:
        if flag:
            j_file.close()
    return flag
#=================================================
def getFromJSON(filename):
#定义读取JSON函数
    flag=False
    dicObject={}
    try:
        j_file=open(filename,'r')
        dicObject=json.load(j_file)
        flag=True
    except:
        print('从%s读取JSON数据错误！'%(filename))
    finally:
        if flag:
            j_file.close()
    return dicObject
#======================================================
d_student={'name':'丁丁','age':'12','birthday':'2006年12月25日'}
filename='student.json'
f_OK=saveToJSON(filename,d_student)
if f_OK:
    print('学生信息保存至JSON成功！')
else:
    sys.exit()
d_get_s=getFromJSON(filename)
if d_get_s:
    print(d_get_s)
