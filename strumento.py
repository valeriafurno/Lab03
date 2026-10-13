class Strumento:

    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore

    def __str__(self):
        return f"{self.__codice} {self.__tipo} {self.__marca} {self.__anno_acquisto} {self.__valore}"

    @property
    def codice(self): #mi serve leggere gli attributi codice per il metodo aggiungi strumento
        return self.__codice

    @property
    def marca(self): #mi serve per il metodo di riordinare per marca
        return self.__marca
