import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def upper(self, s, current=None):
        return s.upper()

    def length(self, s, current=None):
        return len(s)

class MathI(Demo.Math):
    def add(self, a, b, current=None):
        return a + b

    def mul(self, a, b, current=None):
        return a * b

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
math = MathI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.add(math, communicator.stringToIdentity("SimpleMath"))
adapter.activate()

communicator.waitForShutdown()