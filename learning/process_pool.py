from multiprocessing import Pool
import os
import time
import random
#使用线程池
def func_proc(name):
    print('child prcess %s is running'%name)
    start = time.time()
    time.sleep(random.random()*3)
    end =time.time()
    print('child process %s lasted %d seconds'%(name,(end-start)))

if __name__ == '__main__':
    print('this is parent process %s'%os.getppid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(func_proc,args=(i,))
    print('waiting for all child process done...')
    p.close()
    p.join()
    print('all processes are finished')
