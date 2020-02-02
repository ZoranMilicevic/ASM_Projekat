import csv

class CVSReaderMethods:
    AuthorsFilePath = r'input/authors.csv'
    CoauthorsFilePath = r'input/coauthors.csv'
    PublicationsFilePath = r'input/publications.csv'

    authorsFullNamesWithMiddle = dict()
    authorsFullNamesWithoutMiddle = dict()
    authorsShortNamesWithoutMiddle = dict()
    authorsShortNamesWithMiddle = dict()

    @staticmethod
    def readAuthorsFromFile():
        authorsFullNamesWithMiddle = dict() #dictionary -> name: (faculty, department)
        authorsFullNamesWithoutMiddle = dict()
        authorsShortNamesWithoutMiddle = dict()
        authorsShortNamesWithMiddle = dict()

        with open(CVSReaderMethods.AuthorsFilePath) as authorsFile:
            next(authorsFile)
            csvReader = csv.reader(authorsFile, delimiter = ',')
            for row in csvReader:
                fullNameWithoutMiddle = row[1] + ' ' + row[0]
                fullNameWithMiddle = fullNameWithoutMiddle
                if(row[2] != '' and row[2] != ' '):
                    fullNameWithMiddle = fullNameWithMiddle + ' ' + row[2] + '.'
                
                shortNameWithoutMiddle = row[1] + ' ' + row[0][0] + '.'
                shortNameWithMiddle = shortNameWithoutMiddle
                if(row[2] != '' and row[2] != ' '):
                    shortNameWithMiddle = shortNameWithMiddle + row[2] + '.'

                fullNameWithoutMiddle = fullNameWithoutMiddle.lower()
                fullNameWithMiddle = fullNameWithMiddle.lower()

                shortNameWithoutMiddle = shortNameWithoutMiddle.lower()
                shortNameWithMiddle = shortNameWithMiddle.lower()

                authorsFullNamesWithoutMiddle[fullNameWithoutMiddle] = (row[4].strip(), row[3].strip())
                authorsFullNamesWithMiddle[fullNameWithMiddle] = (row[4].strip(), row[3].strip())

                authorsShortNamesWithoutMiddle[shortNameWithoutMiddle] = (row[4].strip(), row[3].strip())
                authorsShortNamesWithMiddle[shortNameWithMiddle] = (row[4].strip(), row[3].strip())

        CVSReaderMethods.authorsFullNamesWithoutMiddle = authorsFullNamesWithoutMiddle
        CVSReaderMethods.authorsFullNamesWithMiddle = authorsFullNamesWithMiddle
        CVSReaderMethods.authorsShortNamesWithoutMiddle = authorsShortNamesWithoutMiddle
        CVSReaderMethods.authorsShortNamesWithMiddle = authorsShortNamesWithMiddle
        return authorsShortNamesWithoutMiddle

    @staticmethod
    def readCoauthorshipsFromFile():
        coauthorships = list()
        with open(CVSReaderMethods.CoauthorsFilePath) as coauthorsFile:
            csvReader = csv.reader(coauthorsFile, delimiter = ',')
            for row in csvReader:
                coauthors = list()
                authors = row[0].split(' and ')
                for author in authors:
                    author = author.lower().strip()
                    if author in CVSReaderMethods.authorsFullNamesWithMiddle or author in CVSReaderMethods.authorsFullNamesWithoutMiddle or author in CVSReaderMethods.authorsShortNamesWithMiddle or author in CVSReaderMethods.authorsShortNamesWithoutMiddle:
                        author = author.split(' ')
                        authorName = author[0] + ' ' + author[1][0] + '.'
                        coauthors.append(authorName)
                if len(coauthors) > 1:
                    coauthorships.append(coauthors)
        return coauthorships
    
    @staticmethod
    def readPublicationsFromFile():
        publications = dict()
        with open(CVSReaderMethods.PublicationsFilePath) as publicationsFile:
            next(publicationsFile) #skip first line
            csvReader = csv.reader(publicationsFile, delimiter = ',')
            for row in csvReader:
                authorsString = row[3]
                authors = authorsString.lower().split(' and ')
                journalAuthors = list()

                for author in authors:
                    author = author.lower().strip()
                    if author in CVSReaderMethods.authorsFullNamesWithMiddle or author in CVSReaderMethods.authorsFullNamesWithoutMiddle or author in CVSReaderMethods.authorsShortNamesWithMiddle or author in CVSReaderMethods.authorsShortNamesWithoutMiddle:
                        author = author.split(' ')
                        authorName = author[0] + ' ' + author[1][0] + '.'
                        journalAuthors.append(authorName)
                
                publications[row[6]] = (row[2], journalAuthors, row[4], row[5])  #dictionary -> journalName : (date-authors-citations-type)
        return publications


    
