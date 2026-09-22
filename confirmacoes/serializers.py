from rest_framework import serializers
from .models import ConfirmacaoDose


class ConfirmacaoDoseSerializer(serializers.ModelSerializer):
    medicamento_nome = serializers.CharField(
        source='medicamento.nome',
        read_only=True
    )

    horario_dose = serializers.TimeField(
        source='horario.horario',
        read_only=True
    )

    class Meta:
        model = ConfirmacaoDose
        fields = [
            'id',
            'medicamento',
            'medicamento_nome',
            'horario',
            'horario_dose',
            'data',
            'status',
            'confirmado_em',
            'criado_em',
        ]

        read_only_fields = [
            'id',
            'confirmado_em',
            'criado_em',
        ]