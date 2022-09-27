import pdfplumber as paper

import sys
sys.stdout = open('output.txt','wt')

with paper.open('sample.pdf') as sample:
    for pg, page in enumerate(sample.pages, start=1):
        print(f'{pg}')
        data = page.extract_text()
        print(data.strip())
        print('_'*45)
    