import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print("Washing!", dish)
        output.put(dish)

def dryer(_input):
    print('set dryer')
    while True:
        dish = _input.get()
        print("Drying", dish)
        _input.task_done()

if __name__ == '__main__':

    dish_queue = mp.JoinableQueue() # 큐 생성.
    dryer_proc = mp.Process(target=dryer, args=(dish_queue, ))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessrt']
    washer(dishes, dish_queue)
    dish_queue.join() # washer가 모든 dryer가 끝났다는 것을 알게 함. 

