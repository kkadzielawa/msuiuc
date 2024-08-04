from queue import Queue


name_lst = ["Konrad", "John", "Jason", "Leo", "Layla"]
num = 2
# def hot_potato(name_lst, num):
simqueue = Queue()

for name in name_lst:
    simqueue.enqueue(name)

print(simqueue.look())

while simqueue.size() > 1:
    for _ in range(num):
        simqueue.enqueue(simqueue.front())
        simqueue.dequeue()
    simqueue.dequeue()

print(simqueue.look())
