from escpos.printer import Usb
import random
import datetime

date = datetime.datetime.now()

nextBusTime = 1

almostThere = 0

printer = Usb(0x04b8, 0x0e15, 0)

def blankLineForSpacing():
    printer.set(align="center", underline=1, width=1, height=1)
    printer.text("                                                \n")

def anActualGoodTimeCalculatorBecauseThisCouldBeAMistakeInTheFuture() :
    almostThere = int(date.strftime("%M"))
    print(almostThere)
    almostThere += 15
    print(almostThere)
    wowWeHadToChangeTheTime = int(date.strftime("%H"))
    if int(almostThere) > 44:
        wowWeHadToChangeTheTime += 1
        ffs = int(almostThere) - 60
        if ffs > 10:
            ffs = str(ffs)
            ffs = str(ffs).zfill(2)
            almostThere = ffs

    if wowWeHadToChangeTheTime == 24:
        wowWeHadToChangeTheTime = 0
        wowWeHadToChangeTheTime = str(wowWeHadToChangeTheTime).zfill(2)
    
    nextBusTime = str(str(wowWeHadToChangeTheTime) + ":" + str(ffs))
    return nextBusTime

def printForUtkarsh(place, price, type, busNumber) :
    timeThatTheBusActuallyComes = anActualGoodTimeCalculatorBecauseThisCouldBeAMistakeInTheFuture()
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


try:
    printForUtkarsh("Zach", 1.50, "Feteus", 515)
    #place string, price int, type string, bus number int
except:
    printer.cut()

