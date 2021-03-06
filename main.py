from tkinter import *
import requests
import tkinter.font as tkFont
from bs4 import BeautifulSoup
class Main(object):
    def __init__(self):
        self.Setup()
        self.Widgets()
        self.Loop()
    def Setup(self):
        self.Root=Tk()
        self.Root.title("感測器控制平台")
        #self.Root.geometry("250x250")
        self.tempVar=StringVar()
        self.tempVar.set("offline")
        self.humiVar=StringVar()
        self.humiVar.set("offline")
        self.distVar=StringVar()
        self.distVar.set("offline")
        self.Font=tkFont.Font(family="helvetica",size=20)
        self.rVar=IntVar()
        self.rVar.set(0)
        self.gVar=IntVar()
        self.gVar.set(0)
        self.bVar=IntVar()
        self.bVar.set(0)
        self.baseurl="192..168.4.1"
    def Widgets(self):
        self.Labels=[]
        self.Buttons=[]
        self.Scales=[]
        self.Labels.append(Label(self.Root,text="接收資料",font=self.Font,fg="red",relief="solid"))
        self.Labels[-1].grid(row=0,column=0,columnspan=3,sticky=W+E)
        self.Labels.append(Label(self.Root,text="  溫度  ",font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=1,column=0,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,text="  濕度  ",font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=1,column=1,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,text="  距離  ",font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=1,column=2,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,textvariable=self.tempVar,font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=2,column=0,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,textvariable=self.humiVar,font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=2,column=1,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,textvariable=self.distVar,font=self.Font,relief="solid"))
        self.Labels[-1].grid(row=2,column=2,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,text="開關控制",font=self.Font,fg="green",relief="solid"))
        self.Labels[-1].grid(row=3,column=0,columnspan=3,sticky=W+E)
        self.ButtonFrame=Frame(self.Root)
        self.ButtonFrame.grid(row=4,column=0,columnspan=3,sticky=W+E)
        self.Buttons.append(Button(self.ButtonFrame,text="電源ON",command=self.onmain,bg="green",font=self.Font,relief="solid"))
        self.Buttons[-1].grid(row=0,column=0,columnspan=1,sticky=W+E)
        self.Buttons.append(Button(self.ButtonFrame,text="蜂鳴器ON",command=self.onbuzz,bg="green",font=self.Font,relief="solid"))
        self.Buttons[-1].grid(row=0,column=1,columnspan=1,sticky=W+E)
        self.Buttons.append(Button(self.ButtonFrame,text="電源OFF",command=self.offmain,bg="red",font=self.Font,relief="solid"))
        self.Buttons[-1].grid(row=1,column=0,columnspan=1,sticky=W+E)
        self.Buttons.append(Button(self.ButtonFrame,text="蜂鳴器OFF",command=self.offbuzz,bg="red",font=self.Font,relief="solid"))
        self.Buttons[-1].grid(row=1,column=1,columnspan=1,sticky=W+E)
        self.Labels.append(Label(self.Root,text="RGB控制",font=self.Font,fg="blue",relief="solid"))
        self.Labels[-1].grid(row=5,column=0,columnspan=3,sticky=W+E)
        self.Scales.append(Scale(self.Root,variable=self.rVar,command=lambda x : self.updatergb(1,self.rVar.get()),from_=0,to=255,orient=HORIZONTAL,relief="solid",label="紅："))
        self.Scales[-1].grid(row=6,column=0,columnspan=3,sticky=W+E)
        self.Scales.append(Scale(self.Root,variable=self.gVar,command=lambda x : self.updatergb(2,self.gVar.get()),from_=0,to=255,orient=HORIZONTAL,relief="solid",label="綠："))
        self.Scales[-1].grid(row=7,column=0,columnspan=3,sticky=W+E)
        self.Scales.append(Scale(self.Root,variable=self.bVar,command=lambda x : self.updatergb(3,self.bVar.get()),from_=0,to=255,orient=HORIZONTAL,relief="solid",label="藍："))
        self.Scales[-1].grid(row=8,column=0,columnspan=3,sticky=W+E)
        self.Root.resizable(0,0)
    def Loop(self):
        self.Root.after(200,self.updateinfo)
        self.Root.mainloop()
    def updateinfo(self):
        print("updateinfo")
        respond=requests.get("http://192.168.4.1/value.html")
        bs4=BeautifulSoup(respond.text,"lxml")
        
        self.tempVar.set(bst.find)
        self.Root.after(200,self.updateinfo)
    def onmain(self):
        print("onmain")
        try:
            requests.get("http://192.168.4.1/r1on.html")
        except(requests.exceptions.ConnectionError):
            pass
    def offmain(self):
        print("offmain")
        try:
            requests.get("http://192.168.4.1/r1off.html")
        except(requests.exceptions.ConnectionError):
            pass
    def onbuzz(self):
        print("onbuzz")
        try:
            requests.get("http://192.168.4.1/r2on.html")
        except(requests.exceptions.ConnectionError):
            pass
    def offbuzz(self):
        print("offbuzz")
        try:
            requests.get("http://192.168.4.1/r2off.html")
        except(requests.exceptions.ConnectionError):
            pass
    def updatergb(self,pin,value):
        try:
            requests.get("http://192.168.4.1/color{}={}".format(pin,value))
        except(requests.exceptions.ConnectionError):
            pass
if __name__=="__main__":
    Main()