import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


def spider():
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    url = "http://www.66ys.co/"
    response = session.get(url)
    with open("66e.html", "wb") as f:
        f.write(response.content)


def sendMail():
    # 初始化
    email_host = 'smtp.163.com'
    email_user = 'w1259337898@163.com'
    email_pass = 'TAJNIMTRWREBKHUB'
    sender = 'w1259337898@163.com'
    receivers = ['1259337898@qq.com', '2558739764@qq.com']

    # 创建MIMEMultipart对象
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ";".join(receivers)
    message["Subject"] = "致亲爱的蒙蒙"

# 正文
    content = "牛啊，蒙蒙！！！"
    part1 = MIMEText(content, "plain", "utf-8")
    # with open("Python思维导图.xmind", "rb") as f:
    #     content2 = f.read()
    # part2 = MIMEApplication(content2)
    # part2["Content-Type"] = "application/octet-stream"
    # part2.add_header("Content-Disposition", "attachment", filename=("gbk", '', "Python思维导图.xmind"))

    message.attach(part1)
    # message.attach(part2)

# 发送
    try:
        # receivers = receivers + [sender]
        email_smtp = smtplib.SMTP()
        email_smtp.connect(email_host, 25)
        email_smtp.login(email_user, email_pass)
        email_smtp.sendmail(sender, receivers, message.as_string())
        print("success!")
    except smtplib.SMTPException as e:
        print("error", e)


if __name__ == '__main__':
    # spider()
    sendMail()
