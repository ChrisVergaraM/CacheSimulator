import sys
import time
# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>
# python cacheSimulator workload.txt LRU 5000
file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])

def readFile(archivo):
	content = open(str(archivo),'r')
	#contenido = []
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido

def cargarFile(archivo):
	print 'Cargando ' + str(file)
	content = open(str(archivo),'r')
	#contenido = []
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido

dataset = cargarFile(file)

class cache:
	def __init__(self, algoritm, tamano):
		self.size = int(tamano)
		self.method = str(algoritm)
		self.missrate = 0
		self.data = {}
		self.cacheContent =[] #LRU
		
	def setMethod(self):
		hits = 0
		miss= 0
		i = 0
		print 'Evaluando una cache %s con %d entradas.' % (self.method, self.size)
		inicio = time.time()
		if(self.method=='LRU'):
			while i < len(dataset):
				if(self.data.has_key(dataset[i])):
					hits = hits+1
					del self.data[dataset[i]]
					self.data[dataset[i]] = dataset[i]											
				else:
					miss = miss+1
					self.missrate = miss
					if(len(self.data)<self.size):						
						self.data[dataset[i]] = dataset[i]						
					else:						
						self.data.popitem()
						self.data[dataset[i]] = dataset[i]							
				i= i+1
			fin = time.time()
			total = fin - inicio
			print len(self.data)
			print 'Hay %d Misses' % self.missrate
			print 'Hits: ' +str(hits)
			print 'Algoritmo ejecutado en %s' % str(total)
			print len(dataset)
			
		else:
			print 'no usare nada'
			
	def printInfo(self):		
		print 'Resultados:'
		print 'Miss rate: x.x% (W misses out of Q references)'
		print 'Miss rate (warm cache): y.y% (M misses out of Q 50000 references)'
		print len(dataset)

test = cache(policy,entriesNum)
test.setMethod()
#test.printInfo()