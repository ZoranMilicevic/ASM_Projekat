import networkx as nx
from csvReaderMethods import CVSReaderMethods

class ProcessPublicationDataMethods:
    GrapthOutputPath = r'output/publicationGraph.gexf'

    @staticmethod
    def createGraph():
        graph = nx.Graph()
        publicataions = CVSReaderMethods.readPublicationsFromFile()
        ProcessPublicationDataMethods.addNodesToGraph(graph, publicataions)
        journalAndHisAuthors = ProcessPublicationDataMethods.createMapOfJurnalAndAuthors(publicataions)
        ProcessPublicationDataMethods.addEdgesToGraph(graph, journalAndHisAuthors)
        return graph
    
    @staticmethod
    def addNodesToGraph(graph, publications):
        for key in publications:
            publicationType = publications[key][3]
            graph.add_node(key, publicationType = publicationType)

    
    @staticmethod
    def createMapOfJurnalAndAuthors(publications):
        journalAndHisAuthors = dict() #dictionary -> journslName: authorNames
        for key in publications:
            for author in publications[key][1]:
                if key in journalAndHisAuthors:
                    journalAndHisAuthors[key].append(author)
                else:
                    journalAndHisAuthors[key] = [author]
        return journalAndHisAuthors          
    
    @staticmethod
    def addEdgesToGraph(graph, journalAndHisAuthors):
        journals = list(journalAndHisAuthors.keys())
        length = len(journals)
        i = 0
        while i < length-1:
            journal1 = journals[i]
            authors1 = journalAndHisAuthors[journal1] 
            j = i + 1
            while j < length:
                journal2 = journals[j]
                authors2 = journalAndHisAuthors[journal2]
                intersection = list(set(authors1) & set(authors2))
                numberOfAuthorsThatPublishedInBothJournals = len(intersection)
                if numberOfAuthorsThatPublishedInBothJournals > 0:
                    if graph.has_edge(journal1, journal2):
                        graph[journal1][journal2]['weight'] += numberOfAuthorsThatPublishedInBothJournals
                    else:
                        graph.add_edge(journal1, journal2, weight=numberOfAuthorsThatPublishedInBothJournals)
                j = j + 1
            i = i + 1
        return graph

    @staticmethod
    def printGraph(graph):
        nx.write_gexf(graph, ProcessPublicationDataMethods.GrapthOutputPath)
        pass
