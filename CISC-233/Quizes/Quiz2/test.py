from Queue import Queue
import random

def hot_potato(name_list, num):
	sim_queue = Queue()

	for name in name_list:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		num = random.randrange(0,5)
		for i in range(num):
			num = random.randrange(0,5)
			print sim_queue.items
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()
	
	return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent","Brad"], 0))
