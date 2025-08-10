from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = BorrowRecord.objects.select_related('book', 'member')
        
        if user.is_librarian:
            return qs 
        else:
            return qs.filter(member=user, returned_date__isnull=True)
        
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

    def destroy(self, request, *args, **kwargs):

        if not request.user.is_librarian:
            return Response({"error": "Only librarians can delete borrow records."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=True, methods=['get'], url_path='return')
    def return_book(self, request, pk=None):

        borrow = self.get_object()

        if borrow.member != request.user:
            return Response({"error": "You cannot return a book you did not borrow."},
                            status=status.HTTP_403_FORBIDDEN)

        borrow.returned_date = timezone.now()
        borrow.save()
        return Response({"message": f"'{borrow.book.title}' has been returned successfully."},
                        status=status.HTTP_200_OK)
