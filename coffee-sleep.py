import csv
import numpy as np
import plotly.express as px

def getDataSource(dataPath):
    coffeeSales = []
    sleep = []
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            coffeeSales.append(float(row['Coffee']))
            sleep.append(float(row['Sleep']))
    return{'x':coffeeSales,'y':sleep}        
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print("Correlation between Coffee vs Sleep :- \n--->",correlation[0,1])
def plotFigure(dataPath):
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        fig = px.scatter(csvReader,x='Coffee',y='Sleep')
        fig.show()    
def setUp():
    dataPath = 'coffee-sleep.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
setUp()    
