class book:
    def __init__(self, name, author, year_published, editor):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.editor = editor

dune = book("Dune", "Frank Herbert", "1965", "Chilton book")
fellowship_ring = book("The Fellowship of the Ring", "J.R.R. Tolkien", "1954", "George Allan & Unwin")
two_towers = book("The Two Towers", "J.R.R. Tolkien", "1954", "George Allen & Unwin")
return_king = book("The Return of the King", "J.R.R. Tolkien", "1954", "George Allen & Unwin")

print(dune.name + ", " + dune.author)