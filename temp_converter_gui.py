# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:54:10 2024

@author: PaganM
"""


from PyQt5 import QtWidgets as qtw
import sys
import temp_converter_functionality

class MainWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       

        self.username_input = qtw.QLineEdit()
        self.username_input2 = qtw.QLineEdit()

        
        '''
        self.username_input = qtw.QLineEdit() creates the boxes where the user
        would input their information. This is done three times to create unique
        input boxes. This uses the packages PyQt5.
        '''
        
    
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Run')
        
        '''
        self.cancel_button and self.submit_button were created here and inside the 
        QPushButton function they were named. These names then appeared on the respective
        buttons.        
        
        '''
        
        layout = qtw.QFormLayout()
        layout.addRow('Degree Input', self.username_input)
        layout.addRow('Metric Input', self.username_input2)

        
        '''
        This adds text directing the user next to what each input text box
        is for.
        '''
        
        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        layout.addRow('', button_widget)        
        self.setLayout(layout)
        
        '''
        The above text creates a layout for where the buttons should go.
        '''
        
        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.temp_func)
        
        '''
        This above text adds functionality to the close and the run button. The 
        function from the below function which is pulling the function from the script
        roll_call_self_everywhere. This should
        then run through the .py file and pull all of the neccessary information.
        '''
        
#        
    def temp_func(self):
        ''' 
        when the submit button is clicked, this function will be called. What
        you want to happen is for the input fields to be plugged into your
        function below
        '''


        self.degree = float(self.username_input.text())
        self.metric = self.username_input2.text()
        outp = temp_converter_functionality.tempfunction(self.degree, self.metric) 
        outp.runtemp()
        temp_result = outp.temp_result
        qtw.QMessageBox.information(self, "Conversion: ", temp_result)
        

        '''
        The function up above connects each of the variables in the .py file with the 
        GUI script that was created up above. The outp variable takes the self.direct,
        self.csv, and self.output and runs them in the runrc() function. After this is
        all completed successfully, the QMessageBox pops up and alerts the user that it ran
        correctly and to check their directory.
        '''

        
    
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='Temp Calculator')
    w.show()
    sys.exit(app.exec_())
    
    
    
    '''
    This gives the window a name which in this case is 'Roll Call' and after
    running the program it will exit out.
    '''