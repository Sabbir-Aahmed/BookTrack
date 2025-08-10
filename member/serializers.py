from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from member.models import BorrowRecord
from book.models import Book

class MemberCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'first_name',
                  'last_name', 'membership_date']


class MemberSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'Member'
        fields = ['id', 'email', 'first_name',
                  'last_name', 'membership_date']
        



class BorrowRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    member_email = serializers.ReadOnlyField(source='member.email')

    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'book_title', 'member', 'member_email', 'borrow_date', 'returned_date']
        read_only_fields = ['borrow_date', 'returned_date', 'member']

    def validate(self, attrs):
        member = self.context['request'].user
        book = attrs.get('book')

        if BorrowRecord.objects.filter(
            member=member,
            book=book,
            returned_date__isnull=True
        ).exists():
            raise serializers.ValidationError(
                {"book": "You have already borrowed this book and have not returned it yet."}
            )

        return attrs