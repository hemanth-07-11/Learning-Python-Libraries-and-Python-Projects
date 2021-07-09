import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
                             QPushButton, QLineEdit, QLabel, QTabBar, QFrame,
                             QStackedLayout, QTabWidget, QShortcut, QKeySequenceEdit)
from PyQt5.QtGui import QIcon, QWindow, QImage, QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__
    def mouse_press(self, e):
        self.selectAll()

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")

        self.create_app()
        self.setMinimumSize(1366, 768)
        self.setBaseSize(1366, 786)
        self.setWindowIcon(QIcon("TA logo BLK.png"))

    def create_app(self):

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.shortcut_newtab = QShortcut(QKeySequence("Ctrl+t"), self)
        self.shortcut_newtab.activated.connect(self.add_tab)

        self.shortcut_reload = QShortcut(QKeySequence("Ctrl+r"), self)
        self.shortcut_reload.activated.connect(self.reload_page)

        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.close_tab)
 
        self.tabbar.tabBarClicked.connect(self.switch_tab)

        self.tabbar.setCurrentIndex(0)
        self.tabbar.setDrawBase(False)


        self.tab_count = 0
        self.tabs = []

  
        self.toolbar = QWidget()
        self.toolbar.setObjectName("Toolbar")
        self.toolbar_layout = QHBoxLayout()
        self.addressbar = AddressBar()


        self.addressbar.returnPressed.connect(self.browse_to)

        self.add_tab_button = QPushButton("+")
        self.add_tab_button.clicked.connect(self.add_tab)

        self.back_button = QPushButton("<-")
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton("->")
        self.forward_button.clicked.connect(self.go_forward)

        self.reload_button = QPushButton("R")
        self.reload_button.clicked.connect(self.reload_page)


        self.toolbar.setLayout(self.toolbar_layout)
        self.toolbar_layout.addWidget(self.back_button)
        self.toolbar_layout.addWidget(self.forward_button)
        self.toolbar_layout.addWidget(self.reload_button)
        self.toolbar_layout.addWidget(self.addressbar)
        self.toolbar_layout.addWidget(self.add_tab_button)


        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)


        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)
        self.add_tab()
        self.show()

    def close_tab(self, i):
        self.tabbar.removeTab(i)


    def add_tab(self):
        i = self.tab_count

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].layout.setContentsMargins(0, 0, 0, 0)

        self.tabs[i].setObjectName("tab" + str(i))


        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://wwww.bing.com"))


        # Update title text, icon, address bar
        self.tabs[i].content.titleChanged.connect(lambda: self.set_tab_content(i, "title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.set_tab_content(i, "icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.set_tab_content(i, "url"))

        # Add webview content to layout (good for developer tools)
        self.tabs[i].splitview = QSplitter()
        self.tabs[i].splitview.setOrientation(Qt.Vertical)
        self.tabs[i].layout.addWidget(self.tabs[i].splitview)


        # Set top level tab from list to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        # Add tab to top level stacked Widget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # Show tab at top of screen, set tab data to website of tab
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i, {"object": "tab" + str(i), "initial": i})

        self.tabbar.setCurrentIndex(i)

        # Add to tab count
        self.tab_count += 1

    def switch_tab(self, i):
        # Get tab data, return object name want to switch to
        tab_data = self.tabbar.tabData(i)["object"]

        # If tab data exists, can click on tabs
        if self.tabbar.tabData(i):
            # Make tab index static
            tab_widget = self.findChild(QWidget, tab_data)
            self.container.layout.setCurrentWidget(tab_widget)

            # Change url in address bar with tab change
            new_url = tab_widget.content.url().toString()
            self.addressbar.setText(new_url)

    def browse_to(self):
        # Get text in address bar
        text = self.addressbar.text()

        # Get index # of current tab, get tab name, get webview associate with name
        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)["object"]
        web_view = self.findChild(QWidget, tab).content

        # Check if address or search term
        if "http" not in text:
            if "." not in text:
                url = "https://www.bing.com/search?q=" + text
            else:
                url = "http://" + text
        else:
            url = text

        web_view.load(QUrl.fromUserInput(url))

    def set_tab_content(self, i, type):

        tab_name = self.tabs[i].objectName()

        count = 0
        running = True

        current_tab = self.tabbar.tabData(self.tabbar.currentIndex())["object"]

        if current_tab == tab_name and type == "url":
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.addressbar.setText(new_url)
            return False

        while running:
            # Get tab data
            tab_data_name = self.tabbar.tabData(count)

            if count >= 99:
                running = False

            if tab_name == tab_data_name["object"]:
                if type == "title":
                    new_title = self.findChild(QWidget, tab_name).content.title()
                    self.tabbar.setTabText(count, new_title)
                elif type == "icon":
                    new_icon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabbar.setTabIcon(count, new_icon)
                running = False
            else:
                count += 1

    def go_back(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()

    def go_forward(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()

    def reload_page(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create environment var to enable developer tools, set to port number or IP with port nubmer
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = "667"

    window = App()

    # Open stylesheet
    with open ("stylesheet.css", "r") as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec_())
