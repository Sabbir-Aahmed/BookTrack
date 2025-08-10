from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book
from member.managers import CustomUserManager
from django.conf import settings

class Member(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    membership_date = models.DateTimeField(auto_now_add=True)
    is_librarian = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member.email} borrowed {self.book.title}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'member'],
                condition=models.Q(returned_date__isnull=True),
                name='unique_borrow'
            )
        ]