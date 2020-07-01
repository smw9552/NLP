from urllib.request import urlopen
import math

class pubmed:

    def extract_PMID_by_two_keywords(self, Keywords):

        try:
            # access pubmed website & search papers by using keywords
            Pubmed_Info_URL = "http://pubmed.ncbi.nlm.nih.gov/?term=" + str(Keywords[0]) + str('+') + str(Keywords[1])
            Pubmed_Info = urlopen(Pubmed_Info_URL, None, timeout=100000)

            # extract all result page number
            while True:
                Info_line = Pubmed_Info.readline()
                if not Info_line: break

                if str(Info_line).__contains__(str('''<meta name="log_resultcount" content=''')):
                    result = str(Info_line).\
                        replace('''b'    <meta name="log_resultcount" content="''', '').\
                        replace('''" />''', '').\
                        replace('\\n', '').\
                        replace("'", '')

                    # 1 page 마다 10개의 PMID 결과가 제공 되기 때문에 10으로 나누어서 정리.
                    page_result = int(result) / 10
                    # 10으로 나눈 뒤 소수점 올림 처리 진행 (누락되는 데이터를 막기 위함)
                    page_result = int(math.ceil(page_result))
                    print(page_result)

            # extract all PMID List (각각의 page에서 PMID 추출, range 함수의 마지막 기준 숫자보다 -1 값으로 for문이 돌아가기 때문에 +1 처리
            PMID_List = []
            for ai in range(1, page_result+1):

                print(str("PMID search page= ") + str(ai))
                Pubmed_PMID_URL = "http://pubmed.ncbi.nlm.nih.gov/?term=" + str(Keywords[0]) + str('+') + str(Keywords[1]) + str("&page=") + str(ai)

                Pubmed_PMID = urlopen(Pubmed_PMID_URL, None, timeout=1000000)

                while True:
                    line = Pubmed_PMID.readline()
                    if not line: break

                    if str(line).__contains__(str(">PMID: <span class=")):

                        PMID = str(line).replace('''b'  <span class="citation-part">PMID: <span class="docsum-pmid">''','').\
                            replace("</span></span>", '').\
                            replace('\\n', '').\
                            replace("'", '')

                        print(PMID)

                        PMID_List.append(PMID)
                        Final_PMID_List = sorted(list(set(PMID_List)))

        except TimeoutError:
            print("Time out error")

        except Exception:
            print ("Error")


        return Final_PMID_List





