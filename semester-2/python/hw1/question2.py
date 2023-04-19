# Step 1: 初始化所有零組件
class CPU: pass
class Monitor: pass
class Mouse: pass
class Keyboard: pass
class SSD: pass
class Reader: pass
class UsbHub: pass
class Printer: pass

class Notebook:
    # Step 3: Aggregation, declaration
    mouse: Mouse
    usb_hub: UsbHub
    printer: Printer

    # Step 2: Composition
    def __init__(self):
        self.cpu = CPU()
        self.monitor = Monitor()
        self.keyboard = Keyboard()
        self.reader = Reader()

    # Step 3: Aggregation
    def connect_mouse(self, mouse: Mouse):
        self.mouse = mouse

    def insert_usb_hub(self, usb_hub: UsbHub):
        self.usb_hub = usb_hub

    def link_printer(self, printer: Printer):
        self.printer = printer

nb = Notebook()
nb.connect_mouse(Mouse())
nb.insert_usb_hub(UsbHub())
nb.link_printer(Printer())
