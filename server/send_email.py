import smtplib
from email.mime.text import MIMEText
from email.header import Header


def alert(useraddr):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # password = raw_input('Type in your email password:')
    #password = getpass.getpass("Type in your email password: ")
    password = '1234567890s'
    sender = 'lhyemailsender@gmail.com'
    server.login(sender, password)

    message = '''\
    <html>
        <h1>Insecure Device Connected to your Network</h1>
        <h2>We blocked the device's Internet access</h2>
        <p> To change this setting visit the following page </p>
        <a href = 'http://192.168.2.1:5000/'> My router: http://192.168.2.1:5000/ </a>
    </html>
    '''
    # msg = MIMEText('FAIL to find a MUD for this device', 'plain', 'utf-8')
    msg = MIMEText(message, 'html')

    msg['Subject'] = Header('Alert from router', 'utf-8')
    msg['From'] = sender
    msg['To'] = useraddr
    try:
        server.sendmail(sender, useraddr, msg.as_string())
        print 'email sended'
    except:
        print 'fail to send email'
    finally:
        server.quit()



def case_two_alert(useraddr, matches, fileName):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # password = raw_input('Type in your email password:')
    #password = getpass.getpass("Type in your email password: ")
    password = '1234567890s'
    sender = 'lhyemailsender@gmail.com'
    server.login(sender, password)

    message = '''\
    <html>
       <h1> Hi, A new device joined your network!</h1>
       <h2> We believe it is a(n) {fileN}. Do you recoggnize this device?</h2>
       <p> Visit the following page to permit/block the device's usage </p>
       <a href = 'http://192.168.2.1:5000/?guess={guess}'> My router http://192.168.2.1:5000/?guess={guess} </a>
    </html>
    '''.format(fileN = fileName, guess = fileName)

    msg = MIMEText(message, 'html')

    msg['Subject'] = Header('Alert from router', 'utf-8')
    msg['From'] = sender
    msg['To'] = useraddr
    try:
        server.sendmail(sender, useraddr, msg.as_string())
        print 'email sended'
    except:
        print 'fail to send email'
    finally:
        server.quit()
