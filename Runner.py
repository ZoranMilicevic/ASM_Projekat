from csvReaderMethods import CVSReaderMethods
from ProcessAuthorData import ProcessAuthorDataMethods
from ProcessPublicationData import ProcessPublicationDataMethods

def main():
    authorGraph = ProcessAuthorDataMethods.createGraph()
    ProcessAuthorDataMethods.printGraph(authorGraph)

    #journalGraph = ProcessPublicationDataMethods.createGraph()



if __name__ == "__main__":
    main()     