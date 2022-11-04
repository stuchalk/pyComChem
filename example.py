from comchem import *
import json

rundef = "cas2png"

if rundef == "props":
    # gets the properties for the CASRN requested
    cmpd = detail("9003-07-0", "properties")
    print(json.dumps(cmpd, indent=4))
    exit()

if rundef == "trifl":
    # gets a list of all compounds starting with "trifluoro*"
    hits = query("trifluoro*")
    print(hits)

if rundef == "key2cas":
    # convert a substance CASRN into its InChIKey
    casrn = key2cas('UHOVQNZJYSORNB-UHFFFAOYSA-N')
    print(casrn)

if rundef == "cas2png":
    # create a png of a molecule based on its CASRN (via SVG from ComChem)
    chemimg("57-83-0", 'png')
