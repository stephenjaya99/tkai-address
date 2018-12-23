import requests
from django.shortcuts import render
from .serializers import AddressSerializer
from .models import Address
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from address.settings import TKAI_USER_URL

def check_token(token):
	resp = requests.post(TKAI_USER_URL + '/get/', json={'payload': token})
	if resp.status_code == 200:
		return True
	return False

# Create your views here.
class AddressListView(APIView):

	def get(self, request, format=None):
		if 'token' not in request.query_params or not check_token(request.query_params['token']):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		return Response(AddressSerializer(Address.objects.all(), many=True).data)

	def post(self, request, format=None):
		if 'token' not in request.query_params or not check_token(request.query_params['token']):
			return Response(status=status.HTTP_400_BAD_REQUEST)

		address_serializer = AddressSerializer(data=request.data)
		if address_serializer.is_valid():
			address = address_serializer.save()
			return Response(address_serializer.data)
		return Response(statu=status.HTTP_400_BAD_REQUEST)

class AddressDetailView(APIView):
	def get_object(self, pk):
		try:
			return Address.objects.get(pk=pk)
		except Address.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
		if 'token' not in request.query_params or not check_token(request.query_params['token']):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		address = self.get_object(pk)
		serializer = AddressSerializer(address, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		if 'token' not in request.query_params or not check_token(request.query_params['token']):
			return Response(status=status.HTTP_400_BAD_REQUEST)
		address = self.get_object(pk)
		address.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)