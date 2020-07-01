from urllib.request import urlopen
from urllib.error import HTTPError
import socket
import math

#Keyword 파일 읽어서 추출하는 코드도 작성 필요
Single_Keyword = ""
Keywords = []


#최초 URL 접근해서 result page 숫자 추출

#Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=ESR1+breast+cancer"
#Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=RAS%2C+Wnt%2C+e3+ligase"
Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=Allium+sativum+anticancer"
#Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=ESR1%20breast%20cancer&page=50"

Pubmed_Info = urlopen(Pubmed_Info_URL, None, timeout=1000000)

while True:
    Info_line = Pubmed_Info.readline()
    #print(Info_line)
    if not Info_line: break

    #Result 숫자 추출
    if str(Info_line).__contains__(str('''<meta name="log_resultcount" content=''')):

        result = str(Info_line).\
            replace('''b'    <meta name="log_resultcount" content="''','').\
            replace('''" />''','').\
            replace('\\n','').\
            replace("'",'')

        # 1 page 당 10개의 PMID 정보 제공됨, result는 전체 데이터 숫자이고 페이지 당 10개씩 나오기 때문에 10으로 나누어서 정리
        page_result = int(result) / 10

        page_result = int(math.ceil(page_result))
        print(page_result)


PMID_List = []

#각 page에서 PMID 추출, range 함수의 마지막 기준 숫자보다 -1 값으로 for문이 돌기 때문에 +1값 처리 진행
for ai in range(1, page_result+1):
    print(str("page") + str(ai) + str("\n"))
    Pubmed_Info_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=ESR1%20breast%20cancer&page=" + str(ai)

    Pubmed_Info = urlopen(Pubmed_Info_URL, None, timeout = 1000000)

    while True:
        Info_line = Pubmed_Info.readline()
        if not Info_line: break

    #PMID 값 추출
        if str(Info_line).__contains__(str(">PMID: <span class=")):
            #print(Info_line)

            PMID = str(Info_line).replace('''b'  <span class="citation-part">PMID: <span class="docsum-pmid">''','').\
                replace("</span></span>",'').\
                replace('\\n','').\
                replace("'",'')

            print(PMID)

            PMID_List.append(PMID)

            Final_PMID_List = sorted(list(set(PMID_List)))

print(str("Extract PMID"))



print(PMID_List)
print(len(PMID_List))
print(PMID_List[2])
print(PMID_List[10])