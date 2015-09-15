import sys
import time
# Format admitted for the project <workload_file> <policy> <cache size (number of entries)> <extra parameters may go here>
# python cacheSimulator.py workload.txt LRU 5000
file = str(sys.argv[1])
policy = str(sys.argv[2])
entriesNum = str(sys.argv[3])

def cargarFile(archivo):
	print 'Cargando ' + str(file)
	content = open(str(archivo),'r')
	#contenido = []
	contenido = [x.strip('\n') for x in content.readlines()]
	return contenido
dataset = cargarFile(file)
optimal = {}
''''
def cargando():
	i=0
	print 'Preparando el algoritmo optimo'
	for line in dataset:
		if optimal.has_key(line):
			optimal[line] = int(optimal.get(line))+1
		optimal[line]=i
		i = i+1
cargando()'''

class cache:
	def __init__(self, algoritm, tamano):
		self.size = int(tamano)
		self.method = str(algoritm)
		self.missrate = 0
		self.data = {}
		self.cacheContent =[] #LRU
		
	def setMethod(self):
		temp = dataset
		clockList = []
		uniques = []
		control = []
		hits = 0
		miss= 0
		i = 0
		cont = 0
		print 'Evaluando una cache %s con %d entradas.' % (self.method, self.size)
		
		#LRU
		if(self.method=='LRU'):
			inicio = time.time()
			while i < len(dataset):
				if(self.data.has_key(dataset[i])):
					hits = hits+1
					control.remove(dataset[i])
					control.append(dataset[i])
				else:
					miss = miss+1
					if(len(self.data)<self.size):						
						self.data[dataset[i]] = dataset[i]
						control.append(dataset[i])
					else:						
						del self.data[control[0]]
						control.remove(control[0])						
						self.data[dataset[i]] = dataset[i]
						control.append(dataset[i])
				i= i+1
				print i
			self.missrate = miss
			fin = time.time()
			total = fin - inicio
			print len(self.data)
			print 'Hay %d Misses' % self.missrate
			print 'Hits: ' +str(hits)
			print 'Algoritmo ejecutado en %s' % str(total)
			print len(dataset)
#Implementacion del algoritmo OPTIMO
# python cacheSimulator workload.txt OPTIMO 5000			
		if(self.method=='OPTIMO'):
			i=0
			print 'Preparando el algoritmo optimo'
			for line in dataset:
				if optimal.has_key(line):
					optimal[line] = int(optimal.get(line))+1
				optimal[line]=i
			inicio = time.time()
			while i < len(dataset):
				#Cuando el elemento se repite
				#proximo = temp[i]
				#temp.remove(proximo)
				#if proximo not in temp:
					#Cuando el elemento nunca se repite en el archivo
				#	uniques.append(proximo)
				#else:
				#	control.append(temp.index(proximo))
				#	control.sort()				
				if(self.data.has_key(dataset[i])):
					hits = hits+1										
				else:
					miss = miss+1
					if(len(self.data)<self.size):						
						self.data[dataset[i]] = optimal[dataset[i]]
					else:
						a = list(self.data.values())
						a.sort()
						del self.data[self.data.keys()[self.data.values().index(a.pop())]]
						self.data[dataset[i]] = optimal[dataset[i]]						
				i= i+1
				print i
			self.missrate = miss
			fin = time.time()
			total = fin - inicio
			print len(self.data)
			print 'Misses'+str(self.missrate)
			print 'Resultados'
			miss1= round((self.missrate/len(dataset))*100)
			miss2= round((self.missrate/len(dataset))*100)
			print 'Miss rate:  %f' % miss1 + str(self.missrate) + ' Misses out of %d References ' % len(dataset)
			print 'Miss rate: (warm cache) %f' % miss2 + str(self.missrate) + ' Misses out of %d References ' % (int(len(dataset))-int(self.size))
			#print 'Hits: ' +str(hits)
			print 'Algoritmo ejecutado en %s' % str(total) + ' segundos'
			#print len(dataset)

	def printInfo(self):		
		print 'Resultados:'
		print 'Miss rate: x.x% (W misses out of Q references)'
		print 'Miss rate (warm cache): y.y% (M misses out of Q 50000 references)'
		print len(dataset)

test = cache(policy,entriesNum)
test.setMethod()
#test.printInfo()