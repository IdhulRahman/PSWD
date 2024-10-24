from mininet.topo import Topo

class MyMeshTopo( Topo ):
    "Full mesh topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        
        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        
        # Add links to form a full mesh
        switches = [s1, s2, s3, s4, s5, s6]
        for i in range(len(switches)):
            for j in range(i + 1, len(switches)):
                self.addLink(switches[i], switches[j])

        # Add host links to switches
        self.addLink( s1, h1 )
        self.addLink( s2, h2 )
        self.addLink( s3, h3 )
        self.addLink( s4, h4 )
        self.addLink( s5, h5 )
        self.addLink( s6, h6 )

topos = { 'mesh': ( lambda: MyMeshTopo() ) }
