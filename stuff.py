from tkinter import *   
from escpos.printer import Usb
import random
import datetime

date = datetime.datetime.now()

nextBusTime = 1

almostThere = 0

timeThatItCurrentlyIsYee = ("00:00")

printer = Usb(0x04b8, 0x0e15, 0)

def blankLineForSpacing():
    printer.set(align="center", underline=1, width=1, height=1)
    printer.text("                                                \n")

def timeCalculator() :
    almostThere = int(date.strftime("%M"))
    print(almostThere)
    almostThere += 15
    print(almostThere)
    wowWeHadToChangeTheTime = int(date.strftime("%H"))
    if int(almostThere) > 44:
        wowWeHadToChangeTheTime += 1
        ffs = int(almostThere) - 60
        if ffs > 10:
            timeThatItCurrentlyIsYee = str(ffs)
            timeThatItCurrentlyIsYee = str(ffs).zfill(2)
            almostThere = timeThatItCurrentlyIsYee

    if wowWeHadToChangeTheTime == 24:
        wowWeHadToChangeTheTime = 0
        wowWeHadToChangeTheTime = str(wowWeHadToChangeTheTime).zfill(2)
    
    nextBusTime = str(str(wowWeHadToChangeTheTime) + ":" + str(ffs))
    return nextBusTime

def printForUtkarsh(place, price, type, busNumber, time) :
    timeThatTheBusActuallyComes = time
    newPriceBecauseNoOneLikesZero = '£{:,.2f}'.format(price)
    number = random.randint(1000000, 9999999)
    currentDate = date.strftime("%d/%m/%y")
    aaaaaa = date.strftime("%d%m%y")
    rrreeeeeeee = (date.strftime("%d%m%y") + str(number))
    
    printer.image("printmersey.png", center=True)
    blankLineForSpacing()
    printer.set(align="left", underline=0, width=2, height=2, custom_size=True)
    printer.text("Location: " + place + "\n")
    printer.text("Price: " + str(newPriceBecauseNoOneLikesZero) + "\n")
    printer.text("Date: " + currentDate + "\n")
    printer.text("Type: " + type + "\n")
    printer.text("Bus Number: " + str(busNumber) + "\n")
    printer.text("Bus Arrives At: " + str(timeThatTheBusActuallyComes) + "\n")
    blankLineForSpacing()
    printer.set(align="left", underline=0, width=2, height=2, custom_size=True)
    printer.barcode(rrreeeeeeee, 'EAN13', 64, 5, '', '')
    printer.cut()

    
window = Tk() 

window.configure(padx = 15, pady = 15, background='#2f2f2f') #window setup stuff

mapImg1 = PhotoImage(file="Picture1.png")  #map setup stuff
mapImg1 = mapImg1.zoom(25)
mapImg1 = mapImg1.subsample(50)

mapImg2 = PhotoImage(file="Picture2.png")  
mapImg2 = mapImg2.zoom(25)
mapImg2 = mapImg2.subsample(50)

mapImg3 = PhotoImage(file="Picture3.png")  
mapImg3 = mapImg3.zoom(25)
mapImg3 = mapImg3.subsample(50) 

#Row 1
b1 = Button(window)

b2 = Button(window)

b3 = Button(window)
#Row 2
b4 = Button(window)

b5 = Button(window)

b6 = Button(window)

#Row 3
b7 = Button(window)

b8 = Button(window)

b9 = Button(window)

#Row 4
b10 = Button(window)

b11 = Button(window)

b12 = Button(window)

