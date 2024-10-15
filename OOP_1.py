class Book():
    def __init__(self, 
                 name_book: str, 
                 autor: str, 
                 publication_year: int, 
                 pages_book: int, 
                 status_book: bool
                 ):
        
        self.name_book = name_book
        self.autor = autor
        self.publication_year = publication_year
        self.pages_book = pages_book
        self.status_book = status_book       
        
        
    def set_status(self, status):
        self.status_book = status
            

    def __str__(self):
        return(self.name_book, self.autor, self.publication_year)
