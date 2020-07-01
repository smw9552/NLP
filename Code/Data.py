class data:

    def input_one_keyword(self, keyword1):

        Keyword = []
        Keyword.append(str(keyword1))

        return Keyword

    def input_two_keywords(self, keyword1, keyword2):

        Keywords = []
        Keywords.append(str(keyword1))
        Keywords.append(str(keyword2))

        return Keywords

    def input_three_keywords(self, keyword1, keyword2, keyword3):

        Keywords = []
        Keywords.append(str(keyword1))
        Keywords.append(str(keyword2))
        Keywords.append(str(keyword3))

        return Keywords

    def read_keyword_txt_files(self, FilePath, FileName, col):

        Keywords = []
        f_keyword = open(FilePath + FileName, 'r')

        while True:
            line = f_keyword.readline()
            if not line: break
            new_line = line.strip("\t")

            Keywords.append(str(new_line[int(col)]).strip())

        return Keywords

    def read_keyword_csv_files(self, FilePath, FileName, col):

        Keywords = []
        f_keyword = open(FilePath + FileName, 'r')

        while True:
            line = f_keyword.readline()
            if not line: break
            new_line = line.strip(",")

            Keywords.append(str(new_line[int(col)]).strip())

        return Keywords

