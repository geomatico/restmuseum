from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.queries import get_count_from_family_and_basis_of_record
from api.serializers import FamilyBasisOfRecordSerializer


class GetThingsFromDataBase(APIView):

    def get(self, request, family_id, basis_of_record):

        if family_id and basis_of_record:
            data = get_count_from_family_and_basis_of_record(family_id, basis_of_record)
            family_serializer = FamilyBasisOfRecordSerializer(data)
            return Response(family_serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
