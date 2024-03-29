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
        if key == 'circle':
            params = request.query_params[key].split(',')
            d = { 'field': key, 'lon': params[0], 'lat': params[1], 'radius': params[2]}
            comparison = """ AND ST_DWithin(geom::geography, ST_SetSRID(ST_MakePoint({lon},{lat}),4326)::geography, {radius}) """
            sql += comparison.format(**d)
        elif key == 'minmax':
            params = request.query_params[key].split(',')
            d = { 'field': params[0], 'min': params[1], 'max': params[2]}
            comparison = ""
            if params[1] :
                comparison += """ AND {field} >= {min}"""
            if params[2] :
                comparison += """ AND {field} <= {max}"""
            sql += comparison.format(**d)
        elif key == 'limit':
            #do nothing
            pass
        else:
            d = { 'field': key, 'value': request.query_params[key]}
            comparison = """ AND {field} = '{value}'"""
            #numeric values
            if key in ['year', 'month', 'day']:
                comparison = """ AND {field} = {value}"""
            sql += comparison.format(**d)
    return sql

def get_taxon_search(terms):
    """
    Descripción de lo que hace la consulta.

    :param terms:
    :return:
    """
    sql = ""

    #todo: prevent SQL injection
    for i, level in enumerate(levels):
        if (i < len(levels)) : #include last level (subspecies)
            # len(levels)-1 : to avoid last level (subspecies)
            levelId = levelsId[i]
            d = { 'terms': terms, 'level': level, 'levelId': levelId, 'i': i }
            comparison = """
                SELECT DISTINCT {level} AS label,
                {levelId} AS id,
            	{i} AS level
            	FROM mcnb_prod
                WHERE UPPER({level}) LIKE UPPER('{terms}%%')
                """
            if( sql ) :
                sql += " UNION "
            sql += comparison.format(**d)

    return get_data_from_database(sql + " ORDER BY level, label", [])

def get_taxon_where(taxon_id, taxon_level, request):
    filters = get_filters_from_request(request)
    comparison = """ {field} = '{value}'"""
    d = { 'field' : levelsId[taxon_level], 'value': taxon_id }
    return comparison.format(**d) + filters

def get_taxon_fields(taxon_level, mode="subtaxa"):

    if(mode == "stats") :
        #for stats we need only two fields with aliases
        return levelsId[taxon_level]+" AS id,"+levels[taxon_level]+" AS name"
    else :
        #unique values (set instead of list) of levelsId and levels
        return ",".join(set(levelsId[:taxon_level+1]+levels[:taxon_level+1]))

def get_stats_from_taxon(taxon_id, taxon_level, type, request):
    """
    Descripción de lo que hace la consulta.

    :param taxon_level:
    :param taxon_id:
    :param filters:
    :return:
    """

    sql = """
    SELECT
    COUNT(*), {field} AS name
    FROM mcnb_prod
    WHERE {where}
    {year}
    GROUP BY {field}
    ORDER BY count(*) DESC
    """

    #hack for decades (if needed in the future)
    #cast(cast(year AS integer)/10 as varchar)||'0'

    d = { 'field': type, 'where': get_taxon_where(taxon_id, taxon_level, request), 'year': ' AND YEAR IS NOT NULL' if type=='year' else '' }

    return get_data_from_database(sql.format(**d), [taxon_id, taxon_level])

def get_children_from_taxon(taxon_id, taxon_level, mode, request):
    """
    Descripción de lo que hace la consulta.

    :param fields:
    :param fieldsgroup:
    :param where:
    :return:
    """

    sql = """
    SELECT
    COUNT(*), {fields}
    FROM mcnb_prod
    WHERE {where}
    GROUP BY {fieldsgroup}
    ORDER BY count(*) DESC
    """

    if (mode == "taxon") :
        taxon_fields_level = taxon_level
    else :
        taxon_fields_level = taxon_level + 1

    d = { 'fields': get_taxon_fields(taxon_fields_level, mode), 'fieldsgroup': get_taxon_fields(taxon_fields_level), 'where': get_taxon_where(taxon_id, taxon_level, request) }

    #print(sql.format(**d))

    return get_data_from_database(sql.format(**d), [taxon_id, taxon_level])

def get_values_from_field(field):
    """
    Descripción de lo que hace la consulta.

    :param field:
    :return:
    """

    sql = """
    SELECT DISTINCT
    {field} AS VALUE
    FROM mcnb_prod
    ORDER BY {field}
    """

    d = { 'field': field }

    return get_data_from_database(sql.format(**d), [field])

def get_minmax_years():
    """
    Descripción de lo que hace la consulta.

    :return:
    """

    sql = """
    SELECT MAX(YEAR) AS maxyear,
    MIN(YEAR) AS minyear
    FROM mcnb_prod
    """

    return get_data_from_database(sql, [])
