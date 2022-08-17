class vscode():
    def excute(self):
        print("compling")
        print("running")
class myeditor():

    def excute(self):
        print("spell cheack")
        print("conventional cheack")
        print("compling")
        print("running")
class labtop:

    def code(self,ide):
        ide.excute()

idetype=myeditor()# we can only change this calling to change the editor type
lab=labtop()
lab.code(idetype) #passed argument for ide type

#the above is duk type polymorphism