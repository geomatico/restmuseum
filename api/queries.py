from django.db import connection


def get_data_from_database(sql, params):
    """
    Método que genera una conexión a la base de datos y ejecuta la sql que le pasemos como parámetro mas los valores
    de los parámetros que necesita la consulta

    La conversión a dict está sacada de la documentación de Django
    Ver: https://docs.djangoproject.com/en/2.2/topics/db/sql/#executing-custom-sql-directly

    :param sql: string
        consulta en SQL. Los parámetros que necesita la consulta se deben fijar con %s
    :param params: array
        array con los parámetros en el orden que necesita la consulta
    :return: dict
        dict con los resultados de la consulta

    """
    with connection.cursor() as cursor:
        cursor.execute(sql, params)

        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

levels = ["domain", "kingdom", "phylum", "class", "_order", "family", "genus", "species", "subspecies"]
levelsId = ["domain", "kingdom", "phylum", "class", "_order", "familyid", "genusid", "speciesid", "subspeciesid"]

def get_filters_from_request(request):
    #print(request.query_params)
    sql = ""

    #todo: prevent SQL injection
    for key in request.query_params:
        sql += " AND "
        d = { 'field': key, 'value': request.query_params[key]}
        comparison = """ {field} = '{value}'"""
        sql += comparison.format(**d)
    return sql

def get_taxon_where(taxon_id, taxon_level, request):
    filters = get_filters_from_request(request)
    comparison = """ {field} = '{value}'"""
    d = { 'field' : levelsId[taxon_level], 'value': taxon_id }
    return comparison.format(**d) + filters

def get_fields(taxon_level):
    #unique values (set instead of list) of levelsId and levels
    return ",".join(set(levelsId[:taxon_level+2]+levels[:taxon_level+2]))

def get_children_from_taxon(taxon_id, taxon_level, request):
    """
    Descripción de lo que hace la consulta.

    :param taxon_level:
    :param taxon_id:
    :param filters:
    :return:
    """

    sql = """
    SELECT
    COUNT(*), {fields}
    FROM api_mcnbprod
    WHERE {where}
    GROUP BY {fields}
    ORDER BY count(*) DESC
    """

    d = { 'fields': get_fields(taxon_level), 'where': get_taxon_where(taxon_id, taxon_level, request) }

    #print(sql.format(**d))

    return get_data_from_database(sql.format(**d), [taxon_id, taxon_level])

def get_count_from_family_and_basis_of_record(family_id, basis_of_record):
    """
    Descripción de lo que hace la consulta.

    :param family_id:
    :param basis_of_record:
    :return:
    """

    sql = """
    SELECT COUNT(*),domain,kingdom,phylum,class,_order,family,familyid,genus,genusid
    FROM api_mcnbprod
    WHERE familyid=%s AND basisofrecord=%s
    GROUP BY domain,kingdom,phylum,class,_order,family,familyid,genus,genusid
    ORDER BY count(*) DESC
    """

    return get_data_from_database(sql, [family_id, basis_of_record])
