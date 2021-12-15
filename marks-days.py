import csv
import numpy as np
import plotly.express as px

def getDataSource(dataPath):
    marks = []
    days = []
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            marks.append(float(row['Marks']))
            days.append(float(row['Days']))
    return{'x':marks,'y':days}        
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print("Correlation between Marks obtained vs Class Attened :- \n--->",correlation[0,1])
def plotFigure(dataPath):
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        fig = px.scatter(csvReader,x='Marks',y='Days')
        fig.show()    
def setUp():
    dataPath = 'marks-days.csv'
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)
setUp()    
