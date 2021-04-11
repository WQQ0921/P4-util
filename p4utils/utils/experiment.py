import os 
import argparse 
import importlib
import sys

class Experiment:

    """ Helper class that describes a nework experiment for FRR configuration.
    """
    def __init__(self):
        root_dir = os.path.dirname(sys.modules['__main__'].__file__)

        #Put FRR config directory here
        config_dir = "tworouters"
        topo_dir = os.path.join(root_dir, config_dir)
        
        # Initialise list of daemons.
        self.daemons = []
        self.nodes = []
        self.directory = [] 
        self._get_config_nodes(topo_dir)


    def _get_config_nodes(self, parent_dir):
        config = "config"
        config_dir = os.path.join(parent_dir, config)
        if os.path.exists(config_dir) and os.path.isdir(config_dir):

            self.daemons.insert(0, "zebra")
            #self.daemons.append("staticd")
            self.daemons.append("ospfd")

            #setattr(self, config, set())
            #setattr(self, "{}_conf".format(config), config_dir)
            self.directory.append(config_dir)

            # Each node  must have a conf file in the
            # config directory called <node_name>.conf.
            for conf in os.listdir(config_dir):
                if conf.endswith(".conf"):
                    self.nodes.append(conf.split('.')[0])
        
