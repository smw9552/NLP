from Code.Data import data
from Code.Pubmed import pubmed

DATA = data()
PUBMED = pubmed()

# Space = %20, Comma = +
Keywords = DATA.input_two_keywords(str("garlic%20extract"), str("anticancer"))

PMID_List = PUBMED.extract_PMID_by_two_keywords(Keywords)

print(PMID_List)
print(len(PMID_List))