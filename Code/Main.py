from Code.Data import data
from Code.Pubmed import pubmed
from Code.Pubtator import pubtator

DATA = data()
PUBMED = pubmed()
PUBTATOR = pubtator()

# Space = %20, Comma = +
#Keywords = DATA.input_two_keywords(str("garlic%20extract"), str("anticancer"))

#PMID_List = PUBMED.extract_PMID_by_two_keywords(Keywords)

Test_PMID = ["24964572", "28483577"]

Titles = []

Titles = PUBTATOR.get_paper_title(Test_PMID)

print(Titles)
