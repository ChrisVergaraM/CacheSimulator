import sys
# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>

file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])
lru = []

def readFile(file):
	content = open(str(file),'r')
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido


class cache:
	def __init__(self, tamano):
		self.size = tamano