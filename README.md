# henriksDialog

### Manage and test dialogs for IBM Watson Dialog Service on Bluemix

This is a simple Python script I developed to manage my dialogs when testing the IBM Watson Dialog Service on Bluemix.
The script takes some command line arguments and then calls the related service API. The entire result is always dumped.

Another feature of the script is to test a dialog by using the `--converse` option. The Watson statement is displayed and it is possible to enter a reply that is sent back to the Watson Dialog Service.

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
usage: henriksDialog [-h] [--register] [--list] [--converse] [--update]
                     [--delete] [-f FILE] [-id DIALOGID] [-dn DIALOGNAME]

Process my Watson Dialog Commands

optional arguments:
  -h, --help            show this help message and exit
  --register, -r        --register -dn diaglogName -f dialogFile
  --list, -l            --list
  --converse, -c        --converse -id dialogID
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

### Converse, chat with Watson
I registered a dialog (the pizza example) and now started the chat by providing the dialog ID.
```
python henriksDialog.py -c -id fb528f9f-xxxx-yyyy-zzz-abcdef1c52879
Namespace(deleteDialog=False, dialogFile=None, dialogID='fb528f9f-xxxx-yyyy-zzz-abcdef1c52879', dialogName=None, listDialog=False, registerDialog=False, startDialog=True, updateDialog=False)
Starting a dialog, stop by Ctrl+C
=================================

[u"Hi, I'm Watson! I can help you order a pizza, what size would you like?"]

Please enter:
What sizes do you have
[u'We have small, medium, large and extra large, as well as all the normal toppings.', u'', u'What size would you like?']

Please enter:
I take a large pizza
[u'', u'What toppings are you in the mood for? (Limit 4)']

Please enter:
what toppings do you have
[u'We have cheese, pepperoni, olives, mushrooms, etc.', u'', u'What toppings are you in the mood for? (Limit 4)']

Please enter:
ok, I take a extra large pizza with salami, tuna and cheese
[u'', u'Do you prefer pickup or delivery?']

Please enter:
for here
[u'I didnt grasp what you said.', u'', u'Do you prefer pickup or delivery?']

Please enter:
I will pick it up
[u'Ok, I have one Large Cheese pizza for pickup. Is that correct?']

Please enter:
no
[u"Oops! Let's start over. What size would you like?"]

Please enter:
extra large
[u'', u'What toppings are you in the mood for? (Limit 4)']

Please enter:
cheese and mushrooms
[u'', u'Do you prefer pickup or delivery?']

Please enter:
delivery
[u'Ok, I have one extra large Cheese & Mushrooms pizza for delivery. Is that correct?']

Please enter:
yes
[u'Sounds good! Your pizza will be ready in 20 minutes. Do you want to order another?']

Please enter:
no, but how are you
[u'Okay, thank you for your order! Just let me know if you want to place another order.']

Please enter:
how are you
[u"I'm great thanks.", u'', u'What size would you like?']
```

