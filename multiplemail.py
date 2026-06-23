import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)#server name and port number
ob.ehlo()
ob.starttls()
ob.login('your_email@gmail.com', 'your_password')#login credentials
subject="test mail"
body="this is a test mail"
message="subject:{}\n\n{}".format(subject,body)
listaddress=['email1@gmail.com','email2@gmail.com','email3@gmail.com']
ob.sendmail('your_email@gmail.com',listaddress,message)
print("mail sent sucessfully ")
ob.quit()