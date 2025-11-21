from rest_framework import serializers
from .models import PomodoroSession

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = "__all__"
        read_only_fields = ["id", "user"]
