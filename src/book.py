class Book:
    def __init__(self, author, name, pages):
        self.author = author
        self.name = name
        self.pages = pages

    def get_author(self):
        return self.author

    def get_name(self):
        return self.name

    def get_pages(self):
        return self.pages

    def __str__(self):
        return self.author + ", " + self.name + ", " + str(self.pages) + " pages"