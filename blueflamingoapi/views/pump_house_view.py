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

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = request.auth.user
        if user.is_staff is True:
            pump_house = PumpHouse.objects.all()

        # elif user.is_staff is False:
        #     date_thresh = datetime.now()
        #     pump_house = pump_house.objects.all().order_by("-publication_date").filter(approved=True).filter(
        #         publication_date__lt=date_thresh)

        user_id = request.query_params.get('user_id', None)
        if user_id is not None and user_id == str(user.id):
            pump_house = pump_house.objects.all()
            pump_house = pump_house.filter(user__id=user_id)
        if user_id is not None and user_id != str(user.id):
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        # # Note the additional `many=True` argument to the
        # # serializer. It's needed when you are serializing
        # # a list of objects instead of a single object.

        serializer = PumpHouseSerializer(
            pump_house, many=True, context={'request': request})
        return Response(serializer.data)


class PumpHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpHouse
        fields = ('id', 'name', 'user')