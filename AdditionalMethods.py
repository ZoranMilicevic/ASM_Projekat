import csv
from csvReaderMethods import CVSReaderMethods

def meanNumberOfAuthors():
    with open(CVSReaderMethods.PublicationsFilePath) as publicationsFile:
        next(publicationsFile) #skip first line
        csvReader = csv.reader(publicationsFile, delimiter = ',')
        
        numberOfAuthorsInConference = 0
        numberOfConferences = 0
        numberOfAuthorsInArticle = 0
        numberOfArticles = 0

        for row in csvReader:
            authorsString = row[3]
            authors = authorsString.lower().split(' and ')
            if row[5] == 'Article' or row[5] == 'Article in Press':
                numberOfArticles = numberOfArticles + 1
                numberOfAuthorsInArticle = numberOfAuthorsInArticle + len(authors)
            elif row[5] == 'Conference Paper':
                numberOfConferences = numberOfConferences + 1
                numberOfAuthorsInConference = numberOfAuthorsInConference + len(authors)
        
        print('Zadatak 17')
        print('----------------------------------------------------------------------')
        print('Prosecan broj autora po radovima u casopisima je: ' + str(numberOfAuthorsInArticle / numberOfArticles))
        print('Prosecan broj autora po radovima na konferncijama je: ' + str(numberOfAuthorsInConference / numberOfConferences))
        print('')
    pass


def bestYears():
    with open(CVSReaderMethods.PublicationsFilePath) as publicationsFile:
        next(publicationsFile) #skip first line
        csvReader = csv.reader(publicationsFile, delimiter = ',')

        fonSiPoints = dict()
        fonIsPoints = dict()
        etfRtiPoints = dict()
        matfRiPoints = dict()

        for row in csvReader:
            authorsString = row[3]
            authors = authorsString.lower().split(' and ')
            
            year = row[2]

            for author in authors:
                author = author.lower().strip()
                department = None

                if author in CVSReaderMethods.authorsFullNamesWithMiddle:
                    authorInfo = CVSReaderMethods.authorsFullNamesWithMiddle[author]
                    department = authorInfo[1]
                    
                elif author in CVSReaderMethods.authorsFullNamesWithoutMiddle: 
                    authorInfo = CVSReaderMethods.authorsFullNamesWithoutMiddle[author]
                    department = authorInfo[1]

                elif author in CVSReaderMethods.authorsShortNamesWithMiddle:
                    authorInfo = CVSReaderMethods.authorsShortNamesWithMiddle[author]
                    department = authorInfo[1]

                elif author in CVSReaderMethods.authorsShortNamesWithoutMiddle:
                    authorInfo = CVSReaderMethods.authorsShortNamesWithoutMiddle[author]
                    department = authorInfo[1]
                
                if department == 'katedra za racunarstvo i informatiku':
                    if year in matfRiPoints:
                        matfRiPoints[year] = matfRiPoints[year] + 1
                    else:
                        matfRiPoints[year] = 1

                elif department == 'katedra za racunarsku tehniku i informatiku':
                    if year in etfRtiPoints:
                        etfRtiPoints[year] = etfRtiPoints[year] + 1
                    else:
                        etfRtiPoints[year] = 1

                elif department == 'Katedra za informacione sisteme':
                    if year in fonIsPoints:
                        fonIsPoints[year] = fonIsPoints[year] + 1
                    else:
                        fonIsPoints[year] = 1
                
                elif department == 'Katedra za softversko inzenjerstvo':
                    if year in fonSiPoints:
                        fonSiPoints[year] = fonSiPoints[year] + 1
                    else:
                        fonSiPoints[year] = 1

    print('Zadatak 20')
    print('----------------------------------------------------------------------')
    print('FON Katedra za softversko inzinjerstvo: ')
    maxYear = 0
    maxPoints = -1
    for entry in fonSiPoints:
        print(str(entry) + ' ' + str(fonSiPoints[entry]) + ' poena')
        if fonSiPoints[entry] > maxPoints:
            maxPoints = fonSiPoints[entry]
            maxYear = entry
    print('----------------------------------------------------------------------')
    print('Najuspesnija godina za FON Katedra za softversko inzinjerstvo ' + str(maxYear) + ' ' + str(maxPoints) + ' poena')

    print('')
    print('FON Katedra za informacione sisteme: ')
    maxYear = 0
    maxPoints = -1
    for entry in fonIsPoints:
        print(str(entry) + ' ' + str(fonIsPoints[entry]) + ' poena')
        if fonIsPoints[entry] > maxPoints:
            maxPoints = fonIsPoints[entry]
            maxYear = entry
    print('----------------------------------------------------------------------')
    print('Najuspesnija godina za FON Katedra za informacione sisteme ' + str(maxYear) + ' ' + str(maxPoints) + ' poena')

    print('')
    print('ETF Katedra za racunarsku tehniku i informatiku: ')
    maxYear = 0
    maxPoints = -1
    for entry in etfRtiPoints:
        print(str(entry) + ' ' + str(etfRtiPoints[entry]) + ' poena')
        if etfRtiPoints[entry] > maxPoints:
            maxPoints = etfRtiPoints[entry]
            maxYear = entry
    print('----------------------------------------------------------------------')
    print('Najuspesnija godina za ETF Katedra za racunarsku tehniku i informatiku ' + str(maxYear) + ' ' + str(maxPoints) + ' poena')
        
    print('')
    print('Math Katedra za racunarstvo i informatiku: ')
    maxYear = 0
    maxPoints = -1
    for entry in matfRiPoints:
        print(str(entry) + ' ' + str(matfRiPoints[entry]) + ' poena')
        if matfRiPoints[entry] > maxPoints:
            maxPoints = matfRiPoints[entry]
            maxYear = entry
    print('----------------------------------------------------------------------')
    print('Najuspesnija godina za Math Katedra za racunarstvo i informatiku ' + str(maxYear) + ' ' + str(maxPoints) + ' poena')
    print('')
    pass

def bestFaculties():
    with open(CVSReaderMethods.PublicationsFilePath) as publicationsFile:
        next(publicationsFile) #skip first line
        csvReader = csv.reader(publicationsFile, delimiter = ',')

        fonSiArtPoints = 0
        fonIsArtPoints = 0
        etfRtiArtPoints = 0
        matfRiArtPoints = 0

        fonSiConfPoints = 0
        fonIsConfPoints = 0
        etfRtiConfPoints = 0
        matfRiConfPoints = 0

        for row in csvReader:
            authorsString = row[3]
            authors = authorsString.lower().split(' and ')
            article = False
            conf = False

            if row[5] == 'Article' or row[5] == 'Article in Press':
                article = True
            elif row[5] == 'Conference Paper':
                conf = True
            else:
                continue

            for author in authors:
                author = author.lower().strip()
                department = None

                if author in CVSReaderMethods.authorsFullNamesWithMiddle:
                    authorInfo = CVSReaderMethods.authorsFullNamesWithMiddle[author]
                    department = authorInfo[1]
                    
                elif author in CVSReaderMethods.authorsFullNamesWithoutMiddle: 
                    authorInfo = CVSReaderMethods.authorsFullNamesWithoutMiddle[author]
                    department = authorInfo[1]

                elif author in CVSReaderMethods.authorsShortNamesWithMiddle:
                    authorInfo = CVSReaderMethods.authorsShortNamesWithMiddle[author]
                    department = authorInfo[1]

                elif author in CVSReaderMethods.authorsShortNamesWithoutMiddle:
                    authorInfo = CVSReaderMethods.authorsShortNamesWithoutMiddle[author]
                    department = authorInfo[1]
                
                if department == 'katedra za racunarstvo i informatiku':
                    if article:
                        matfRiArtPoints = matfRiArtPoints + 1
                    elif conf:
                        matfRiConfPoints = matfRiConfPoints + 1

                elif department == 'katedra za racunarsku tehniku i informatiku':
                    if article:
                        etfRtiArtPoints = etfRtiArtPoints + 1
                    elif conf:
                        etfRtiConfPoints = etfRtiConfPoints + 1

                elif department == 'Katedra za informacione sisteme':
                    if article:
                        fonIsArtPoints = fonIsArtPoints + 1
                    elif conf:
                        fonIsConfPoints = fonIsConfPoints + 1
                
                elif department == 'Katedra za softversko inzenjerstvo':
                    if article:
                        fonSiArtPoints = fonSiArtPoints + 1
                    elif conf:
                        fonSiConfPoints = fonSiConfPoints + 1

    print('Zadatak 3')
    print('----------------------------------------------------------------------')
    print('Konferencije: ')
    print('\tFon Katedra za softversko inzinjerstvo: ' + str(fonSiConfPoints) + ' poena')
    print('\tFon Katedra za informacione sisteme: ' + str(fonIsConfPoints) + ' poena')
    print('\tEtf katedra za racunarsku tehniku i informatiku: ' + str(etfRtiConfPoints) + ' poena')
    print('\tMatf katedra za racunarstvo i informatiku: ' + str(matfRiConfPoints) + ' poena')

    print('Casopisi: ')
    print('\tFon Katedra za softversko inzinjerstvo: ' + str(fonSiArtPoints) + ' poena')
    print('\tFon Katedra za informacione sisteme: ' + str(fonIsArtPoints) + ' poena')
    print('\tEtf katedra za racunarsku tehniku i informatiku: ' + str(etfRtiArtPoints) + ' poena')
    print('\tMatf katedra za racunarstvo i informatiku: ' + str(matfRiArtPoints) + ' poena')
    print('')
    pass
