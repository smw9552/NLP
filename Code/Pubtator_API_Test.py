import nltk
from urllib.request import urlopen
from nltk import word_tokenize



Single_PMID = "24964572"
PMIDs = ["28483577", "24964572", "27283605"]

Pubtator_Info_URL = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids=24964572"

Pubtator_Info = urlopen(Pubtator_Info_URL, None, timeout=100000)

Title = []
Abstract = []
Bioconcept_Gene = []
Bioconcept_Disease = []
Bioconcept_Chemical = []
Bioconcept_Mutation = []
Bioconcept_Species = []
Bioconcept_Cellline = []

while True:
    Info_line = Pubtator_Info.readline()
    if not Info_line: break

    #Abstract tokenization
    if str(Info_line).__contains__("|a|"):

        print(Info_line)

        Abstract = str(Info_line).replace('\\n','').\
            replace(str(Single_PMID),"").\
            replace("|a|","").lower().\
            replace('b"','').\
            replace('"','').\
            split(".")

        print(Abstract)

        #Abstract를 tokenization 진행
        #tokens = word_tokenize(str(Abstract))
        #print(tokens)

        #text = nltk.Text(tokens)
        #text.concordance("Garlic", 100, 100)
print("\n")
print("\n")


# 두 키워드를 포함하는 sentence 추출
for info in Abstract:

    if str(info).__contains__(str("garlic").lower()) and str(info).__contains__(str("cancer").lower()):
        #print("Extraction")
        #print(str(info).strip())
        Data = str(info).strip()

print(Data)

data_tokens = word_tokenize(str(Data))
print(data_tokens)

inter_data_token = data_tokens[int(data_tokens.index('garlic'))+1:int(data_tokens.index('cancer'))-1]


#Tokenization 진행 후 관련된 단어를 포함하는지에 대한 여부로 두 keyword 사이의 연관성을 비교 분석

key = "treatment"

for inter_data in inter_data_token:
    print(inter_data)
    if str(inter_data) == str(key):
        correlation = True
    elif str(inter_data) == str(key):
        correlation = False

print(correlation)

"""

    #Bioconcept filtering (Gene, Disease, Chemical, Mutation, Species, Celline)
    #if str(Info_line).__contains__("Species"):
    #    print(str(Info_line)) 
    """