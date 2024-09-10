import requests

from srp.book import Book

class ExternalCatalogAdapter:
    BASE_URL = "http://openlibrary.org/search.json"

    def search_by_title(self, title):
        response = requests.get(self.BASE_URL, params={"title": title})
        if response.status_code == 200:
            return self._convert_to_books(response.json())
        return []

    def _convert_to_books(self, data):
        books = []
        for doc in data.get('docs', []):
            title = doc.get('title')
            author = doc.get('author_name', ['Unknown'])[0]
            category = doc.get('subject', ['Unknown'])[0]
            books.append(Book(title, author, category))
        return books