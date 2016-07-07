# Manage dialogs for IBM Watson Dialog Service on Bluemix
#
# This is a simple Python script I developed to manage my
# dialogs when testing the IBM Watson Dialog Service on Bluemix.
# The script takes some command line arguments and then calls
# the related service API. The entire result is always dumped.
#
# Some of the source is taken from this SDK example:
# https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/dialog_v1.py
#
# Author: Henrik Loeser

import json,argparse
from os.path import join, dirname
from watson_developer_cloud import DialogV1

# Credentials are read from a file
with open("config.json") as confFile:
     config=json.load(confFile)['credentials']

# Initialize the dialog with username & password
dialog = DialogV1(
    username=config['username'],
    password=config['password'])

# Define parameters that we want to catch and some basic command help
def getParameters(args=None):
   parser = argparse.ArgumentParser(description='Process my Watson Dialog Commands',prog='henriksDialog')
   parser.add_argument("--register","-r", dest='registerDialog', action='store_true',
                       help='--register -dn diaglogName -f dialogFile')
   parser.add_argument("--list", "-l",dest='listDialog', action='store_true',
                       help='--list')
   parser.add_argument("--converse", "-c",dest='startDialog', action='store_true',
                       help='--converse -id dialogID')
   parser.add_argument("--update", "-u",dest='updateDialog', action='store_true',
                       help='--update -id dialogID -f dialogFile')
   parser.add_argument("--delete", "-d",dest='deleteDialog', action='store_true',
                       help='--delete -id dialogID')
   parser.add_argument("-f", "--file", dest="dialogFile",
                    help="read dialog file from here", metavar="FILE")
   parser.add_argument("-id", "--id", dest="dialogID",
                    help="dialog ID")
   parser.add_argument("-dn", "--dialogname", dest="dialogName",
                    help="dialog name")


   parms = parser.parse_args()
   return parms

# Register a dialog
def registerDialog(dialogFile,dialogName):
  with open(join(dirname(__file__), dialogFile)) as dialog_file:
     print(json.dumps(dialog.create_dialog(
         dialog_file=dialog_file, name=dialogName), indent=2))

# List available dialogs
def listDialog():
   print(json.dumps(dialog.get_dialogs(), indent=2))

# Update an existing dialog, requires dialog ID for now
def updateDialog(dialogFile,dialogID):
   with open(join(dirname(__file__), dialogFile)) as dialog_file:
     print(json.dumps(dialog.update_dialog(dialog_file=dialog_file, dialog_id=dialogID), indent=2))

# Delete an existing dialog, requires dialog ID for now
def deleteDialog(dialogID):
  print(json.dumps(dialog.delete_dialog(dialog_id=dialogID), indent=2))


# Start a dialog and converse with Watson
def converse(dialogID):
  print "Starting a dialog, stop by Ctrl+C"
  print "=================================\n"
  # Start the dialog
  resp = dialog.conversation(dialogID)
  # Output is printed. It is not pretty, but takes care of all parts...
  print resp['response']
  # Now loop to chat
  while True:
    dinput = raw_input("Please enter:\n")
    resp=dialog.conversation(dialog_id=dialogID,
                             dialog_input=dinput,
                             conversation_id=resp['conversation_id'],
                             client_id=resp['client_id'])
    print resp['response']

#
# Main program, for now just detect what function to call
#
if __name__ == '__main__':
    parms = getParameters()
    print parms
    if (parms.registerDialog and parms.dialogFile):
       registerDialog(parms.dialogFile,parms.dialogName)
    if (parms.listDialog):
       listDialog()
    if (parms.updateDialog and parms.dialogID and parms.dialogFile):
       updateDialog(parms.dialogFile,parms.dialogID)
    if (parms.deleteDialog and parms.dialogID):
       deleteDialog(parms.dialogID)
    if (parms.startDialog and parms.dialogID):
       converse(parms.dialogID)
