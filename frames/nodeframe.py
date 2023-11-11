import customtkinter
from tkinter import *

class NodeViewerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.build()
        self.buttons = {}

    def build(self):
        pass

    def nodeButtonPressed(self, node):
        print(node)

    def buildNewNodes():
        pass

    def setInitialNodes(self, nodes):
        for node in nodes.keys():
            b = customtkinter.CTkButton(self, text = node, command = lambda n = node: self.nodeButtonPressed(n))
            b.pack(side=TOP, fill=X)
            self.buttons[node] = b

        print(self.buttons)