import csv
import numpy as np
import plotly.express as px

def getDataSource(dataPath):
    tvSize = []
    time = []
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            tvSize.append(float(row['TV-Size']))
            time.append(float(row['Time']))
    return{'x':tvSize,'y':time}        
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print("Correlation between Size of Tv vs Tv watch hours :- \n--->",correlation[0,1])
def plotFigure(dataPath):
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        fig = px.scatter(csvReader,x='TV-Size',y='Time')
        fig.show()    
def setUp():
    dataPath = 'tv-time.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
setUp()    
