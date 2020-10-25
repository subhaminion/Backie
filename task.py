import abc
import json
import uuid

from broker import Broker

class NotImplementedError:
	pass

class BaseTask(abc.ABC):
	"""
	Usage:
	class AdderTask(BaseTask):
		task_name = "AdderTask"
		def run(self, a, b):
			result = a + b
			return result
	adder = AdderTask()
	adder.delay(9, 34)
	"""

	task_name = None

	def __init__(self):
		if not self.task_name:
			raise ValueError("task_name should be defined")
		self.broker = Broker()


	@abc.abstractmethod
	def run(self, *args, **kwargs):
		# business logic goes here
		raise NotImplementedError("Task run method must be implemented.")


	def delay(self, *args, **kwargs):
		try:
			task_id = str(uuid.uuid4())
			_task = {"task_id":  task_id, "args": args, "kwargs": kwargs}
			serialized_task = json.dumps(_task)
			self.broker.enqueue(queue_name=self.task_name, item=serialized_task)
			print("task: {0} succesfuly queued".format(task_id))
		except Exception:
			raise Exception("Unable to publish task to the broker.")
