#!/usr/bin/python3

# Obtains sentences with copyright from the ukWac and brWaC corpus to build the Noun Compound Senses (NCS) dataset.

import sys
import re
import os.path
from argparse import ArgumentParser
import pandas as pd

from data.utils import read_data, read_en_corpus, read_pt_corpus

arg_parser = ArgumentParser(
    description='This script generates the files with the original sentences of the NCS datasets. It requires the ukWaC and/or brWaC corpora to get the sentences with copyright from them.'
)

arg_parser.add_argument(
    '--lang',
    '-l',
    type=str,
    choices=['en', 'pt'],
    help='Language of the dataset: English (en) or Portuguese (pt)',
    required=True,
    default=None
)

arg_parser.add_argument(
    '--corpus',
    '-c',
    type=str,
    required=True,
    help='ukWaC/brWaC corpus. brWaC should be in .conll format. UKWAC as a single file concatenating all the XML files.',
    default=None
)

args = arg_parser.parse_args()
lang = args.lang
corpf = args.corpus

# Input file (sentences and IDs)
if lang == 'en':
    inpf = './input/sentids_en.csv'
elif lang == 'pt':
    inpf = './input/sentids_pt.csv'

# Read sentence ids
nc_ids = pd.read_csv(inpf)

# Get target ids and compounds
target_ids, compounds = read_data(nc_ids, lang)

# Reads corpus
if lang == 'en':
    compounds = read_en_corpus(target_ids, compounds, corpf)
elif lang == 'pt':
    compounds = read_pt_corpus(target_ids, compounds, corpf)

# Output
fname = 'original_sents.csv'
outf = os.path.join('dataset', lang, 'naturalistic', fname)

if os.path.exists(outf):
    ans = 'y'
    ans = input('File %s will be overwritten. Proceed? (y/n) [DEFAULT: y]' %outf)
    if ans == 'n' and ans == 'no':
        exit(0)
        
out = open(outf, 'w+')

# Print head
out.write('"compound","compositionality","sentence1","sentence2","sentence3"\n')
for c in compounds:
    out.write('"{}","{}",'.format(c, compounds[c]['comp']))
    if 'sent1' in compounds[c]:
        out.write('"{}",'.format(compounds[c]['sent1']))
    else:
        out.write(',')
    if 'sent2' in compounds[c]:
        out.write('"{}",'.format(compounds[c]['sent2']))
    else:
        out.write(',')
    if 'sent3' in compounds[c]:
        out.write('"{}"\n'.format(compounds[c]['sent3']))
    else:
        out.write('\n')
out.close()
print('File %s created' %outf)
