#!/usr/bin/env python
#coding=utf-8
import sys
import smtplib
import datetime
import threading
from dateutil.parser import parse

def sendMail(date):
    subject = sys.argv[4].decode("utf-8").replace("__", " ").replace("_ue", u"ü").replace("_Ue", u"Ü").replace("_ae", u"ä").replace("_Ae", u"Ä").replace("_oe", u"ö").replace("_Oe", u"Ö").replace("_ss", u"ß")
    username = sys.argv[5]
    password = sys.argv[6].decode("utf-8").replace("__", " ")
    fromaddr = username
    toaddr  = sys.argv[1]
    msgText = sys.argv[7].decode("utf-8").replace("__", " ").replace("[date]", date).replace("<br>", "\r\n").replace("_ue", u"ü").replace("_Ue", u"Ü").replace("_ae", u"ä").replace("_Ae", u"Ä").replace("_oe", u"ö").replace("_Oe", u"Ö").replace("_ss", u"ß")
    #print(u"%s" % (msgText))

    msg = u"\r\n".join([
      "From: ".join(fromaddr),
      "To: ".join(toaddr),
      "Subject: " + subject,
      "",
      msgText
      ])

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
    except:
        print("Login failed.")
    try:
        server.sendmail(fromaddr, toaddr, msg.encode("utf-8"))
        server.quit()
        print("Email for the " + date + " was sent successfully.")
    except:
        print("Email for the " + date + " could not be sent.")

def checkDate():
    datesToClear = []
    for date in dates:
        a = parse(date)
        b = datetime.datetime.now()
        delta = a-b
        if delta.days <= daysBefore and delta.days > 0:
            dateArr = date.split('-')
            dateStr = dateArr[2] + "." + dateArr[1] + "." + dateArr[0]
            sendMail(dateStr)
            datesToClear.append(date)
    for date in datesToClear:
        dates.remove(date)
    if len(dates) == 0:
        return
    #threading.Timer(3600, checkDate).start ()

daysBefore = int(sys.argv[3])
dates = sys.argv[2].split(",")
checkDate()
