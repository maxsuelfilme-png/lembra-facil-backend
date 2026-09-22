from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, ValidationError

from .models import ConfirmacaoDose
from .serializers import ConfirmacaoDoseSerializer


class ConfirmacaoDoseViewSet(viewsets.ModelViewSet):
    serializer_class = ConfirmacaoDoseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ConfirmacaoDose.objects.filter(
            usuario=self.request.user
        ).select_related(
            'medicamento',
            'horario'
        ).order_by('-data', 'horario__horario')

    def perform_create(self, serializer):
        medicamento = serializer.validated_data['medicamento']
        horario = serializer.validated_data['horario']
        status = serializer.validated_data.get('status', 'pendente')

        if medicamento.usuario != self.request.user:
            raise PermissionDenied(
                'Este medicamento não pertence ao usuário.'
            )

        if horario.medicamento_id != medicamento.id:
            raise ValidationError(
                'Este horário não pertence ao medicamento informado.'
            )

        confirmado_em = None

        if status == 'tomado':
            confirmado_em = timezone.now()

        serializer.save(
            usuario=self.request.user,
            confirmado_em=confirmado_em
        )