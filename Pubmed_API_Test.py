from urllib.request import urlopen
from urllib.error import HTTPError
import socket


#Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=ESR1+breast+cancer"
Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=ESR1%20breast%20cancer&page=50"

Pubmed_Info = urlopen(Pubmed_Info_URL, None, timeout = 1000000)

while True:
    Info_line = Pubmed_Info.readline()
    if not Info_line: break

    #Result 숫자 추출

    #if str(Info_line).__contains__(str('''<meta name="log_resultcount" content=''')):
    #    print(Info_line)

    #PMID 값 추출
    if str(Info_line).__contains__(str(">PMID: <span class=")):
        #print(Info_line)

        print(str(Info_line).replace('''b'  <span class="citation-part">PMID: <span class="docsum-pmid">''','').
              replace("</span></span>",'').
              replace('\\n','').
              replace("'",''))