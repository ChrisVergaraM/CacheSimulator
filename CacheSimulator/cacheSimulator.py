import sys
# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>

file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])

def readFile(archivo):
	content = open(str(archivo),'r')
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido

dataset = readFile(file)
lru = []

class cache:
	def __init__(self, algoritm, tamano):
		self.size = int(tamano)
		self.method = str(algoritm)
		
	def setMethod(self):
		if(self.method=='LRU'):
			print 'usare algo'
		else:
			print 'no usare nada'
			
	def printInfo(self):
		print 'Evaluando una cache %s con %d entradas.' % (self.method, self.size)
		print 'Resultados:'
		print 'Miss rate: x.x% (W misses out of Q references)'
		print 'Miss rate (warm cache): y.y% (M misses out of Q 50000 references)'
		print len(dataset)

test = cache(policy,entriesNum)
test.printInfo()