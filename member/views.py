from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BorrowRecordViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        user = self.request.user
        qs = BorrowRecord.objects.select_related('book', 'member')
        
        if user.is_librarian:
            return qs 
        else:
            return qs.filter(member=user, returned_date__isnull=True)
        


    @swagger_auto_schema(
        operation_summary="List borrow records",
        operation_description="List of all borrow records. Librarians can see all; members can see only their active borrow records.",
        responses={200: BorrowRecordSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a borrow record",
        operation_description="Create a borrow record for the authenticated user. The book must be available.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['book'],
            properties={
                'book': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the book to borrow'),
            },
        ),
        responses={
            201: BorrowRecordSerializer,
            400: 'Bad request or book unavailable',
            404: 'Book not found',
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(member=self.request.user)



    @swagger_auto_schema(
        operation_summary="Delete a borrow record",
        operation_description="Only librarians can delete borrow records.",
        responses={
            204: 'Borrow record deleted successfully',
            403: 'Only librarians can delete borrow records',
        },
    )
    def destroy(self, request, *args, **kwargs):

        if not request.user.is_librarian:
            return Response({"error": "Only librarians can delete borrow records."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    

    @swagger_auto_schema(
        method='get',
        operation_summary="Return a borrowed book",
        operation_description="Mark the borrowed book as returned. Only the member who borrowed the book can return it.",
        responses={
            200: openapi.Response('Book returned successfully', BorrowRecordSerializer),
            403: 'You cannot return a book you did not borrow',
            404: 'Borrow record not found',
        },
    )

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
    
    @swagger_auto_schema(
        operation_summary="Retrieve a book that borrowed",
        operation_description="Get detailed information about a borrowed book",
        responses={200: BorrowRecordSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)