import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendEmail():
    def SendEmail(self):
        print('邮件发送开始')

        from_addr='kuanghongxia@weseepro.com'
        to_addrs='kuanghongxia@weseepro.com'

        msg=MIMEMultipart()
        #设置邮件正文信息信息，From，To，Subject
        body= MIMEText('接口自动化结果测试邮件','html','utf-8')#3个参数，1为文本内容，2为文本格式，3为编码设置
        msg['from']=Header('接口自动化测试平台','utf-8')
        msg['to']=Header('测试相关人员','utf-8')
        msg['subject']=Header('接口自动化测试结果报告','utf-8')
        msg.attach(body)
        #设置邮件附件信息
        report='F:\\python\\jianshi\\report\\result.html'
        att=MIMEText(open(report,'rb').read(),'base64','utf-8')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment; filename="result.html"'#附件名为中文可能有问题
        msg.attach(att)

        stm=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)

        stm.login("kuanghongxia@weseepro.com","Cd123456")#登录
        stm.sendmail(from_addr,#邮件发送者地址
                          to_addrs,#字符串列表，邮件发送地址
                          msg.as_string()#发送内容

         )#发送
        stm.quit()
        print('邮件发送成功')
if __name__=='__main__':
    SendEmail()
    print('邮件发送成功')