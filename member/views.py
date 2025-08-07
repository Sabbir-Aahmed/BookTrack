from rest_framework.mixins import CreateModelMixin,  ListModelMixin
from rest_framework.viewsets import GenericViewSet
from member.serializers import MemberSerializer
from member.models import Member


class MemberViewSet(ListModelMixin,CreateModelMixin, GenericViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
