import sys
# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>

file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])

def readFile(archivo):
	content = open(str(archivo),'r')
	#contenido = []
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido

def cargarFile(archivo):
	content = open(str(archivo),'r')
	#contenido = []
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido

dataset = cargarFile(file)
lru = []

class cache:
	def __init__(self, algoritm, tamano):
		self.size = int(tamano)
		self.method = str(algoritm)
		self.missrate = 0
		self.data = {}
		self.cacheContent =[]
		self.lru = []
		
	def setMethod(self):
		hits = 0
		cont = 0
		i = 0
		j = 0
		if(self.method=='LRU'):
			while j < self.size:
				if(self.data.has_key(dataset[i])):
					hits = hits+1
					i = i+1
					
				else:
					self.data[dataset[i]] = [dataset[i]]
					self.cacheContent.append(dataset[i])
					i = i+1
				j = len(self.cacheContent)
			print len(self.cacheContent)
		else:
			print 'no usare nada'
			
	def printInfo(self):
		print 'Evaluando una cache %s con %d entradas.' % (self.method, self.size)
		print 'Resultados:'
		print 'Miss rate: x.x% (W misses out of Q references)'
		print 'Miss rate (warm cache): y.y% (M misses out of Q 50000 references)'
		print len(dataset)

test = cache(policy,entriesNum)
test.setMethod()
test.printInfo()