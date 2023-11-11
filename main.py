from tkinter import *
import customtkinter
import os

from tools.data_reader import DataReader
from frames.nodeframe import NodeViewerFrame
from frames.entryframe import EntryFrame


class App:
    def __init__(self): 
        self.sizex = 800
        self.sizey = 600

        self.root = customtkinter.CTk()
        self.root.title = "Second brain"
        self.root.geometry("{}x{}".format(self.sizex, self.sizey))
        self.root.resizable(False, False)
        self.buildMainPage()

        self.dataReader = DataReader(os.getcwd()+"\data\ ")
        self.dataReader.writeTestIndex() # Remove once past testing
        self.nodes = self.dataReader.readNodes()
        self.frame_node.setInitialNodes(self.nodes)
        self.root.mainloop()
        

    def buildMainPage(self):
        self.frame_node = NodeViewerFrame(self.root, width = self.sizex/3)
        self.frame_node.pack(side=LEFT, fill=Y)
        self.frame_entry = EntryFrame(self.root)
        self.frame_entry.pack(side=RIGHT, fill=BOTH, expand=True)


    def loadPage(self, node):
        if not self.dataReader.nodeExists(node): raise Exception("Invalid node")
        
        data = self.dataReader.readPage(node)
        self.frame_entry.setEntry(data)



if __name__ == "__main__":
    App()