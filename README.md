## pyComChem
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
- additional specialized functions
