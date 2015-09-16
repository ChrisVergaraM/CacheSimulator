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
	
class clockItem:
	def __init__(self,content,ind):
		self.content = content
		self.ind = str(ind)

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
			
#Implementacion del algoritmo CLOCK
# python cacheSimulator workload.txt CLOCK 5000			
		if(self.method=='CLOCK'):
			ref = []
			indice = 0
			indices = {}
			puntero = 0
			posicion = 0
			stop = True
			inicio = time.time()
			while i < len(dataset):
				stop = True
				if puntero == (self.size)-1:
					puntero = 0
				if(self.data.has_key(dataset[i])):
					hits = hits+1
					del self.data[dataset[i]]
					self.data[dataset[i]] = 1
					ref.append(dataset[i])
				else:
					miss = miss+1
					if(len(self.data)<self.size):
						self.data[dataset[i]] = 0
						indices[dataset[i]] = indice
						clockList.append(dataset[i])					
						indice = indice + 1
					else:
						if (self.data.get(clockList[puntero])==0):
							posicion = indices.get(clockList[puntero])
							del self.data[clockList[puntero]]
							del indices[clockList[puntero]]
							if clockList[puntero] in ref:
								ref.remove(clockList[puntero])
							#clockList.remove(clockList[puntero])							
							puntero = puntero + 1
							
							
						else:
							while stop:
								tope = (len(clockList)-1)
								for element in ref:
									self.data[element]=0
								self.data[clockList[puntero]] = 0
								puntero = puntero + 1
								if (self.data.get(clockList[puntero])==0):
									posicion = indices.get(clockList[puntero])								
									del self.data[clockList[puntero]]
									del indices[clockList[puntero]]
									if clockList[puntero] in ref:
										ref.remove(clockList[puntero])
									#clockList.remove(clockList[puntero])
									puntero = puntero + 1
									stop = False
									if (puntero == (int(self.size))):
										puntero = 0
									if indice==self.size:
										indice = 0
								if (puntero == (int(self.size))):
										puntero = 0
								if indice==self.size:
										indice = 0
							indice = indice + 1	
						self.data[dataset[i]] = 0
						indices[dataset[i]] = indice
						clockList[posicion] = dataset[i]
						indice = indice + 1
					if indice==self.size:
						indice = 0	
				i= i+1
				print i
				ref = list(set(ref))
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
			#print 'Hits: ' +str(hits)
			print 'Algoritmo ejecutado en %s' % str(total) + ' segundos'
			#print len(dataset)

test = cache(policy,entriesNum)
test.setMethod()
info = str(test.size)+','+str(test.misses)+','+str(test.method)
guardar('results',info)
