#! /usr/bin/env python3

import io
import csv
import glob
import re

import requests

import datapackage
from jsontableschema import infer

simple_metadata_url = 'http://discovery.ucl.ac.uk/cgi/export/eprint/1469811/Simple/discovery-eprint-1469811.txt'

def download():
    data_csv_list = [
        "http://discovery.ucl.ac.uk/1469811/2/EUROEVOL09-07-201516-34_FaunalSpecies.csv",
        "http://discovery.ucl.ac.uk/1469811/3/EUROEVOL09-07-201516-34_FaunalTaxaList.csv",
        "http://discovery.ucl.ac.uk/1469811/4/EUROEVOL09-07-201516-34_FaunalBiometrics.csv",
        "http://discovery.ucl.ac.uk/1469811/5/EUROEVOL09-07-201516-34_FaunalBones.csv",
        "http://discovery.ucl.ac.uk/1469811/6/EUROEVOL09-07-201516-34_FaunalPhases.csv",
        "http://discovery.ucl.ac.uk/1469811/7/EUROEVOL09-07-201516-34_C14Samples.csv",
        "http://discovery.ucl.ac.uk/1469811/8/EUROEVOL09-07-201516-34_CommonPhases.csv",
        "http://discovery.ucl.ac.uk/1469811/9/EUROEVOL09-07-201516-34_CommonSites.csv",
        "http://discovery.ucl.ac.uk/1469811/10/EUROEVOL09-07-201516-34_ABotPhases.csv",
        "http://discovery.ucl.ac.uk/1469811/11/EUROEVOL09-07-201516-34_ABotSamples.csv",
        "http://discovery.ucl.ac.uk/1469811/13/EUROEVOL09-07-201516-34_ABotTaxaList.csv",
        "http://discovery.ucl.ac.uk/1469811/14/EUROEVOL-13-07-2015-ABotSites.csv"]

    fields_csv_list = [
        "http://discovery.ucl.ac.uk/1469811/15/Manning_ABotPhases_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/16/Manning_ABotSamples_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/17/Manning_ABotSites_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/18/Manning_ABotTaxaList_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/19/Manning_C14Samples_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/20/Manning_CommonPhases_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/21/Manning_CommonSites_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/22/Manning_FaunalBiometrics_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/23/Manning_FaunalBones_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/24/Manning_FaunalPhases_fields.csv",
        "http://discovery.ucl.ac.uk/1469811/26/Manning_FaunalSpecies_fields.csv"]

    for url in data_csv_list:
        r = requests.get(url)
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
        with io.open('data/{}'.format(fname), 'w') as f:
            f.write(r.text)

    for url in fields_csv_list:
        r = requests.get(url)
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
        with io.open('archive/{}'.format(fname), 'w') as f:
            f.write(r.text)


#download()

dp = datapackage.DataPackage()
dp.descriptor['name'] = 'euroevol09'
dp.descriptor['title'] = 'EUROEVOL09'
dp.descriptor['resources'] = []

for filepath in glob.glob('data/*.csv'):

    with io.open(filepath) as stream:
        headers = stream.readline().rstrip('\n').split(',')
        values = csv.reader(stream)
        schema = infer(headers, values)
        dp.descriptor['resources'].append(
            {
                'name': 'data',
                'path': filepath,
                'schema': schema
            }
        )


with open('../datapackage.json', 'w') as f:
  f.write(dp.to_json())

