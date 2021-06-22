from blueflamingoapi.models import salinity
from blueflamingoapi.models.salinity import Salinity
from django.http.response import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError


class SalinityView(ViewSet):
    def create(self, request):

        user = request.auth.user
        salinity = Salinity()
        salinity.ppm = request.data["ppm"]
        salinity.message = request.data["message"]

        if user.is_staff is True:
            try:
                salinity.save()
                serializer = SalinitySerializer(salinity, context={'request': request})
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
                salinity = Salinity.objects.get(pk=pk)
                salinity.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except salinity.DoesNotExist as ex:
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
        salinity = Salinity.objects.get(pk=pk)

        if user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        salinity.user = user
        salinity.ppm = request.data["ppm"]
        salinity.message = request.data["message"]

        salinity.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = request.auth.user
        salinity = Salinity.objects.all()

        user_id = request.query_params.get('user_id', None)
        if user_id is not None and user_id == str(user.id):
            salinity = Salinity.objects.all()
            salinity = Salinity.filter(user__id=user_id)
        if user_id is not None and user_id != str(user.id):
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        serializer = SalinitySerializer(
            salinity, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            salinity = Salinity.objects.get(pk=pk)
            serializer = SalinitySerializer(salinity, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class SalinitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salinity
        fields = ('id', 'ppm', 'message')