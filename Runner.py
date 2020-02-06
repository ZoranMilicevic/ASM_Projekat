from csvReaderMethods import CVSReaderMethods
from ProcessAuthorData import ProcessAuthorDataMethods
from ProcessPublicationData import ProcessPublicationDataMethods
import AdditionalMethods

def main():
    authorGraph = ProcessAuthorDataMethods.createGraph()
    ProcessAuthorDataMethods.printGraph(authorGraph)

    journalGraph = ProcessPublicationDataMethods.createGraph()
    ProcessPublicationDataMethods.printGraph(journalGraph)

    AdditionalMethods.bestFaculties()
    AdditionalMethods.meanNumberOfAuthors()
    AdditionalMethods.bestYears()
    pass

if __name__ == "__main__":
    main()     