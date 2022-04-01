# encoding: utf-8
"""
@file: paizhao.py
@version: 1.0
@author: Atlantis
@time: 2020/12/9 18:23
@DESC: 利用电脑摄像头拍照，并通过邮件发送
"""
import time # 获取拍照的时间、开机时间等
import smtplib #用来发送邮件
from email.mime.image import MIMEImage  #可以把图片当成邮件附件发送
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2  # pip install opencv-python


host = "smtp.163.com" # 发邮件的服务器接口
port = 25
sender = 'gooonepiece@163.com' # 邮件的发送方
pwd = 'FQIBPADQMMGEMSCS' #授权码
receiver = 'gooonepiece@126.com' # 邮件的接收方
path = 'D:'


def GetPicture():
    #cv2.namedWindow('camera') # 打开windows窗口
    #开启ip摄像
    # video = 'http://admin:admin@192.168.1.4:8081/video'
    # 电脑摄像头的话，不要video，直接用传入0
    cap = cv2.VideoCapture(0) # 打开摄像头
    ret,frame = cap.read(0) # 产生窗口、图片
    cv2.imwrite(path + '/person.jpg',frame) # 把图片写入路径
    cap.release()# 摄像头关闭





def SetMsg():
    msg = MIMEMultipart('mixed') # 添加附件
    #标题
    msg['Subject'] = '小姐姐图片'
    msg['From'] = sender
    msg['To'] = receiver

    #邮件正文内容
    text = "你的小姐姐到了,请接收"
    text_plain = MIMEText(text,'plain','utf-8') # 文本消息转码（把传输的二进制数转为utf-8）
    msg.attach(text_plain) # 把消息插入到邮件

    #图片
    SendImageFile = open(path + '/person.jpg','rb').read() # 获取图片数据
    image = MIMEImage(SendImageFile) # 图片转码（转为人类能识别的）

    #将收件人看见的附件照片名称改为people.png（即改一下邮件里的图片名字）
    image['Content-Disposition'] = 'attachment;filename = "people.jpg"'
    msg.attach(image)
    return msg.as_string()# 把消息作为字符串返回

# 发送邮件
def SendEmail(msg):
    smtp = smtplib.SMTP() # 实例化发邮件对象
    smtp.connect(host) # 对象连接服务器
    smtp.login(sender,pwd) # 登录服务器输入账户名、密码
    smtp.sendmail(sender,receiver,msg) # 发送邮件 sendmail(从哪发，往哪发，邮件内容)
    time.sleep(2) # 发送有延迟，停两秒再退出
    smtp.quit()

if __name__ == '__main__':
    #先拍照
    GetPicture()
    #设置邮件格式
    msg= SetMsg()
    #发送邮件
    SendEmail(msg)

