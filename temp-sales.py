import csv
import numpy as np
import plotly.express as px

def getDataSource(dataPath):
    icecreamSales = []
    temperature = []
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            icecreamSales.append(float(row['Ice-cream']))
            temperature.append(float(row['Temperature']))
    return{'x':icecreamSales,'y':temperature}        
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print("Correlation between Temperature vs Ice Cream Sales :- \n--->",correlation[0,1])
def plotFigure(dataPath):
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        fig = px.scatter(csvReader,x='Temperature',y='Ice-cream')
        fig.show()    
def setUp():
    dataPath = 'temp-sales.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
setUp()    
