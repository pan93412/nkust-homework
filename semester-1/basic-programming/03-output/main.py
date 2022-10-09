"""
一、跳脫字元
"""
name1 = ["Alex's iPhone"
                    'Alex\'s iPhone']

"""
二、輸出 print()

print(項目1, [項目2, ...][, sep=分隔字元][, end=結束字元])
  -> 分隔字元預設為空白
"""

print(100, "智慧商務系", True, [1])
print(str(100) + "智慧商務系" + str(True))

print(100, "智慧商務系", True, sep="#")
print(100, "智慧商務系", True, end="@") # no newline now
print(100, "智慧商務系", True, sep="#", end="@") # no newline now

print()

"""
三、print() 命令參數格式化
"""

## 3-1. 百分比 (%)
## print(項目 % (參數1, 參數2, ...))
fmt = "Hello, %s!"
print(fmt % ("World"))
print(fmt % ("Alex"))

fmt_num = "You have NTD$%d remaining."
print(fmt_num % (114514))

fmt_num = "You have NTD$%f remaining."
print(fmt_num % (114.514))

print("%s 的成績是 %d 分" % ("班代", 80))
print("%5s 的成績是 %3d 分" % ("班代", 80))   # right-aligned
print("%-5s 的成績是 %3d 分" % ("班代", 80))  # left-aligned
print("我的體重是 %f kg" % (114514.1919810))
print("我的體重是 %.2f kg" % (114514.1919810))  # 四捨五入
print("我的體重是 %-10.2f kg" % (114514.1919810))  # 四捨五入, r-a

## 3-2. `.format()`
## print(項目.format(參數 1, 參數 2, ...))
## while 項目: {[編號][:格式化規格]}
fmt = "Hello, {}!"
print(fmt.format("World"))
print(fmt.format("Alex"))

fmt_num = "You have NTD${0} remaining."
print(fmt_num.format(114514))

fmt_num = "You have NTD${price} remaining."
print(fmt_num.format(price = 114.514))

print("{} 的成績是 {} 分".format("班代", 80))
print("{1} 的成績是 {0} 分".format("班代", 80))
print("{:>5} 的成績是 {:>3} 分".format("班代", 80))   # right-aligned
print("{:<5} 的成績是 {:>3} 分".format("班代", 80))  # left-aligned
print("我的體重是 {} kg".format(114514.1919810))
print("我的體重是 {:.2} kg".format(114514.1919810))  # 四捨五入
print("我的體重是 {:<10.2} kg".format(114514.1919810))  # 四捨五入, r-a
print("我的體重是 {:^10.2} kg".format(114514.1919810))  # 四捨五入, r-c
print("我的體重是 {:>10.2} kg".format(114514.1919810))  # 四捨五入, r-c

## 3-3. `f-string`
## print(f"項目")
##
## Usage of this is really similar to
## the `.format()` method.
for i in range(12):
    print(f"Hello, {i:>2}!")
