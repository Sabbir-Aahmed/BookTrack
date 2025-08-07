from django.db import models
from book.models import Book

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membership_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class BorrowRecord(models.Model):
    book =models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
