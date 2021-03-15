class Book:
    def __init__(self, name, author, issue_date, theme, type_):
        self.bookName = name
        self.bookAuthor = author
        self.bookIssue_date = issue_date
        self.bookTheme = theme
        self.bookType = type_

    def showInfo(self):
        print(self.bookName, "\t", self.bookAuthor, "\t", self.bookIssue_date, "\t", self.bookTheme, "\t", self.bookType)

x = Book("紅玫瑰與白玫瑰", "張愛玲", "1944年", "愛情", "小說")
x2 = Book("小王子", "安托萬·聖修伯里", "1943(R&H)/1945(Gallimard)", "童話", "兒童文學")
x3 = Book("傲慢與偏見", "珍·奧斯汀", "1813年", "觀點主義", "小說")
x.showInfo()
x2.showInfo()
x3.showInfo()

