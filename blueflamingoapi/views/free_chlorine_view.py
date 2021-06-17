from blueflamingoapi.models import free_chlorine
from blueflamingoapi.models.free_chlorine import FreeChlorine
from django.http.response import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.core.exceptions import ValidationError


class FreeChlorineView(ViewSet):
    def create(self, request):

        user = request.auth.user
        free_chlorine = FreeChlorine()
        free_chlorine.ppm = request.data["ppm"]
        free_chlorine.message = request.data["message"]
        # free_chlorine.user = user

        if user.is_staff is True:
            try:
                free_chlorine.save()
                serializer = FreeChlorineSerializer(free_chlorine, context={'request': request})
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
                free_chlorine = FreeChlorine.objects.get(pk=pk)
                free_chlorine.delete()

                return Response({}, status=status.HTTP_204_NO_CONTENT)
            except free_chlorine.DoesNotExist as ex:
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
        free_chlorine = FreeChlorine.objects.get(pk=pk)

        if user.is_staff is False:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        free_chlorine.user = user
        free_chlorine.ppm = request.data["ppm"]
        free_chlorine.message = request.data["message"]

        free_chlorine.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = request.auth.user
        free_chlorine = FreeChlorine.objects.all()

        # elif user.is_staff is False:
        #     date_thresh = datetime.now()
        #     free_chlorine = free_chlorine.objects.all().order_by("-publication_date").filter(approved=True).filter(
        #         publication_date__lt=date_thresh)

        user_id = request.query_params.get('user_id', None)
        if user_id is not None and user_id == str(user.id):
            free_chlorine = FreeChlorine.objects.all()
            free_chlorine = FreeChlorine.filter(user__id=user_id)
        if user_id is not None and user_id != str(user.id):
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        # # Note the additional `many=True` argument to the
        # # serializer. It's needed when you are serializing
        # # a list of objects instead of a single object.

        serializer = FreeChlorineSerializer(
            free_chlorine, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            free_chlorine = FreeChlorine.objects.get(pk=pk)
            serializer = FreeChlorineSerializer(free_chlorine, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class FreeChlorineSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeChlorine
        fields = ('id', 'ppm', 'message')