class Books:
    def __init__(self, name, author, year_published, editor):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.editor = editor

dune = Books("Dune", "Frank Herbert", "1965", "Chilton Books")
fellowship_ring = Books("The Fellowship of the Ring", "J.R.R. Tolkien", "1954", "George Allan & Unwin")
two_towers = Books("The Two Towers", "J.R.R. Tolkien", "1954", "George Allen & Unwin")
return_king = Books("The Return of the King", "J.R.R. Tolkien", "1954", "George Allen & Unwin")