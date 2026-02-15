# pyComChem
A Python package to access data via the CommonChemistry.org API.

A revised version of the CommonChemistry website, originally at commonchemistry.org, has been redeveloped
into a much larger (~500K) database of CAS Registry Numbers and now includes an API for programmatic access.

This package provides access to the API to search the database and extract chemical metadata, images, and mol files.

Currently available commands are:
- query - search either and exact string or substring
- detail - full metadata retrieval
- key2cas - specialized function to return the CAS Registry Number of a compound from its InChIKey
- chemimg - download structural images an `.svg`, `.png`, or `.ps` files

Future improvements will include
- molfile - download the mol file of a compound

## Configuration
Before running this package, sign up on the [Common Chemistry website](https://www.cas.org/services/commonchemistry-api) for an API KEY

## Updates
- updated the code to handle the CAS addition of an APIKey (2/15/26)

## Presentation
“Supporting the global community with CAS common chemistry” Andrea Jacobs, Stuart Chalk, Leah McEwen, 
Amy Liu, Ka Wing Kelly Cao paper presented at the ACS Virtual Meeting, March 2022