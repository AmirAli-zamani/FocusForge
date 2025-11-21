from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import DailyReport
from ..serializers import DailyReportSerializer

class APIDailyReportList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reports = DailyReport.objects.filter(user=request.user).order_by("-date")
        serializer = DailyReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DailyReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIDailyReportDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user, pk):
        return DailyReport.objects.filter(user=user, id=pk).first()

    def get(self, request, pk):
        report = self.get_object(request.user, pk)
        if not report:
            return Response({"error": "Not found"}, status=404)
        serializer = DailyReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(request.user, pk)
        if not report:
            return Response({"error": "Not found"}, status=404)
        serializer = DailyReportSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        report = self.get_object(request.user, pk)
        if not report:
            return Response({"error": "Not found"}, status=404)
        report.delete()
        return Response(status=204)
