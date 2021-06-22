from blueflamingoapi.models import filter_pressure
from blueflamingoapi.models.filter_pressure import FilterPressure
from django.http.response import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError


class FilterPressureView(ViewSet):
    def create(self, request):

        user = request.auth.user
        filter_pressure = FilterPressure()
        filter_pressure.psi = request.data["psi"]
        filter_pressure.message = request.data["message"]
        # filter_pressure.user = user

        if user.is_staff is True:
            try:
                filter_pressure.save()
                serializer = FilterPressureSerializer(filter_pressure, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_404_BAD_REQUEST)
        elif user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):

        user = request.auth.user

        if user.is_staff is True:
            try:
                user = request.auth.user
                filter_pressure = FilterPressure.objects.get(pk=pk)
                filter_pressure.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except filter_pressure.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
            except Exception as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        user = request.auth.user
        filter_pressure = FilterPressure.objects.get(pk=pk)

        if user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        filter_pressure.user = user
        filter_pressure.psi = request.data["psi"]
        filter_pressure.message = request.data["message"]

        filter_pressure.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = request.auth.user
        filter_pressure = FilterPressure.objects.all()

        user_id = request.query_params.get('user_id', None)
        if user_id is not None and user_id == str(user.id):
            filter_pressure = FilterPressure.objects.all()
            filter_pressure = FilterPressure.filter(user__id=user_id)
        if user_id is not None and user_id != str(user.id):
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        serializer = FilterPressureSerializer(
            filter_pressure, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            filter_pressure = FilterPressure.objects.get(pk=pk)
            serializer = FilterPressureSerializer(filter_pressure, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class FilterPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterPressure
        fields = ('id', 'psi', 'message')