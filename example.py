from comchem import *
import json


def props(casrn='57-83-0'):
    # gets the properties for the CASRN requested
    cmpd = detail(casrn, "properties")
    return cmpd


def trifl():
    # gets a list of all compounds starting with "trifluoro*"
    hits = query("trifluoro*")
    print(hits)


def key2casrn(key):
    # convert a substance CASRN into its InChIKey
    # uses code to find the lowest molecular weight hit for the InChIkey
    casrn = key2cas(key)
    print(casrn)


def cas2png(casrn='57-83-0'):
    # create a png of a molecule based on its CASRN (via SVG from ComChem)
    chemimg(casrn, 'png')
    print('image saved to ' + casrn + '.py')


subs = ['57-83-0', '71-43-2', '118-96-7']
for sub in subs:
    out = props(sub)
    print(json.dumps(out, indent=4))

# key2cas('UHOVQNZJYSORNB-UHFFFAOYSA-N')
# trifl()
# cas2png('57-83-0')
