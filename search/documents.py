# from django_elasticsearch_dsl import DocType, Index
# from book.models import Book

# books = Index('books')

# @books.doc_type
# class BookDocument(DocType):
#     model = Book

#     fields = [
#         'name',
#         'author',
#         'ISBN',
#         'genre',
#     ]