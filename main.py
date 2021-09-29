#! python
from pymongo import MongoClient
from pprint import pprint
import sys
import pyperclip 

def initDb():
    client=MongoClient('mongodb://localhost/')
    db=client.tboxdb
    return db

def onRootCommand(db, name):
    object = db.projects.find_one({"name": name})
    if object != None:
        pyperclip.copy('cd ' + object.get("root"))
        pprint("root folder for " + name + " command copied to clipboard")
    else:
        pprint("project does not exist!")


def processCommand(db, command, args):
    if command == "root":
        onRootCommand(db, args[0])

#now we can start the main code 
db = initDb()

if len(sys.argv) == 1: 
    exit("usage tooldb action args")

args = sys.argv[1:len(sys.argv)]
command = args[0]

processCommand(db, command, args[1:len(args)])