class Prestito:
    def __init__(self, id_prestito, data, codice_strumento, cognome_allievo):
        self.__id_prestito = id_prestito
        self.__data = data
        self.__codice_strumento = codice_strumento
        self.__cognome_allievo = cognome_allievo


    def __str__(self):
        return f"{self.__id_prestito} {self.__data} {self.__codice_strumento} {self.__cognome_allievo}"

    @property
    def id_prestito(self):
        return self.__id_prestito

    @property
    def codice_strumento(self):
        return self.__codice_strumento