import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

ccpath = 'https://commonchemistry.cas.org/api/'
fields = ['name', 'image', 'inchi', 'inchikey', 'smile', 'canonicalSmile', 'molecularFormula', 'molecularMass',
          'properties', 'synonyms', 'replaceRns', 'hasMolefile']


# get data from a page
def detail(casrn, field="all"):
    """ access the common chemistry detail api """
    url = ccpath + 'detail?cas_rn=' + casrn
    respnse = urlopen(url)
    jsn = json.loads(respnse.read())

    if field == "all":
        return jsn
    elif field in fields:
        if field == "properties":
            properties = {}
            properties.update({"properties": jsn['experimentalProperties']})
            properties.update({"citations": jsn['propertyCitations']})
            return properties
        else:
            return jsn[field]
    else:
        return "Field not available..."


# run a search
def query(term):
    url = ccpath + 'search?q=' + term
    respnse = urlopen(url)
    jsn = json.loads(respnse.read())
    out = []
    for hit in jsn['results']:
        textname = BeautifulSoup(hit["name"], "lxml").text
        out.append({"textname": textname, "htmlname": hit["name"].lower(), "rn": hit["rn"]})
    return out


# search for a compound using an InChIKey
def key2cas(key):
    """ search the api for an InChKey"""
    hits = query('InChIKey=' + key)
    return hits[0]['rn']  # only returns the casne of the first hit
