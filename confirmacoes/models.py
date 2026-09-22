from django.db import models
from django.contrib.auth.models import User
from medicamentos.models import Medicamento
from horarios.models import HorarioMedicamento


class ConfirmacaoDose(models.Model):

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('tomado', 'Tomado'),
        ('nao_tomado', 'Não tomado'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='confirmacoes'
    )

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE,
        related_name='confirmacoes'
    )

    horario = models.ForeignKey(
        HorarioMedicamento,
        on_delete=models.CASCADE,
        related_name='confirmacoes'
    )

    data = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )

    confirmado_em = models.DateTimeField(
        null=True,
        blank=True
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data', 'horario']
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'medicamento', 'horario', 'data'],
                name='dose_unica_por_horario_data'
            )
        ]

    def __str__(self):
        return f'{self.medicamento.nome} - {self.data} - {self.status}'