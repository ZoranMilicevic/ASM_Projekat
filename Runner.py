from csvReaderMethods import CVSReaderMethods
from ProcessAuthorData import ProcessAuthorDataMethods
from ProcessPublicationData import ProcessPublicationDataMethods

def main():
    authorGraph = ProcessAuthorDataMethods.createGraph()
    ProcessAuthorDataMethods.printGraph(authorGraph)

    journalGraph = ProcessPublicationDataMethods.createGraph()
    ProcessPublicationDataMethods.printGraph(journalGraph)
    pass

if __name__ == "__main__":
    main()     