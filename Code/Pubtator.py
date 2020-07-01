from urllib.request import urlopen
from nltk import word_tokenize

class pubtator:

    def get_paper_title(self, PMID_List):

        Paper_Title_List = []

        try:
            for ai in range(0, len(PMID_List)):

                #print(PMID_List[ai])

                Pubtator_Info_URL = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=" + str(PMID_List[ai])
                Pubtator_Info = urlopen(Pubtator_Info_URL, None, timeout=100000)

                while True:
                    Info_line = Pubtator_Info.readline()
                    if not Info_line: break

                    if str(Info_line).__contains__(str(PMID_List[ai])+str("|t|")):

                        Title = str(Info_line).replace('\\n','').\
                            replace(str(PMID_List[ai]),'').\
                            replace('|t|','').\
                            replace("b'","").\
                            replace("'","")

                        Paper_Title_List.append(str(Title))

        except TimeoutError:
            print("Timeout error")

        except Exception:
            print("Error")

        return Paper_Title_List


    def get_paper_abstract(self, PMID_List):

        Paper_Abstract_List = []

        try:
            for ai in range(0, len(PMID_List)):
                Pubtator_Info_URL = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=" + str(PMID_List[ai])
                Pubtator_Info = urlopen(Pubtator_Info_URL, None, timeout=100000)

                while True:
                    Info_line = Pubtator_Info.readline()
                    if not Info_line: break

                    if str(Info_line).__contains__(str(PMID_List[ai]) + str("|a|")):

                        Abstract = str(Info_line).replace('\\n', '').\
                            replace(str(PMID_List[ai]),''). \
                            replace('|a|', '').lower().\
                            replace("b'", "").\
                            replace("'", "").\
                            split(".")

                        #str(Abstract) 진행하게 되면 들어가는 데이터에 \가 포함되는 문제가 발생함
                        Paper_Abstract_List.append(Abstract)


        except TimeoutError:
            print("Timeout error")

        except Exception:
            print("Error")

        return Paper_Abstract_List