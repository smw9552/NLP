from urllib.request import urlopen

Single_PMID = "28483577"
PMIDs = []

Pubtator_Info_URL = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=28483577"

Pubtator_Info = urlopen(Pubtator_Info_URL, None, timeout=100000)

while True:
    Info_line = Pubtator_Info.readline()
    if not Info_line: break

    print(Info_line)