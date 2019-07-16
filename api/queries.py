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


def get_count_from_family_and_basis_of_record(family_id, basis_of_record):
    """
    Descripción de lo que hace la consulta.

    :param family_id:
    :param basis_of_record:
    :return:
    """

    sql = """
    SELECT COUNT(*),domain,kingdom,phylum,class,_order,family,familyid,genus,genusid 
    FROM mcnb_prod 
    WHERE familyid=%s AND basisofrecord=%s 
    GROUP BY domain,kingdom,phylum,class,_order,family,familyid,genus,genusid 
    ORDER BY count(*) DESC
    """

    return get_data_from_database(sql, [family_id, basis_of_record])
