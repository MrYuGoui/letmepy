from time import sleep,ctime
import threading
def super_player(filename,time):
    for i in range(999999):
        print(f"开始播放：{filename,ctime()}")
        sleep(time)
lists={"权游.MP4":1,"我和你.mp3":2,"东京热.avi":5}
threads=[]
files=range(len(lists))
for filename,time in lists.items():
    t=threading.Thread(target=super_player,args=(filename,time))
    threads.append(t)
if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"结束{ctime()}")