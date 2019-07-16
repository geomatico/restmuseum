from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.queries import get_count_from_family_and_basis_of_record


class GetThingsFromDataBase(APIView):

    def get(self, request, family_id, basis_of_record):

        if family_id and basis_of_record:
            sql = get_count_from_family_and_basis_of_record(family_id, basis_of_record)
            return Response(sql)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
