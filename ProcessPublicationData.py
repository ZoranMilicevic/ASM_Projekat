import networkx as nx
from csvReaderMethods import CVSReaderMethods
import matplotlib.pyplot as plt

class ProcessPublicationDataMethods:

    @staticmethod
    def createGraph():
        graph = nx.Graph()
        publicataions = CVSReaderMethods.readPublicationsFromFile()
        ProcessPublicationDataMethods.addNodesToGraph(graph, publicataions)
        authorAndHisJournals = ProcessPublicationDataMethods.creatMapOfAuthorsAndJournals(publicataions)
        journalAndHisAuthors = ProcessPublicationDataMethods.createMapOfJurnalAndAuthors(publicataions)
        ProcessPublicationDataMethods.addEdgesToGraph(graph, authorAndHisJournals, journalAndHisAuthors)
        return graph
    
    @staticmethod
    def addNodesToGraph(graph, publications):
        for key in publications:
            graph.add_node(key)

    @staticmethod
    def creatMapOfAuthorsAndJournals(publications):
        authorAndHisJournals = dict() #dictionary -> authorName: journals
        for key in publications:
            for author in publications[key][1]:
                if author in authorAndHisJournals:
                    authorAndHisJournals[author].append(key)
                else:
                    authorAndHisJournals[author] = [key]
        return authorAndHisJournals
    
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
    def addEdgesToGraph(graph, authorAndHisJournals, journalAndHisAuthors):
        pass
