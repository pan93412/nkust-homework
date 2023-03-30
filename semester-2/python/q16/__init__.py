class Cpu: pass
class Monitor: pass
class Mouse: pass
class Keyboard: pass
class Harddisk: pass

class Notebook:
    def __init__(self, cpu: Cpu, monitor: Monitor, keyboard: Keyboard, harddisk: Harddisk):
        self.cpu = cpu
        self.monitor = monitor
        self.keyboard = keyboard
        self.harddisk = harddisk

    def addMouse(self, mouse):
        self.mouse = mouse


cpu = Cpu()
monitor = Monitor()
mouse = Mouse()
keyboard = Keyboard()
harddisk = Harddisk()

notebook = Notebook(cpu, monitor, keyboard, harddisk)
