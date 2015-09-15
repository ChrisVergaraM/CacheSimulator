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

#print dataset

def guardar(nombreArchivo,info):
	f = open (nombreArchivo+'.txt', "a+")
	f.write(str(info)+'\n')
	f.close()

class cache:
	def __init__(self, algoritm, tamano):
		self.size = int(tamano)
		self.method = str(algoritm)
		self.missrate = 0
		self.data = {}
		self.misses = 0
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
			self.missrate = miss
			fin = time.time()
			total = fin - inicio
			print len(self.data)
			#print 'Misses'+str(self.missrate)
			print 'Resultados'
			miss1= round((float(self.missrate)/len(dataset)),2)*100
			self.misses =miss1
			miss2= round((float(self.missrate)/(int(len(dataset))-int(self.size))),2)*100
			print 'Miss rate:  %s' % str(miss1) + str(self.missrate) + ' %%  Misses out of %d References ' % len(dataset)
			print 'Miss rate: (warm cache) %s' % str(miss2) + str(self.missrate) + ' %%  Misses out of %d References ' % (int(len(dataset))-int(self.size))
			print 'Algoritmo ejecutado en %s' % str(total) + ' segundos'
#Implementacion del algoritmo OPTIMO
# python cacheSimulator workload.txt OPTIMO 5000			
		if(self.method=='OPTIMO'):
			temp = {}
			noUsados = {}
			usados = {}
			eliminar = []
			detener = True
			j=0
			print 'Preparando el algoritmo optimo'
			for line in dataset:
				temp[line]=j
				if noUsados.has_key(line):
					usados[line] = j
					del noUsados[line]
				else:
					if not usados.has_key(line):
						noUsados[line]=j
					else:
						usados[line]=j				
				j= j+1
			usadosList = usados.values()
			usadosList.sort()
			usadosList.reverse()
			noUsadosList = noUsados.values()
			noUsadosList .sort()
			print usadosList
			print noUsadosList
			eliminar = noUsadosList+usadosList
			print eliminar
			inicio = time.time()
			print i
			while i < len(dataset):		
				if(self.data.has_key(dataset[i])):
					hits = hits+1
					print 'Es un hit'
				else:
					miss = miss+1
					print 'Es un miss'
					if(len(self.data)<self.size):
						self.data[dataset[i]] = 0
					else:
						punt = 0
						while detener:
							if self.data.has_key(dataset[eliminar[punt]]):
								del self.data[dataset[eliminar[punt]]]
								eliminar.remove(eliminar[punt])
								detener = False
							else:
								punt = punt + 1
						detener = True
						self.data[dataset[i]] = 0
				i= i+1
				print i
				print self.data
			self.missrate = miss
			fin = time.time()
			total = fin - inicio
			print len(self.data)
			print 'Misses'+str(self.missrate)
			print 'Resultados'
			miss1= round((float(self.missrate)/len(dataset)),2)*100
			self.misses =miss1
			miss2= round((float(self.missrate)/(int(len(dataset))-int(self.size))),2)*100
			print 'Miss rate:  %s' % str(miss1) + str(self.missrate) + ' %%  Misses out of %d References ' % len(dataset)
			print 'Miss rate: (warm cache) %s' % str(miss2) + str(self.missrate) + ' %%  Misses out of %d References ' % (int(len(dataset))-int(self.size))
			print 'Algoritmo ejecutado en %s' % str(total) + ' segundos'

test = cache(policy,entriesNum)
test.setMethod()
info = str(test.size)+','+str(test.misses)+','+str(test.method)
guardar('results',info)
