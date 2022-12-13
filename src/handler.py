from graph import Graph

class Hanler(object):

    def to_graph(self, content):
        a_graph=Graph()
        lines = [line.rstrip() for line in content if not(line.startswith("#"))]
        a_graph.set_type(lines[0])
        a_graph.parse(lines[1:])
        
    def reader(self, filepath):
        """
        Read a graph txt file
        param:
        """
        self.a_file =  open(filepath, 'r')
        content = self.a_file.readlines()
        self.to_graph(content)

    def writer(self, filepath, content=""):
        """
        Create a graph txt file
        param:
        param:
        """
        self.a_file =  open(filepath, 'w')
        self.a_file.writelines(content)
        self.a_file.close()
    
