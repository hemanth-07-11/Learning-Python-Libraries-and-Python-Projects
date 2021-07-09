import os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    component = QQmlComponent(engine)
    component.loadUrl(QUrl("qmlmain.qml"))

    window = component.create()
    if window:
        window.show()
    else:
        for error in component.errors():
            print(error.toString())

    sys.exit(app.exec_())
