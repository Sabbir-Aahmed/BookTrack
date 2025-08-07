from django.urls import path,include
from book.views import BooksViewSet, CategoryViewSet, AuthorViewSet
from member.views import MemberViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books', BooksViewSet, basename='books')
router.register('categories', CategoryViewSet, basename='categories')
router.register('authors', AuthorViewSet, basename='authors')
router.register('members', MemberViewSet, basename='members')

urlpatterns = [
    path('', include(router.urls))
]
