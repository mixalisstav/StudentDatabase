from PyQt6.QtWidgets import QApplication,QVBoxLayout,QLabel,QWidget,QGridLayout,QPushButton,QLineEdit,QComboBox
import sys
from datetime import datetime


class AvarageDistance(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Avarage Speed Calculator")
        grid = QGridLayout()
        self.unit = ""
        
        # create widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()
        
        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()
        
        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")
        
        calculate_button.clicked.connect(self.calculate_distance)
        
        combo = QComboBox()
        combo.addItems(['Imperial(miles)', 'Metric(km)'])

        if combo.currentText() == 'Imperial(miles)':
            self.speed = "mph"
            self.unit = "mph"
        if combo.currentText() == 'Metric(km)':
            self.speed = "km"
            self.unit = "km/h"
            
        grid.addWidget(distance_label,0,0)   
        grid.addWidget(self.distance_line_edit,0,1)
        grid.addWidget(combo,0,2)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.time_line_edit,1,1)
        grid.addWidget(calculate_button,2,1,1,1)
        grid.addWidget(self.output_label,3,0,1,2)
        
        self.setLayout(grid)
        
        
    def calculate_distance(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        
        speed = distance/time
    
        if self.speed == "km":
            spped = round(speed, 2)
            
            
        
        if self.speed == "mph":
            speed = round(speed*0.621371 , 2)
            
            
            
            
        self.output_label.setText(f"Avarage Speed: {speed} {self.unit}")    
                
           
            
app = QApplication(sys.argv)
avarage_distance = AvarageDistance()
avarage_distance.show()
sys.exit(app.exec())            