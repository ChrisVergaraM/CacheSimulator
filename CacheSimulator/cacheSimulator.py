import sys


# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>
file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])


class cache:
	def __init__(self, tamano):
		self.size = tamano