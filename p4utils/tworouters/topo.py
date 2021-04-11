import os 
import logging

from mininet.topo import Topo

class Topology(Topo):
    """ Create the network topology"""

    def __init__(self):
        super(Topology, self).__init__()

        # Routers as mininet switches
        # Will write another function to use the switches as routers
        r1 = self.addSwitch('r1')
        r2 = self.addSwitch('r2')

        # Two host two router scenario 
        h1 = self.addHost('h1',ip='10.1.0.1/24', defaultRoute='via 10.1.0.2')
        h2 = self.addHost('h2',ip='10.2.0.1/24', defaultRoute='via 10.2.0.2')

        #h1 = self.addSwitch('h1')
        #h2 = self.addSwitch('h2')       

        # Add the connections 
        self.addLink(r1, r2)
        self.addLink(h1, r1)
        self.addLink(r2, h2)

        
