from blueflamingoapi.models.pump_house import PumpHouse
from django.http.response import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError


class PumpHouseView(ViewSet):
    def create(self, request):

        user = request.auth.user
        pump_house = PumpHouse()
        pump_house.name = request.data["name"]
        pump_house.user = user

        if user.is_staff is True:
            try:
                pump_house.save()
                serializer = PumpHouseSerializer(pump_house, context={'request': request})
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
                pump_house = PumpHouse.objects.get(pk=pk, user=user)
                pump_house.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except PumpHouse.DoesNotExist as ex:
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
        # category = Category.objects.get(pk = request.data["categoryId"])
        pump_house = PumpHouse.objects.get(pk=pk)

        if user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        pump_house.user = user
        pump_house.name = request.data["name"]

        pump_house.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        
        pump_house = PumpHouse.objects.all()

        # # Note the additional `many=True` argument to the
        # # serializer. It's needed when you are serializing
        # # a list of objects instead of a single object.

        serializer = PumpHouseSerializer(
            pump_house, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            pump_house = PumpHouse.objects.get(pk=pk)
            serializer = PumpHouseSerializer(pump_house, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

class PumpHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpHouse
        fields = ('id', 'name', 'user')