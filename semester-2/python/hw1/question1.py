class Windows:
    def __init__(self, w=10, h=5):
        self.width = w
        self.height = h

    # Step 2: `getArea()`
    def getArea(self):
        return self.width * self.height

    # Step 4: `__eq__()`
    def __eq__(self, other: "Windows"):
        return self.getArea() == other.getArea()

# Step 1: 建立 `w0`
w0 = Windows()

# Step 3: 再次建立 `w0`
w0 = Windows(12, 8)
print(w0.getArea()) # 印出

# Step 5: `w1` to compare
w1 = Windows(12, 8)
print(w0 == w1)
