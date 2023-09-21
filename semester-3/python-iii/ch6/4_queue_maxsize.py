import queue

maxsize = int(input("maxsize (5–20) = "))
if not 5 <= maxsize <= 20:
    raise Exception("A maxsize must be between 5 and 20.")

q = queue.Queue[int](maxsize)

# 往佇列插入 100 個資料
for i in range(100):
    if q.qsize() >= q.maxsize:
        # 存放的資料達到上限 maxsize，插入會 block
        break
    else:
        q.put(i)

# 從佇列取值
while not q.empty():
    n = q.get()
    print("本次取出資料：%d" % n)
