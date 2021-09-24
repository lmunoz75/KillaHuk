import sys
import numpy as np 
#from GUI_ui import*
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer, QTime
import time

qtCreatorFile = "Interfaz.py"

class MiApp(QMainWindow):
    def __init__(self):               
        
        super().__init__()              
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.grafica = Canvas_grafica()        
        self.ui.grafica_uno.addWidget(self.grafica)
        
        timer=QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        
    def displayTime(self):
        currentTime=QTime.currentTime()
        displayText=currentTime.toString('hh:mm:ss')        
        #self.clk.setText(displayText)
        
class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1,dpi=100, figsize=(5,5), 
                                         sharey=True, facecolor='white')
        super().__init__(self.fig)
        
        ff = 440      
        fm = 8000     
        tm = 1 / fm  
        t = 3 
        
        t_vec = np.arange(0, t, tm)
        y = np.sin(2 * np.pi * ff * t_vec).astype(np.float32)      
       
        
        self.ax.plot(t_vec,y, linewidth=1.5)
        self.ax.set_title("Simulation", color='black',fontsize=12)
        self.ax.grid(True,linestyle='--')
        self.ax.set_xlim(0,3/ff)        
        #self.ax.set_ylim()
        #self.ax.set_facecolor("#072d0d")
        #self.ax.set_xticklabels(["e"])
        #self.ax.set_yticklabels(["a"])
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())

#%%
x=np.linspace(0,1035,207)
print(x)