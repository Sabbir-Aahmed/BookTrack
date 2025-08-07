from django.urls import path,include
from book.views import BooksViewSet, CategoryViewSet, AuthorViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books', BooksViewSet, basename='books')
router.register('categories', CategoryViewSet, basename='categories')
router.register('authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('', include(router.urls))
]
