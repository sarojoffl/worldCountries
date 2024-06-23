from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Countries
from .serializers import CountriesSerializer

@api_view(['GET', 'POST'])
def countries_list(request):
    """
    List all countries or create a new country.
    """
    if request.method == 'GET':
        name = request.GET.get('name', None)
        if name:
            countries = Countries.objects.filter(name__icontains=name)
        else:
            countries = Countries.objects.all()
        
        serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CountriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def countries_detail(request, pk):
    """
    Retrieve, update or delete a country by id (pk).
    """
    try:
        country = Countries.objects.get(pk=pk)
    except Countries.DoesNotExist:
        return JsonResponse({'message': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountriesSerializer(country)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CountriesSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return JsonResponse({'message': 'Country deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

