from PyQt6.QtWidgets import QApplication,QVBoxLayout,QLabel,QWidget,QGridLayout,QPushButton,QLineEdit
import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age calculator!")
        grid = QGridLayout()
        
        
        # create widgets
        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()
        
        date_label = QLabel("Date of birth (MM/DD/YYYY): ")
        self.date_birth_line_edit = QLineEdit()
        calculate_button = QPushButton("Calculate age")
        self.output_label = QLabel("")
        
        calculate_button.clicked.connect(self.calculate_age)
        
        grid.addWidget(name_label,0,0)
        grid.addWidget(self.name_line_edit,0,1)
        grid.addWidget(date_label,1,0)
        grid.addWidget(self.date_birth_line_edit,1,1)
        grid.addWidget(calculate_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)
        
        
        

        self.setLayout(grid)
    
    
    def calculate_age(self):
        
        current_year = datetime.now().year
        date_birth = self.date_birth_line_edit.text()
        year_birth = datetime.strptime(date_birth,"%m/%d/%Y").date().year
        age = current_year-year_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")
    
    
app = QApplication(sys.argv)    
age_calculator = AgeCalculator()    

age_calculator.show()
sys.exit(app.exec())