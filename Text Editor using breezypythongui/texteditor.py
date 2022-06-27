'''
Author: Ranjul Arumadi
'''
from breezypythongui import EasyFrame

class TextEditor(EasyFrame):
    def __init__(self):

        EasyFrame.__init__(self,title="Text Editor")
        self.setResizable(True)
        self.setBackground("#252526")
        self.addButton(text="OPEN",row=1,column=0,command=self.optext)
        self.addButton(text="NEW",row=1,column=1,command=self.newtext)
        self.addButton(text="SAVE",row=1,column=2,command=self.svtext)
        self.output=self.addTextArea("",row=4,column=0,columnspan=3,height=15)
        
    def optext(self):
        try:
            self.filename = self.prompterBox(title = "",
     promptString = "Please enter file name",
     inputText = "",
     fieldWidth = 20)
            fi=self.filename
            if fi=="":
                self.messageBox(title = "ERROR",
     message = "File name not entered!",
     width = 25,
     height = 5)
            else:
                f=open(fi,'r')
                fc=f.read()
                self.output.setText(fc)
                f.close()
        except FileNotFoundError:
            self.messageBox(title = "ERROR", message = "File does not exist!")

    def newtext(self):
        self.output.setText("")

    def svtext(self):
        try:
            self.filename = self.prompterBox(title = "",
     promptString = "Please enter file name",
     inputText = "",
     fieldWidth = 20)
            new=self.output.getText()
            fi=self.filename
            f=open(fi,'w')
            f.write(new)
            f.close()
        except FileNotFoundError:
            self.messageBox(title = "ERROR", message = "Enter file name!")

def main():
        TextEditor().mainloop()

if __name__=="__main__":
        main()

