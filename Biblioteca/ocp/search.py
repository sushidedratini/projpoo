from typing import List

from data.external_catalog_adapter import ExternalCatalogAdapter
from srp.book import Book

class BookSearch:
    def __init__(self):
        self.external_adapter = ExternalCatalogAdapter()

    def search_by_title(self, books: List[Book], title: str, external: bool=False):
        # Primeiro, busca na coleção local
        local_books = [book for book in books if title in book.title]
        if local_books:
            return local_books
        
        # Se externo, procura em outra base
        if external:
            return self.search_by_external_source(title)
        return []

    def search_by_author(self, books, author):
        return [book for book in books if book.author == author]

    def search_by_category(self, books, category):
        return [book for book in books if book.category == category]
    
    def search_by_external_source(self, title):
        # Se não encontrar, busca na API externa
        external_books = self.external_adapter.search_by_title(title)
        if external_books:
            return external_books
        return []