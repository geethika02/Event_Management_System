from datetime import datetime
from tkinter import *
import pytz
from pprint import pprint
from tkinter.constants import GROOVE, TOP, X
import pymsgbox
from typing_extensions import IntVar
from Google import Create_Service, convert_to_RFC_datetime

def time(a,b):
   a=int(a);b=int(b)
   a-=5;b-=30
   if(b<0):
      a-=1
      b+=60
   if(a<0):
      a=-a
      a=24-a
   return a,b


def hi():
   CLIENT_SECRET_FILE = ''#download and insert your own secret file of google calender 
   API_NAME='calendar'
   API_VERSION = 'v3'
   SCOPES = ['https://www.googleapis.com/auth/calendar']

   service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

   syear = sy.get();smon = sm.get();sdate = sd.get()
   eyear=ey.get();emon=em.get();edate=ed.get()
   stime=sh.get(); smin=smi.get(); etime=eh.get(); emin=emi.get()
   event_name=en.get()
   edes=ed1.get()
   
   stime,smin=time(stime,smin)
   etime,emin=time(etime,emin)


   #Create

   calendar_id_party = '' ##insert your own id

   event_request_body = {
      'start': {
      'dateTime': convert_to_RFC_datetime(int(syear),int(smon),int(sdate),int(stime),int(smin)),
      'timeZone': 'Asia/Kolkata',
    },
   'end': {
      'dateTime': convert_to_RFC_datetime(int(eyear),int(emon),int(edate),int(etime),int(emin)),
      'timeZone': 'Asia/Kolkata',
   },
   'summary': event_name,
   'description': edes,
   'colorId': 5,
   'status': 'confirmed',
   'transparency': 'opaque',
   'visibility' : 'public'
   }

   response = service.events().insert(
    calendarId = calendar_id_party,
    body=event_request_body
   ).execute()
   eventId = response['id']

   pymsgbox.alert(text='Your event is created successfully', title='Confirmation',button='OK')



#Update

   # start_datetime = convert_to_RFC_datetime(2020,12,31,17,30)
   # end_datetime =  convert_to_RFC_datetime(2020, 12, 31, 17,59)
   # response['start']['datetime'] = start_datetime
   # response['end']['datetime'] = end_datetime
   # response['summary'] = 'New Year Party'
   # response['description'] = 'Enjoying last day of 2020'
   # service.events().update(
   #    calendarId = calendar_id_party,
   #    eventId = eventId,
   #     body = response
   # ).execute()

#delete
# service.events().delete(calendarId=calendar_id_party, eventId = eventId).execute()



window=Tk()
window.geometry("1080x600")
window.title("Event Calendar")
window.config(bg='#260042')

eventName=StringVar()
eventDes = StringVar()

title=Label(window,text='Event Calendar',border=7,bd=8,relief=GROOVE,font=("algerian",20,"bold"),bg="#b8e6ff").grid(column=2,row=1,padx=10)
# title.pack(side=TOP,fill=X)


Label(window,text='Start Date').grid(row=2)
sy=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
sy.grid(row=2,column=1,padx=20,pady=10)
sm=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
sm.grid(row=2,column=2,padx=30,pady=10)
sd=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
sd.grid(row=2,column=3,padx=20,pady=10)

Label(window,text='Start Time').grid(row=3)
sh=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
sh.grid(row=3,column=1,padx=20,pady=10)
smi=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
smi.grid(row=3,column=2,padx=40,pady=10)

Label(window,text='End Date').grid(row=4)
ey=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
ey.grid(row=4,column=1,padx=20,pady=10)
em=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)    
em.grid(row=4,column=2,padx=40,pady=10)
ed=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
ed.grid(row=4,column=3)

Label(window,text='End Time').grid(row=5)
eh=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
eh.grid(row=5,column=1,padx=20,pady=10)
emi=Entry(window,font=('times new roman',8,"bold"),bd=5,relief=GROOVE)
emi.grid(row=5,column=2,padx=40,pady=10)

Label(window,text='Event Name').grid(row=6)
en=Entry(window,font=('times new roman',8,"bold"),textvariable=eventName,bd=5,relief=GROOVE)
en.grid(row=6,column=1,padx=20,pady=10)

Label(window,text='Event Description').grid(row=7)
ed1 = Entry(window,font=('times new roman',8,"bold"),textvariable=eventDes,bd=5)
ed1.grid(row=7,column=1,pady=10,padx=70)

btn = Button(window,text='Create',height=1,width=12,bg="#fff",fg="#000",command=hi)
btn.grid(row=10,column=5,padx=20,pady=50)

window.mainloop()