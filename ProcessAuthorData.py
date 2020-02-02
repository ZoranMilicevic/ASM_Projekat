import networkx as nx
from csvReaderMethods import CVSReaderMethods

class ProcessAuthorDataMethods:
    GrapthOutputPath = 'output/authorGraph.gexf'

    @staticmethod
    def createGraph():
        graph = nx.Graph()
        ProcessAuthorDataMethods.addNodesToGraph(graph)
        ProcessAuthorDataMethods.addEdgesToGraph(graph)
        return graph

    @staticmethod
    def addNodesToGraph(graph):
        authors = CVSReaderMethods.readAuthorsFromFile()
        for key in authors:
            faculty = authors[key][0]
            fact = 'none'
            if faculty == 'matematicki fakultet':
                fact = 'matf'
            if faculty == 'elektrotehnicki fakultet':
                fact = 'etf'
            if faculty == 'fakultet organizacionih nauka':
                fact = 'fon'
            graph.add_node(key, faculty = fact)
        pass

    @staticmethod
    def addEdgesToGraph(graph):
        coauthorships = CVSReaderMethods.readCoauthorshipsFromFile()
        for coauthorship in coauthorships:
            length = len(coauthorship)
            i=0
            while i < length-1:
                author1 = coauthorship[i]
                j = i + 1
                while j < length:
                    author2 = coauthorship[j]
                    if graph.has_edge(author1, author2):
                        graph[author1][author2]['weight'] += 1
                    else:
                        graph.add_edge(author1, author2, weight=1)
                    j = j + 1
                i = i + 1

    @staticmethod
    def printGraph(graph):
        nx.write_gexf(graph, ProcessAuthorDataMethods.GrapthOutputPath)
     

