class JsonSerializer(object):

    def __init__(self, data):
        self.data = data

    def to_json(self):
        """
        Aquí la lógica que transforma los datos en lo que quieres que devuelva
        :return: json
        """
        return self.data
