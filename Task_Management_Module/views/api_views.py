from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import Task
from ..serializers import TaskSerializer

class APITaskList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APITaskDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user, pk):
        return Task.objects.filter(owner=user, id=pk).first()

    def get(self, request, pk):
        task = self.get_object(request.user, pk)
        if not task:
            return Response({"error": "Not found"}, status=404)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(request.user, pk)
        if not task:
            return Response({"error": "Not found"}, status=404)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = self.get_object(request.user, pk)
        if not task:
            return Response({"error": "Not found"}, status=404)

        task.delete()
        return Response(status=204)
