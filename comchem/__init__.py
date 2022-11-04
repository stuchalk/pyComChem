import json
import re
import cairosvg
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

ccpath = 'https://commonchemistry.cas.org/api/'
fields = ['name', 'image', 'inchi', 'inchikey', 'smile', 'canonicalSmile', 'molecularFormula',
          'molecularMass', 'properties', 'synonyms', 'replaceRns', 'hasMolefile']


def detail(casrn, field="all"):
    """
    Access the Common Chemistry detail API at
    https://commonchemistry.cas.org/api/detail?cas_rn=<casrn>
    :param casrn: CAS Registry Number
    :param field: field to return or all fields (default)
    :return mixed
    """
    if not _validcas(casrn):
        return ''  # false
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
        return ''  # false


def query(term='', exact=False):
    """
    Search the CommonChemistry database API at
    https://commonchemistry.cas.org/api/search?q=<term>
    :param term: string to be searched
    :param exact: boolean to indicate an exact match
    :return: string
    """
    url = ''
    if _validkey(term):
        url = ccpath + 'search?q=InChIKey=' + term  # InChIKey search
    elif exact is False and term[-1:] != '*':
        url = ccpath + 'search?q=' + term + '*'
    elif term[-1:] == '*' or exact is True:  # is the last char of term a '*'?
        url = ccpath + 'search?q=' + term
    respnse = urlopen(url)
    jsn = json.loads(respnse.read())
    out = []  # false
    if jsn['results']:
        for hit in jsn['results']:
            textname = BeautifulSoup(hit["name"], "lxml").text
            out.append({"textname": textname, "htmlname": hit["name"].lower(), "rn": hit["rn"]})
    return out


def key2cas(key):
    """
    Find the CAS Registry Number of a chemical substance using an IUPAC InChIKey
    :param key - a valid InChIKey
    """
    if _validkey(key):
        hits = query('InChIKey=' + key, True)
        if hits:
            if len(hits) == 1:
                return hits[0]['rn']
            else:
                # check hits for smallest molar mass compound, i.e., not polymer
                minmm = 100000
                minrn = ''
                for i, hit in enumerate(hits):
                    mm = detail(hit['rn'], 'molecularMass')
                    if mm != '':
                        if float(mm) < minmm:
                            minmm = float(mm)
                            minrn = hit['rn']
                return minrn
        else:
            return ''
    else:
        return ''


def chemimg(chemid='', imgtype='svg'):
    """
    Get an image for a compound from either a CAS Registry Number, InChIKey, SMILES, or name
    :param chemid: the CAS Registry Number, InChIKey, SMILES, or name
    :param imgtype: the type of image file to produce - svg, png, or ps
    :return:
    """
    # check identifier for type so checking can be done
    if chemid == '':
        return False
    if _validkey(chemid):
        casrn = key2cas(chemid)
    elif not _validcas(chemid):
        casrn = query(chemid, True)
    else:
        casrn = chemid
    if not casrn:
        return casrn
    # get svg data and save
    svg = detail(casrn, "image")
    f = open(casrn + ".svg", "w")
    f.write(svg)
    f.close()
    if imgtype == 'png':
        cairosvg.svg2png(url=casrn + ".svg", write_to=casrn + ".png")
    elif imgtype == 'ps':
        cairosvg.svg2ps(url=casrn + ".svg", write_to=casrn + ".ps")
    if imgtype == 'png' or imgtype == 'ps':
        if os.path.exists(casrn + ".svg"):
            os.remove(casrn + ".svg")
    return True


def _validkey(key):
    """
    Validate and IUPAC InChIKey
    :param key: a string to be validated as an IUPAC InChIKey
    :return: bool
    """
    test = re.search(r'^[A-Z]{14}-[A-Z]{8}[SN]A-[A-Z]$', key)
    if test is None:
        return False
    return True


def _validcas(cas):
    """
    Validate a CAS Registry Number
    See: https://en.wikipedia.org/wiki/CAS_Registry_Number#Format
    :param cas: a string to be validated as a CAS Registry Number
    :return: bool
    """
    test = re.search(r'^\d{2,8}-\d{2}-\d$', cas)
    # if format of string does not match then it's not CAS RN
    if test is None:
        return False
    # verify check digit
    reverse = cas[::-1]  # reverse the CAS Registry Number (needed for checksum math and split out checksum)
    digits = reverse.replace('-', '')  # remove the dashes
    nochk = digits[1:]  # all but first digit
    chksum = int(digits[:1])  # first digit
    total = 0
    for i, digit in enumerate(nochk):
        total += (i + 1) * int(digit)  # index of chars starts at 0
    newsum = total % 10
    if newsum == chksum:
        return True
    else:
        return False
