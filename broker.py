import redis

class Broker:
	"""
	using redis as our broker.
	This will implement basic FIFO queue using redis.
	"""
	def __init__(self):
		host = "localhost"
		port = 6379
		password = None
		self.redis_instance = redis.StrictRedis(
			host=host, port=port, password=password, db=0, socket_timeout=8.0
		)

	def enqueue(self, item, queue_name):
		self.redis_instance.lpush(queue_name, item)

	def dequeue(self, queue_name):
		dequeued_item = self.redis_instance.brpop(queue_name, timeout=3)
		if not dequeued_item:
			return None

		dequeued_item = dequeued_item[1]
		return dequeued_item
