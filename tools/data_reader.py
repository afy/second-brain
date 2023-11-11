import json

# Nodes: Category data, titles, atc


class DataReader:
    def __init__(self, _path):
        self.path = _path
        self.nodeLookup = {}
        self.files = {
            "nodes": "nodes.json",
            "page": "/pages/"
        }


    def readNodes(self) -> dict:
        with open(self.path+self.files["nodes"], "r") as i:
            self.nodeLookup = json.load(i)
        return self.nodeLookup


    def nodeExists(self, node) -> dict: 
        return node not in self.nodeLookup.keys()


    def readPage(self, node):
        print(f"test key {node}")


    def writeTestIndex(self):
        d = {}
        d["IT"] = {
            "Networks": {
                "Ethernet": 0
            },
            "Algorithms": {
                "Djikstras": 0 # What to do with leaf nodes?
            }
        }
        d["Maths"] = {

        }
        d["Arts"] = {
            "Architecture": {}
        }
        with open(self.path+self.files["nodes"], "w") as o:
            json.dump(d, o)