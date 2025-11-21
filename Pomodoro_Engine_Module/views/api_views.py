from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import PomodoroSession
from ..serializers import PomodoroSessionSerializer

class APISessionList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        sessions = PomodoroSession.objects.filter(user=request.user)
        serializer = PomodoroSessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PomodoroSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APISessionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user, pk):
        return PomodoroSession.objects.filter(user=user, id=pk).first()

    def get(self, request, pk):
        session = self.get_object(request.user, pk)
        if not session:
            return Response({"error": "Not found"}, status=404)
        serializer = PomodoroSessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk):
        session = self.get_object(request.user, pk)
        if not session:
            return Response({"error": "Not found"}, status=404)
        serializer = PomodoroSessionSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        session = self.get_object(request.user, pk)
        if not session:
            return Response({"error": "Not found"}, status=404)
        session.delete()
        return Response(status=204)
