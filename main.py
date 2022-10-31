
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_MainWindow
from carre import  Ui_Carre_Dialog
from rectangle import Ui_Rectangle_Dialog
import sys

# Fonction pour afficher les fenettres
def afficheRectangle():
   Rectangle_Dialog.show() 

def afficheCarre():
    Carre_Dialog.show()   


# Fonction pour les calculs des surfaces 

def surfaceRectangle():
    L = int(ui_rectangle.longueur.text())
    l = int(ui_rectangle.largueur.text())
    surface = L*L
    ui_rectangle.resultat.setText(str(surface))

def surfaceCarre():
    c = int(ui_carre.cote.text())
    surface = c*c
    ui_carre.resultat.setText(str(surface))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# affichage des fenettre
Carre_Dialog = QtWidgets.QDialog()
ui_carre = Ui_Carre_Dialog()
ui_carre.setupUi(Carre_Dialog)

Rectangle_Dialog = QtWidgets.QDialog()
ui_rectangle = Ui_Rectangle_Dialog()
ui_rectangle.setupUi(Rectangle_Dialog)

# Excution des Fonction d'affichages
ui.btn_rectangle.clicked.connect(afficheRectangle)
ui.btn_carre.clicked.connect(afficheCarre)

# excution des fonction de calculs

ui_rectangle.btn_valider.clicked.connect(surfaceRectangle)
ui_carre.btn_valider.clicked.connect(surfaceCarre)
sys.exit(app.exec_())
