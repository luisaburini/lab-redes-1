import atexit
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import info,setLogLevel
from mininet.link import TCLink
net = None

def createTopo():
	topo=Topo()
	#Create Host Nodes
	for x in range(1,9):
		print "h"+str(x)
		topo.addHost("h" + str(x))
	#Create Switch Nodes
	topo.addSwitch("c1")
	topo.addSwitch("d1")
	topo.addSwitch("d2")
	for x in range(1,5):
		print "a"+str(x)
		topo.addSwitch("a" + str(x))
		
	#Create links
	topo.addLink("c1","d1",bw=10000, delay='1ms')
	topo.addLink("c1","d2",bw=10000, delay='1ms')

	for x in range(1,3):
		topo.addLink("d"+str(x),"a"+str(2*x-1),bw=1000,delay='3ms')
		topo.addLink("d"+str(x),"a"+str(2*x),bw=1000,delay='3ms')

	
	for x in range(1,5):
		topo.addLink("a"+str(x),"h"+str(2*x-1),bw=100,delay='5ms')
		if 2*x == 8:
			topo.addLink("a"+str(x),"h"+str(2*x),bw=100,delay='5ms',loss=15)
		topo.addLink("a"+str(x),"h"+str(2*x),bw=100,delay='5ms')
	return topo

def startNetwork():
	topo = createTopo()
	global net
	net = Mininet(topo=topo, autoSetMacs=True, link=TCLink)
	net.start()
	CLI(net)

def stopNetwork():
	if net is not None:
		net.stop()

if __name__ == '__main__':
	atexit.register(stopNetwork)
	setLogLevel('info')
	startNetwork()
