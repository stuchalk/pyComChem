from comchem import *
import json

cmpd = detail("9003-07-0", "properties")
print(json.dumps(cmpd, indent=4))
exit()

hits = query("trifluoro*")
print(hits)

casrn = key2cas('UHOVQNZJYSORNB-UHFFFAOYSA-N')
print(casrn)

chemimg("71-43-2", 'png')
