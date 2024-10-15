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
        

        

class Reader():
    def __init__(self, 
                 name: str, 
                 id_ticket: int, 
                 list_book: list,
                 ):
        
        self.name = name
        self.id_ticket = id_ticket
        self.list_book = list_book
        
    
    def add_book_list_book(self, new_book):
        self.list_book.append(new_book)
        
        
    def back_book_library(self,del_book):
        if len(self.list_book) > 0:
            result = "Книга не найдена"
            for book in self.list_book:
                if book == del_book:
                    self.list_book.remove(del_book)
                    result = "Книга успешно возвращена"
        return result           

