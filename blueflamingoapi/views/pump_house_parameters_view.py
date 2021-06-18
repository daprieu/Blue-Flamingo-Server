from blueflamingoapi.models.ph import Ph
from blueflamingoapi.models.pump_house_parameters import PumphouseParameters
from blueflamingoapi.models import (PumpHouse, Hardness, Alkalinity, CyanuricAcid, FilterPressure, FreeChlorine, 
                                    TotalChlorine, Ph, Salinity, )
from django.http.response import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError
from datetime import datetime


class PumphouseParametersView(ViewSet):
    def create(self, request):

        user = request.auth.user
        pump_house_parameters = PumphouseParameters()
        pump_house_parameters.date = datetime.now()
        pump_house_parameters.pumphouse = PumpHouse.objects.get(pk=request.data['pumphouse']) 
        pump_house_parameters.user = user
        if request.data['hardness'] is not None:
            pump_house_parameters.hardness = Hardness.objects.get(pk=request.data['hardness'])
        pump_house_parameters.hardness_note = request.data['hardness_note']
        if request.data['total_chlorine'] is not None:
            pump_house_parameters.total_chlorine = TotalChlorine.objects.get(pk=request.data['total_chlorine'])
        if request.data['free_chlorine'] is not None:
            pump_house_parameters.free_chlorine = FreeChlorine.objects.get(pk=request.data['free_chlorine'])
        pump_house_parameters.chlorine_note = request.data['chlorine_note']
        if request.data['ph'] is not None:
            pump_house_parameters.ph = Ph.objects.get(pk=request.data['ph'])
        pump_house_parameters.ph_note = request.data['ph_note']
        if request.data['alkalinity'] is not None:
            pump_house_parameters.alkalinity = Alkalinity.objects.get(pk=request.data['alkalinity'])
        pump_house_parameters.alkalinity_note = request.data['alkalinity_note']
        if request.data['cyanuric_acid'] is not None:
            pump_house_parameters.cyanuric_acid = CyanuricAcid.objects.get(pk=request.data['cyanuric_acid'])
        pump_house_parameters.cyanuric_acid_note = request.data['cyanuric_acid_note']
        if request.data['salinity'] is not None:
            pump_house_parameters.salinity = Salinity.objects.get(pk=request.data['salinity'])
        pump_house_parameters.salinity_note = request.data['salinity_note']
        if request.data['filter_pressure'] is not None:
            pump_house_parameters.filter_pressure = FilterPressure.objects.get(pk=request.data['filter_pressure'])
        pump_house_parameters.filter_pressure_note = request.data['filter_pressure_note']
        pump_house_parameters.filter_basket = request.data['filter_basket']

        
        try:
            pump_house_parameters.save()
            serializer = PumphouseParametersSerializer(pump_house_parameters, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self, request, pk=None):

        user = request.auth.user
        pump_house_parameters = PumphouseParameters.objects.get(pk=pk, user=user)

        if user.id is pump_house_parameters.user.id:
            try:
                user = request.auth.user
                pump_house_parameters.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except pump_house_parameters.DoesNotExist as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
            
            except Exception as ex:
                return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif user.id is not pump_house_parameters.user.id:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        user = request.auth.user
        # category = Category.objects.get(pk = request.data["categoryId"])
        pump_house_parameters = PumphouseParameters.objects.get(pk=pk)

        if user.id is not pump_house_parameters.user.id:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        user = request.auth.user
        # pump_house_parameters = PumphouseParameters()
        pump_house_parameters.date = datetime.now()
        pump_house_parameters.user = user
        pump_house_parameters.pumphouse = PumpHouse.objects.get(pk=request.data['pumphouse'])
        if pump_house_parameters.hardness is None:
            pump_house_parameters.hardness = None
        elif request.data['hardness'] is not None:
            pump_house_parameters.hardness = Hardness.objects.get(pk=request.data['hardness'])
        pump_house_parameters.hardness_note = request.data['hardness_note']
        if request.data['total_chlorine'] is not None:
            pump_house_parameters.total_chlorine = TotalChlorine.objects.get(pk=request.data['total_chlorine'])
        if request.data['free_chlorine'] is not None:
            pump_house_parameters.free_chlorine = FreeChlorine.objects.get(pk=request.data['free_chlorine'])
        pump_house_parameters.chlorine_note = request.data['chlorine_note']
        if request.data['ph'] is not None:
            pump_house_parameters.ph = Ph.objects.get(pk=request.data['ph'])
        pump_house_parameters.ph_note = request.data['ph_note']
        if request.data['alkalinity'] is not None:
            pump_house_parameters.alkalinity = Alkalinity.objects.get(pk=request.data['alkalinity'])
        pump_house_parameters.alkalinity_note = request.data['alkalinity_note']
        if request.data['cyanuric_acid'] is not None:
            pump_house_parameters.cyanuric_acid = CyanuricAcid.objects.get(pk=request.data['cyanuric_acid'])
        pump_house_parameters.cyanuric_acid_note = request.data['cyanuric_acid_note']
        if request.data['salinity'] is not None:
            pump_house_parameters.salinity = Salinity.objects.get(pk=request.data['salinity'])
        pump_house_parameters.salinity_note = request.data['salinity_note']
        if request.data['filter_pressure'] is not None:
            pump_house_parameters.filter_pressure = FilterPressure.objects.get(pk=request.data['filter_pressure'])
        pump_house_parameters.filter_pressure_note = request.data['filter_pressure_note']
        pump_house_parameters.filter_basket = request.data['filter_basket']

        pump_house_parameters.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = request.auth.user
        pump_house_parameters = PumphouseParameters.objects.all()

        # elif user.is_staff is False:
        #     date_thresh = datetime.now()
        #     pump_house_parameters = pump_house_parameters.objects.all().order_by("-publication_date").filter(approved=True).filter(
        #         publication_date__lt=date_thresh)

        user_id = request.query_params.get('user_id', None)
        if user_id is not None and user_id == str(user.id):
            pump_house_parameters = PumphouseParameters.objects.all()
            pump_house_parameters = PumphouseParameters.filter(user__id=user_id)
        if user_id is not None and user_id != str(user.id):
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        # # Note the additional `many=True` argument to the
        # # serializer. It's needed when you are serializing
        # # a list of objects instead of a single object.

        serializer = PumphouseParametersSerializer(
            pump_house_parameters, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            pump_house_parameters = PumphouseParameters.objects.get(pk=pk)
            serializer = PumphouseParametersSerializer(pump_house_parameters, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class PumphouseParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumphouseParameters
        fields = ('id', 'user', 'date', 'pumphouse', 'hardness',  'hardness_note', 'total_chlorine',
                'free_chlorine', 'chlorine_note', 'ph', 'ph_note', 'alkalinity',
                'alkalinity_note', 'cyanuric_acid', 'cyanuric_acid_note', 'salinity', 
                'salinity_note', 'filter_pressure', 'filter_pressure_note', 'filter_basket',)
        depth = 1