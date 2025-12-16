from PyQt6.QtWidgets import QApplication,QVBoxLayout,QLabel,QWidget,QGridLayout, \
    QPushButton,QLineEdit,QComboBox,QMainWindow,\
    QTableWidget,QTableWidgetItem,QDialog,QToolBar,QStatusBar,\
    QMessageBox
       
       
from PyQt6.QtCore import Qt       
from PyQt6.QtGui import QAction,QIcon
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Student Management System")
        
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item =self.menuBar().addMenu("&Edit")
        
        
        
        add_edit_action = QAction(QIcon("/pngs/search.png"),"Search",self)
        edit_menu_item.addAction(add_edit_action)
        add_edit_action.triggered.connect(self.search_student)
        add_edit_action.setMenuRole(QAction.MenuRole.NoRole)
        
        
        add_student_action = QAction(QIcon("/pngs/add.png"),"Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        
        
        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)
        
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
        # create toolbar and add tool bar elem
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(add_edit_action)
        
        # CREATE STATUS BAR AND ADD STATUS BAR ELEM
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        
        # detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)
        
    def about(self):
        dialog = AboutDialog()
        dialog.exec()
        
        
    def search_student(self):
        dialog2 = SearchDialog()
        dialog2.exec()
        
    
    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)
        
        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)  
        
        children = self.findChildren(QPushButton) 
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)
    
    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()
    
        
    def edit(self):
        dialog = EditDialog()
        dialog.exec()    
        
    def load_data(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        data1 = cursor.fetchall()
        self.table.setRowCount(0)
        
        for row_number, row_data in enumerate(data1):
            self.table.insertRow(row_number)
            for column_number ,data  in enumerate(row_data):
                self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
        conn.close()
        
    def insert(self):
        dialog = InsertDialog()  
        dialog.exec()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        self.index = main_window.table.currentRow()
        self.student_id = main_window.table.item(self.index,0).text()
        student_name = main_window.table.item(self.index,1).text()
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        selected_course = main_window.table.item(self.index,2).text()
        
        courses =["Biology","Math","Astronomy","Physics"]
        self.course_name = QComboBox()
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(selected_course)
        
        layout.addWidget(self.course_name)
        
        
        
        current_mobile = main_window.table.item(self.index,3).text()
        
        self.mobile = QLineEdit(current_mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)
        
        button = QPushButton("Submit")
        button.clicked.connect(self.update)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    
    def update(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute("UPDATE students SET name = ? , course = ?, mobile = ? WHERE id = ?",(self.student_name.text(), self.course_name.itemText(self.course_name.currentIndex()), self.mobile.text(), self.student_id))
        
        conn.commit()
        cursor.close()
        conn.close()

        main_window.load_data()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")
        
        
        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to delete?")
        yes = QPushButton("YES")
        no = QPushButton("NO")
        
        layout.addWidget(confirmation,0,0,1,2)
        layout.addWidget(yes,1,0)
        layout.addWidget(no,1,1)
        
        self.setLayout(layout)
        
        yes.clicked.connect(self.delete_cell)
        no.clicked.connect(self.no)
        
    
    
    def delete_cell(self):
        index = main_window.table.currentRow()
        student_id = main_window.table.item(index,0).text()
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute('DELETE from students WHERE id = ? ',(student_id,))
        
        conn.commit()
        cursor.close()
        conn.close()
        main_window.load_data()
        
        self.close()
        
        comfirmation_widget = QMessageBox()
        comfirmation_widget.setWindowTitle("Success")
        comfirmation_widget.setText("The record was deleted")
        comfirmation_widget.exec()
    
    
    def no(self):
        self.close()    
        

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        content = """
        This app is for student data from a sqlite.db
        """
        self.setText(content)
 
      
        
class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        
        self.student_query =QLineEdit()
        self.student_query.setPlaceholderText("Name")
        layout.addWidget(self.student_query)
        
        
        button = QPushButton("Search")
        button.clicked.connect(self.search_query)
        layout.addWidget(button)
        
        
        self.setLayout(layout)
    def search_query(self):
        name = self.student_query.text()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        result = cursor.execute('SELECT * FROM students WHERE name = ?',(name,))
        rows = list(result)
        
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        
        for item in items:
            main_window.table.item(item.row(),1).setSelected(True)
        

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)
        
        courses =["Biology","Math","Astronomy","Physics"]
        self.course_name = QComboBox()
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)
        
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)
        
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO students (name , course, mobile) VALUES (?,?,?)',
                       (name,course,mobile)) 
        conn.commit()
        cursor.close()
        conn.close()
        main_window.load_data()
        
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())                    