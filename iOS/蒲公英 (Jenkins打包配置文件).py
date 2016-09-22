# coding=utf-8


import time
import urllib2
import time
import json
import mimetypes
import os
import smtplib
import datetime

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

#蒲公英应用上传地址
url = 'http://www.pgyer.com/apiv1/app/upload'
#蒲公英提供的用户Key
uKey = 'd226dd05c81a278d649ecc0a5a842713'
#上传文件的文件名（这个可随便取，但一定要以ipa结尾）
file_name = '1.ipa'
#蒲公英提供的 API Key
_api_key = 'f8319609c0fe99283d44605605b4cd4c'
#安装应用时需要输入的密码，这个可不填
installPassword = '123456'

# 运行时环境变量字典
environsDict = os.environ
#此次 jenkins 构建版本号
jenkins_build_number = environsDict['BUILD_NUMBER']

#项目名称，用在拼接tomcat文件地址
project_name = '就医160医生端'

#ipa文件在tomcat服务器上的地址
#ipa_file_tomcat_http_url = 'http://10.1.95.5:8080/' + project_name + '/static/' + jenkins_build_number + '/' + jenkins_build_number + '.ipa'

#获取 ipa 文件路径
def get_ipa_file_path():
    #工作目录下面的 ipa 文件
    ipa_file_workspace_path = '/Users/lisuxia/Desktop/Jenkins/ipa/' + '1' + '.ipa'
    #tomcat 上的 ipa 文件
#    ipa_file_tomcat_path = '/usr/local/tomcat/webapps/' + project_name + '/static/' + jenkins_build_number + '/' + jenkins_build_number + '.ipa'
    print '路径:' + ipa_file_workspace_path

    if os.path.exists(ipa_file_workspace_path):
        return ipa_file_workspace_path
#    elif os.path.exists(ipa_file_tomcat_path):
#        return ipa_file_tomcat_path

#ipa 文件路径
ipa_file_path = get_ipa_file_path()
print ipa_file_path

#请求字典编码
def _encode_multipart(params_dict):
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    for k, v in params_dict.items():
        data.append('--%s' % boundary)
        if hasattr(v, 'read'):
            filename = getattr(v, 'name', '')
            content = v.read()
            decoded_content = content.decode('ISO-8859-1')
            data.append('Content-Disposition: form-data; name="%s"; filename="kangda.ipa"' % k)
            data.append('Content-Type: application/octet-stream\r\n')
            data.append(decoded_content)
        else:
            data.append('Content-Disposition: form-data; name="%s"\r\n' % k)
            data.append(v if isinstance(v, str) else v.decode('utf-8'))
    data.append('--%s--\r\n' % boundary)
    return '\r\n'.join(data), boundary

#处理 蒲公英 上传结果
def handle_resule(result):
    json_result = json.loads(result)
    if json_result['code'] is 0:
        send_Email(json_result)

#发送邮件
def send_Email(json_result):
    appName = json_result['data']['appName']
    appKey = json_result['data']['appKey']
    appVersion = json_result['data']['appVersion']
    appBuildVersion = json_result['data']['appBuildVersion']
    appShortcutUrl = json_result['data']['appShortcutUrl']
    #邮件接受者
    mail_receiver = ['linjing@91160.com','zhuanghm@91160.com','duzeguang@91160.com','wurx@91160.com','wangweihua@91160.com','liuhaibin@91160.com','lilijun@91160.com','chentt@91160.com','guantp@91160.com','lishx@91160.com','xuequan@91160.com','yuezhx@91160.com','liguozhong@91160.com','yugq@91160.com','luobin@91160.com','lujun@91160.com','liuqichao@91160.com','lijr@91160.com','litaoran@91160.com','qiuju@91160.com','fangfang@91160.com']
    #mail_receiver = ['lishx@91160.com']
    #根据不同邮箱配置 host，user，和pwd
    mail_host = 'smtp.exmail.qq.com:465'
    mail_user = 'ios@91160.com'
    mail_pwd = 'ningYuan2016A'
    mail_to = ','.join(mail_receiver)

    msg = MIMEMultipart()

    environsString = '<h3>医生端iOS安装包</h3><p>'
    #environsString += '<p>ipa 包下载地址 : ' + ipa_file_tomcat_http_url + '<p>'
    environsString += '<p>蒲公英网站在线安装 : ' + 'http://www.pgyer.com/' + str(appShortcutUrl) + '   密码 : ' + installPassword + '<p>'
    environsString += '<li><a href="itms-services://?action=download-manifest&url=https://ssl.pgyer.com/app/plist/' + str(appKey) + '">点我直接安装</a></li>'
    message = environsString
    body = MIMEText(message, _subtype='html', _charset='utf-8')
    msg.attach(body)

    msg['To'] = mail_to
    msg['from'] = mail_user
    #获得当前时间
    now = datetime.datetime.now()  #这是时间数组格式
    #转换为指定的格式
    otherStyleTime = now.strftime("%Y%m%d")
    #邮件主题
    msgSubject = 'iOS' + '_' + otherStyleTime + '_' + jenkins_build_number +'安装包'
    msg['subject'] = msgSubject

    try:
        s = smtplib.SMTP_SSL()  #使用SMTP_SSL()
        s.connect(mail_host)
        s.login(mail_user, mail_pwd)
        s.sendmail(mail_user, mail_receiver, msg.as_string())
        s.close()
        print '发送邮件成功'
    except Exception, e:
        print e

#############################################################
#请求参数字典
params = {
    'uKey': uKey,
    '_api_key': _api_key,
    'file': open(ipa_file_path, 'rb'),
    'publishRange': '2',
    'password': installPassword
}

coded_params, boundary = _encode_multipart(params)
req = urllib2.Request(url, coded_params.encode('ISO-8859-1'))
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
try:
    resp = urllib2.urlopen(req)
    body = resp.read().decode('utf-8')
    handle_resule(body)
except urllib2.HTTPError as e:
    print(e.fp.read())
