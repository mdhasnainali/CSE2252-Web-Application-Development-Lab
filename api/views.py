from rest_framework import status
from rest_framework.views import APIView
from api.serializers import BreedSerializer, DogSerializer
from rest_framework.response import Response
from api.models import Dog,Breed


class BreedList(APIView):
    def post(self, request, *args, **kwargs):
        serailizer = BreedSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'data': serailizer.data})
        else:
            return Response({'errors': serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        breed = Breed.objects.all()
        serailizer = BreedSerializer(breed, many=True)
        return Response({'data': serailizer.data})


class BreedDetail(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            student = Breed.objects.get(name=pk)
            serailizer = BreedSerializer(student)
            return Response({'data': serailizer.data})
        except Breed.DoesNotExist:
            return Response({'data': 'not found'})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            student = Breed.objects.get(name=pk)
            serailizer = BreedSerializer(instance=student, data=request.data)
            if serailizer.is_valid():
                serailizer.save()
                return Response({'data': serailizer.data})
            else:
                return Response({'errors': serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Breed.DoesNotExist:
            return Response({'data': 'not found'})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            student = Breed.objects.get(name=pk)
            student.delete()
            return Response({'data': 'deleted'})
        except Breed.DoesNotExist:
            return Response({'data': 'not found'})


class DogList(APIView):
    def post(self, request, *args, **kwargs):
        serailizer = DogSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'data': serailizer.data})
        else:
            return Response({'errors': serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        dogs = Dog.objects.all()
        serailizer = DogSerializer(dogs, many=True)
        return Response({'data': serailizer.data})


class DogDetail(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            dog = Dog.objects.get(id=pk)
            serailizer = DogSerializer(dog)
            return Response({'data': serailizer.data})
        except Dog.DoesNotExist:
            return Response({'data': 'not found'})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            dog = Dog.objects.get(id=pk)
            serailizer = DogSerializer(instance=dog, data=request.data)
            if serailizer.is_valid():
                serailizer.save()
                return Response({'data': serailizer.data})
            else:
                return Response({'errors': serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Breed.DoesNotExist:
            return Response({'data': 'not found'})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            dog = Dog.objects.get(id=pk)
            dog.delete()
            return Response({'data': 'deleted'})
        except Breed.DoesNotExist:
            return Response({'data': 'not found'})

