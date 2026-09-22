from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Medicamento
from .serializers import MedicamentoSerializer


class MedicamentoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medicamento.objects.filter(
            usuario=self.request.user
        ).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)