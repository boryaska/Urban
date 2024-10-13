class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        # print(self.file_names)

    def get_all_words(self):
        import string
        dct = dict()
        table = str.maketrans("", "", string.punctuation)

        for file in self.file_names:
            lst = []
            with open(file, encoding='utf-8') as txt:
                for line in txt:
                    string = line.lower()
                    edit_string = string.translate(table)
                    lst.extend(edit_string.split())
            dct[file] = lst
        return dct
    
    def find(self, word):
        dct = dict()
        info_dct = WordsFinder.get_all_words(self)
        for a, b in info_dct.items():
            index = b.index(word.lower()) + 1
            dct[a] = index

        return dct    

    def count(self, word):
        dct = dict()
        info_dct = WordsFinder.get_all_words(self)
        for a, b in info_dct.items():
            count = b.count(word.lower())
            dct[a] = count

        return dct    
    
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего