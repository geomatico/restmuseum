from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from api.serializers import JsonSerializer

from api.queries import get_minmax_years
from api.queries import get_values_from_field
from api.queries import get_children_from_taxon
from api.queries import get_taxon_search
from api.queries import get_stats_from_taxon

class MinmaxYearsRestApi(APIView):

    def get(self, request):

        data = get_minmax_years()
        family_serializer = JsonSerializer(data)
        return Response(family_serializer.to_json(), status=200)

class SearchRestApi(APIView):

    def get(self, request, terms):

        if terms:
            data = get_taxon_search(terms)
            family_serializer = JsonSerializer(data)
            return Response(family_serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UniqueValuesRestApi(APIView):

    def get(self, request, field):

        if field:
            data = get_values_from_field(field)
            family_serializer = JsonSerializer(data)
            return Response(family_serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StatsRestApi(APIView):

    def get(self, request, type, taxon_id, taxon_level):

        limit = request.query_params['limit'] if ('limit' in request.query_params) else 0
        if taxon_id and taxon_level:
            #if not int(taxon_level) : Response('Taxon_level should be a number', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            if type=="taxon" :
                data = get_children_from_taxon(taxon_id, int(taxon_level), "stats", request)
            else :
                data = get_stats_from_taxon(taxon_id, int(taxon_level), type, request)
            #if we want less results
            try:
                limit = int(limit)
            except ValueError:
                return Response('Limit param should be a number',
                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            if(limit):
                data = data[0:(limit)]
            serializer = JsonSerializer(data)
            return Response(serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaxonRestApi(APIView):

    def get(self, request, taxon_id, taxon_level):

        if taxon_id and taxon_level:
            data = get_children_from_taxon(taxon_id, int(taxon_level), "taxon", request)
            serializer = JsonSerializer(data)
            return Response(serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubtaxaRestApi(APIView):

    def get(self, request, taxon_id, taxon_level):

        if taxon_id and taxon_level:
            data = get_children_from_taxon(taxon_id, int(taxon_level), "subtaxa", request)
            serializer = JsonSerializer(data)
            return Response(serializer.to_json(), status=200)
        else:
            return Response('Something was wrong!!',
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
