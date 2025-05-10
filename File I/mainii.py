class Library:
    def __init__(self, list, name):
        self.booklist=list
        self.name=name
        self.lend={}
    def displaybook(self):
        print(f"We have the following books in the library: {self.name}")
        for book in self.booklist:
            print(book)
    
    def lendbook(self, user, book):
        if book not in self.lend.keys():
            self.lend.update({book: user})
            print("lender book database was updated successfully")
