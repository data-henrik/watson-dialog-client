# henriksDialog

### Manage dialogs for IBM Watson Dialog Service on Bluemix

This is a simple Python script I developed to manage my dialogs when testing the IBM Watson Dialog Service on Bluemix.
The script takes some command line arguments and then calls the related service API. The entire result is always dumped.

Some of the source is taken from this SDK example:
https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/dialog_v1.py

(More to come, first the code... ;)

In order to get started, you will need to have the watson-developer-cloud module installed:
```
pip install watson-developer-cloud
```

## Some usage examples

### Invoke Help
```
python henriksDialog.py -h
usage: henriksDialog [-h] [--register] [--list] [--update] [--delete]
                     [-f FILE] [-id DIALOGID] [-dn DIALOGNAME]

Process my Watson Dialog Commands

optional arguments:
  -h, --help            show this help message and exit
  --register, -r        --register -dn diaglogName -f dialogFile
  --list, -l            --list
  --update, -u          --update -id dialogID -f dialogFile
  --delete, -d          --delete -id dialogID
  -f FILE, --file FILE  read dialog file from here
  -id DIALOGID, --id DIALOGID
                        dialog ID
  -dn DIALOGNAME, --dialogname DIALOGNAME
                        dialog name
```

### List available dialogs
```
python henriksDialog.py --list
Namespace(deleteDialog=False, dialogFile=None, dialogID=None, dialogName=None, listDialog=True, registerDialog=False, updateDialog=False)
{
  "dialogs": [
    {
      "dialog_id": "d9e886ab-xxx-yyyy-zzz-abcdef2e52df4", 
      "name": "pizza"
    }, 
    {
      "dialog_id": "f8be984c-xxxx-yyyy-zzzz-abcdef9f0fa8", 
      "name": "henrikdialog1"
    }
  ], 
  "language_packs": [
    {
      "dialog_id": "en-us-legacy", 
      "name": "en-us-legacy"
    }, 
    {
      "dialog_id": "ar-sa", 
      "name": "ar-sa"
    }, 
    {
      "dialog_id": "es-es", 
      "name": "es-es"
    }, 
    {
      "dialog_id": "pt-br", 
      "name": "pt-br"
    }, 
    {
      "dialog_id": "de-de", 
      "name": "de-de"
    }, 
    {
      "dialog_id": "cs-cz", 
      "name": "cs-cz"
    }, 
    {
      "dialog_id": "en-us", 
      "name": "en-us"
    }, 
    {
      "dialog_id": "it-it", 
      "name": "it-it"
    }, 
    {
      "dialog_id": "fr-fr", 
      "name": "fr-fr"
    }, 
    {
      "dialog_id": "ja-jp", 
      "name": "ja-jp"
    }
  ]
}
```
### Create/register a new dialog
```
python henriksDialog.py --register -f henrikDialog1.xml -dn myDialog
Namespace(deleteDialog=False, dialogFile='henrikDialog1.xml', dialogID=None, dialogName='myDialog', listDialog=False, registerDialog=True, updateDialog=False)
{
  "dialog_id": "fb528f9f-xxxx-yyyy-zzz-abcdef1c52879"
}
```

