import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
print(printer.upper("hello world"))
print(printer.length("hello world"))

math_base = communicator.stringToProxy("SimpleMath:default -p 11000")
math = Demo.MathPrx.checkedCast(math_base)
if not math:
    raise RuntimeError("Invalid proxy")

print(math.add(2, 3))
print(math.mul(4, 5))
