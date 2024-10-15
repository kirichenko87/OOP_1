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



class Librarian():
    def __init__(self, 
                 name: str, 
                 id_librian: int, 
                 list_readers: list[Reader],
                 ):
        
        self.name = name
        self.id_librian = id_librian
        self.list_readers = list_readers
        
    
    def export_book(self, book):
        self.reader.add_book_list_book(book)
        
        
    def import_book(self, book):
        self.reader.back_book_library(book)
        


class Library():
    def __init__(self, 
                 book:Book, 
                 reader: Reader, 
                 librarean: Librarian):
        
        self.book = book
        self.reader = reader
        self.librarean = librarean
        
        
    def find_book(self, find):
        result = "Книга не найдена"
        if self.book.autor == find or self.book.name_book == find:
            if self.book.status_book == True:
                result = "Книга успешно найдена"
        return result
    
            
    def add_new_book(self, title: str, autor: str, publication: int):
        self.book.name_book = title
        self.book.autor = autor
        self.book.publication_year = publication
        self.book.set_status(True)

        
class programm:
    
    @staticmethod
    def main():
        b1 = Book("Тихий Дон", "Шолохов М", 1930, 200, False )
        b2 = Book("А зори здесь тихие", "Васильев", 1969, 500, False)
        b3 = Book("Идиот", "Тургенев", 1890, 200, False)
        r1 = Reader("Кириченко", 19324, b1)
        l1 = Librarian("Семенова", 12343, r1)
        bi = Library([b1.autor, b2.autor, b3.autor], r1, l1)
        print(b1.autor)
        
        