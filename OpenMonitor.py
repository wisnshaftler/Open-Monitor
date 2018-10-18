import socket
import smtplib

print ("Thank you for using OpenMonitor \n")
print ("Starting....\n")

#creating variables
print ("creating runtime variables....\n")
email = senderemail = ip = senderpass = smtpserver =""
loop = port = emailport=1

#open file and pass the values to variables
with open('config.txt', 'r+') as f:
    for line in f.readlines():
        data = line.split(": ",1)[1]
        if loop ==1:
            email = data.rstrip('\n')
            loop +=1
        elif loop == 2:
            port = int(data)
            loop += 1
        elif loop == 3:
            ip = data.rstrip('\n')
            loop +=1
        elif loop ==4 :
            emailport = int(data)
            loop +=1
        elif loop ==5:
            senderemail = data.rstrip('\n')
            loop += 1
        elif loop ==6:
            senderpass =data.rstrip('\n')
            loop +=1
        elif loop ==7:
            smtpserver = data.rstrip('\n')
            loop +=1

#print default values to user
fo = open("config.txt",'r+')
readtext = fo.read()
print ("This is your default configurations. You can change this by changing config.txt file. *note plese dont remove space after : mark ","\n")
print (readtext,"\n")
#create function for send emails
def emailfunc (emails,msg):
    server = smtplib.SMTP_SSL(smtpserver, emailport)
    server.login(senderemail, senderpass)
    server.sendmail(
        senderemail,
        emails,
        'Subject: {}\n\n{}'.format("syslog nofitication", msg))
    server.quit()
    print ("*** email has been sent ***","\n")
    
#create udp socket listner
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))

#infinity loop for listning
print ("Server listening started!","\n")
while True:
    data, addr = sock.recvfrom(1024)
    print (addr , (data.decode("utf-8")).split(": ",1)[1] ,"\n")

    #send email
    emailfunc(email, (addr , (data.decode("utf-8")).split(": ",1)[1] ,))
