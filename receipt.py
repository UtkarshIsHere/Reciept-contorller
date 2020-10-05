from escpos.printer import Usb
import random
import datetime

date = datetime.datetime.now()



printer = Usb(0x04b8, 0x0e15, 0)


def blankLineForSpacing():
    printer.set(align="center", underline=1, width=1, height=1)
    printer.text("                                                \n")



def printForUtkarsh(place, price, type, busNumber) :
    number = random.randint(1000000, 9999999)
    currentDate = date.strftime("%d/%m/%y")
    fixTheFuckingDate = date.strftime("%d%m%y")
    makeAFuckingBarcode = (date.strftime("%d%m%y") + str(number))
    nextBusTime = date.strftime("%H:" + date.strftime())

    printer.image("logo.png", center=True)
    blankLineForSpacing()
    printer.set(align="left", underline=0, width=2, height=2, custom_size=True)
    printer.text("Location: " + place + "\n")
    printer.text("Price: £" + str(price) + "\n")
    printer.text("Date: " + currentDate + "\n")
    printer.text("Type: " + type + "\n")
    printer.text("Bus Number: " + str(busNumber) + "\n")
    printer.text("Next Bus Coming At: " + str(nextBusTime) + "\n")
    blankLineForSpacing()
    printer.set(align="left", underline=0, width=2, height=2, custom_size=True)
    printer.barcode(makeAFuckingBarcode, 'EAN13', 64, 5, '', '')
    printer.cut()

printForUtkarsh("Filthy Whore", 150, "Slag", 515)