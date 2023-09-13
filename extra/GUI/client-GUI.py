import sys
import time
import random
import csv
from ui_mainwindow import Ui_MainWindow
from PySide6            import QtCore, QtWidgets, QtGui
from PySide6.QtCore     import Qt, QPointF, QThread
from PySide6.QtGui      import QPainter
from PySide6.QtWidgets  import QApplication, QMainWindow, QBoxLayout
from PySide6.QtCharts   import QLineSeries, QChart, QChartView




#adding a backgroundtimer that waits a certain amount of time
class BackgroundTimer(QThread):
  def __init__(self, duration):
    super().__init__()
    self.duration = duration
  
  def run(self):
    time.sleep(self.duration)


#Initialising the chart
class MyWidget(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    
    #Adding a maximum value for the zoom to work properly
    self.max = 5
    self.tick = 0
    
    # QLineSeries for datapoints
    self.series = QLineSeries()  
    self.series2 = QLineSeries()
    self.series3 = QLineSeries()
    self.series4 = QLineSeries()
    self.series5 = QLineSeries()



    # Füge mehrere Datenpunkte hinzu

    
    # QChart für Beschreibung des Kurvendiagrams
    self.chart = QChart()          # Erzeuge die Beschreibung eines Kurvendiagrams
    self.chart.addSeries(self.series)
    self.chart.addSeries(self.series2)
    self.chart.addSeries(self.series3)
    self.chart.addSeries(self.series4)
    self.chart.addSeries(self.series5)   # Füge Datenpunkte hinzu
    self.chart.legend().hide()     # Verstecke Legende
    self.chart.createDefaultAxes() # Automatische Achsenbeschriftung
    self.chart.setTitle("Einfaches Kurvendiagram") # Diagramtitel
    
    # QChartView zum Darstellen des Kurvendiagrams
    self.chartView = QChartView(self.chart) # Erzeuge eine Darstellungsform des Kurvendiagrams
    self.chartView.setRenderHint(QPainter.Antialiasing)  # Kantenglättung aktivieren
    
    #
    # Layout zusammenstecken
    #
    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.addWidget(self.chartView)
    
    #
    # Subjekte und Observer verbinden
    #
    

    
    # Hintergrundtimer
    self.backgroundtimer = BackgroundTimer(0.5)
    self.add_pt_to_chart()

  def add_pt_to_chart(self):
    self.tick = self.tick + 1
    maxValue = 0
    values = []
    with open('values.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            a = float(row[0])
            values.append(a)

    maxValue = max(values)
   
    
    self.series.append(self.tick, values[0])    # Füge einen Datenpunkt hinzu
    self.series2.append(self.tick, values[1])    # Füge einen Datenpunkt hinzu
    self.series3.append(self.tick, values[2])    # Füge einen Datenpunkt hinzu
    self.series4.append(self.tick, values[3])    # Füge einen Datenpunkt hinzu
    self.series5.append(self.tick, values[4]) 

    if(maxValue > self.max):
        self.max = (self.max / 0.7)
        self.chart.zoom(0.7)

            
   
    
    # Auch wenn es nicht direkt nachvollziehbar ist, liefert die Funktion
    # axes(...) ein QList<QAbstractAxis>-Objekt.
    # Wir nehmen das letzte Element dieser Liste und das ist ein QAbstractAxis-Objekt.
    self.chart.axes(Qt.Horizontal)[-1].setMax(self.tick)
    self.chart.axes(Qt.Horizontal)[-1].setMin(max(0, self.tick-20))
    
    self.backgroundtimer.start() # Starte Hintergrundtimer im Hintergrund

class MainWindow(QMainWindow):
   def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        chart = MyWidget()
        chart.show()

   





      

if __name__ == "__main__":
  app = QtWidgets.QApplication([])
 
  window = MainWindow()
  window.show()


  sys.exit(app.exec())
