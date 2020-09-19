from PyQt5 import QtWidgets

types = {
    'info': QtWidgets.QMessageBox.Information,
    'question': QtWidgets.QMessageBox.Question,
    'warning': QtWidgets.QMessageBox.Warning,
    'critical': QtWidgets.QMessageBox.Critical,
}

class DialogFactory:
    def __init__(self, title, message, type=None, ok_button=None):
        self.msg = QtWidgets.QMessageBox()
        
        if type == None:
            self.set_icon('info')
        else:
            self.set_icon(type)
        
        if ok_button == True:
            self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        
        self.msg.setWindowTitle(title)
        self.msg.setText(message)
    
    def set_icon(self, type):
        if type in types:
            self.msg.setIcon(types[type])
            return True
        
        raise ValueError(f"Invalid type. Valid types: {', '.join(types.keys())}")
    
    def show(self):
        self.msg.show()
        
    def wait(self):
        self.msg.exec_()
        
    def close(self):
        self.msg.close()
        
        