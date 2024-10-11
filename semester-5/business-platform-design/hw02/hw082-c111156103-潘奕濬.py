# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

# 四個月份
labels = ['Jun', 'Jul', 'Aug', 'Sep']
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
