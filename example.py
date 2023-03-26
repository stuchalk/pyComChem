from comchem import *
import json


def props(casrn='57-83-0'):
    # gets the properties for the CASRN requested
    cmpd = detail(casrn, "properties")
    print(json.dumps(cmpd, indent=4))

def trifl():
    # gets a list of all compounds starting with "trifluoro*"
    hits = query("trifluoro*")
    print(hits)

def key2cas():
    # convert a substance CASRN into its InChIKey
    # uses code to find the lowest molecular weight hit for the InChIkey
    casrn = key2cas('UHOVQNZJYSORNB-UHFFFAOYSA-N')
    print(casrn)

def cas2png(casrn='57-83-0'):
    # create a png of a molecule based on its CASRN (via SVG from ComChem)
    chemimg(casrn, 'png')
    print('image saved to ' + casrn + '.py')

trifl()