def stations():

    window.configure(padx = 15, pady = 15, background='#2f2f2f')
       
    wirralMap1 = Label(window, image = mapImg1)   
    wirralMap1.grid(column = 0, row = 1, padx=0, pady=0)  

       
    wirralMap1 = Label(window, image = mapImg2)   
    wirralMap1.grid(column = 1, row = 1,) 

     
    wirralMap1 = Label(window, image = mapImg3)   
    wirralMap1.grid(column = 2, row = 1,)

    #1
    t1=timeCalculator()
    b1.configure(text="Heswall Station" + t1)
    b1.grid(column = 0, row = 2,  pady=10, command=printForUtkarsh("Heswall Bus Station", 1.50, "Single", 471,t1))

    t2=timeCalculator()
    b2.configure(text="Boathouse Lane" + t2)
    b2.grid(column = 1, row = 2,  pady=10, command=printForUtkarsh("Boathouse Lane", 1.50, "Single", 471,t2)) 

    t3=timeCalculator()
    b3.configure(text="Telegraph Road" + t3)
    b3.grid(column = 2, row = 2,  pady=10, command=printForUtkarsh("Telegraph Road", 1.50, "Single", 471,t3))
    #2
    t4=timeCalculator()
    b4.configure(text="Gayton Lane" + t4)
    b4.grid(column = 0, row = 3,  pady=10, command=printForUtkarsh("Gayton Lane", 1.50, "Single", 471,t4))
    
    t5=timeCalculator()
    b5.configure(text="Banks Road" + t5)
    b5.grid(column = 1, row = 3,  pady=10, command=printForUtkarsh("Banks Road", 1.50, "Single", 471,t5))

    t6=timeCalculator()
    b6.configure(text="Barnston Road" + t6)
    b6.grid(column = 2, row = 3,  pady=10, command=printForUtkarsh("Barnston Road", 1.50, "Single", 471,t6))
    #3
    t7=timeCalculator()
    b7.configure(text="Beacon Lane" + t7)
    b7.grid(column = 0, row = 4,  pady=10, command=printForUtkarsh("Beacon Lane", 1.50, "Single", 471,t7))

    t8=timeCalculator()
    b8.configure(text="Broomlads" + t8)
    b8.grid(column = 1, row = 4,  pady=10, command=printForUtkarsh("Broomlands", 1.50, "Single", 471,t8))

    t9=timeCalculator()
    b9.configure(text="Whitfield Lane" + t9)
    b9.grid(column = 2, row = 4,  pady=10, command=printForUtkarsh("Whitfield Lane", 1.50, "Single", 471,t9))
    #4
    t10=timeCalculator()
    b10.configure(text="Riverbank Road" + t10)
    b10.grid(column = 0, row =5,  pady=10, command=printForUtkarsh("Riverbank Road", 1.50, "Single", 471,t10))

    t11=timeCalculator()
    b11.configure(text="School Hill" + t11)
    b11.grid(column = 1, row = 5,  pady=10, command=printForUtkarsh("School Hill", 1.50, "Single", 471,t11))

    t12=timeCalculator()
    b12.configure(text="Pipers" + t12)
    b12.grid(column = 2, row = 5,  pady=10, command=printForUtkarsh("Pipers", 1.50, "Single", 471, t12))

    

def start():
    window.configure(padx=100,pady=100)
    start = Button(window, text="Press Here to Start", command=menu)
    start.grid(column = 0, row = 1, padx=0, pady=0)

def menu():

    window.configure(padx = 15, pady = 15, background='#2f2f2f')
       
    wirralMap1 = Label(window, image = mapImg1)   
    wirralMap1.grid(column = 0, row = 1, padx=0, pady=0)  

       
    wirralMap1 = Label(window, image = mapImg2)   
    wirralMap1.grid(column = 1, row = 1,) 

     
    wirralMap1 = Label(window, image = mapImg3)   
    wirralMap1.grid(column = 2, row = 1,)
    #1  
    b1.configure(text="Wallasey")
    b1.grid(column = 0, row = 2,  pady=10)

    b2.configure(text="Heswall", command=stations)
    b2.grid(column = 1, row = 2,  pady=10) 

    b3.configure(text="Barnston")
    b3.grid(column = 2, row = 2,  pady=10)
    #2
    b4.configure(text="Birkenhead")
    b4.grid(column = 0, row = 3,  pady=10)

    b5.configure(text="Greasby")
    b5.grid(column = 1, row = 3,  pady=10)

    b6.configure(text="West Kirby")
    b6.grid(column = 2, row = 3,  pady=10)
    #3
    b7.configure(text="Moreton")
    b7.grid(column = 0, row = 4,  pady=10)

    b8.configure(text="Meols")
    b8.grid(column = 1, row = 4,  pady=10)

    b9.configure(text="Bebington")
    b9.grid(column = 2, row = 4,  pady=10)
    #4
    b10.configure(text="Thursaston")
    b10.grid(column = 0, row = 5,  pady=10)

    b11.configure(text="Brombourgh")
    b11.grid(column = 1, row = 5,  pady=10)

    b12.configure(text="Thornton Hough")
    b12.grid(column = 2, row = 5,  pady=10)


start()

window.mainloop() 




