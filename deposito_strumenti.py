import strumento
from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti= [] #mi serve a ricordare i prestiti registrati e a controllare se uno strumento è già in prestito
        self.__contatore_prestiti= 0

    @property
    def responsabile(self): #in questo modo accedo all'attributo nascosto
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile): #permette di modificare l'attributo
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        #CARICA GLI STRUMENTI DAL FILE

        with open(file_path,'r', encoding='utf-8') as f:
            f.readline()
            for riga in f:
                campi = riga.strip("\n").split(",")
                codice = campi[0]
                titolo = campi[1]
                marca = campi[2]
                anno_acquisto = int(campi[3])
                valore = float(campi[4])
                strumento =Strumento(codice, titolo, marca, anno_acquisto, valore)
                self.__strumenti.append(strumento) #aggiungo ogni oggetto Strumento alla lista deposito,
                # in questo modo gli altri metodi possono utilizzarlo

                #print(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        #AGGIUNGO UNO STRUMENTO NEL DEPOSITO: aggiunge solo nel sistema e non aggiorna il file

        ultimo_strumento = self.__strumenti[-1] #leggo l'ultimo strumento
        ultimo_numero=int(ultimo_strumento.codice[1:])

        nuovo_codice = "S" + str(ultimo_numero + 1)
        nuovo_strumento=Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore) #creo un nuovo strumento che abbia il nuovo codice
        self.__strumenti.append(nuovo_strumento) #lo aggiungo alla lista
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        #ordinare gli strumenti per marca in ordine alfabetico
        print("--Elenco strumenti ordinati per marca--")

        strumenti_ordinati=sorted(self.__strumenti, key=attrgetter('marca'))
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        #controllo se lo strumento è presente nel deposito
        strumento_trovato = False
        for strumento in self.__strumenti:
            if strumento.codice == id_strumento:
                strumento_trovato = True

        if strumento_trovato == False: #se lo strumento non esiste, sollevo eccezione
            raise Exception(f"strumento non trovato")

        #controllo se lo strumento è gia in prestito
        for prestito in self.__prestiti:
            if prestito.codice_strumento == id_strumento:
                raise Exception(f"prestito già in prestito")

        self.__contatore_prestiti += 1 #incremento il contatore per generare un nuovo codice di prestito
        nuovo_codice = 'P' + str(self.__contatore_prestiti)

        # creo un nuovo prestito con codice e lo aggiungo alla lista dei prestiti attivi
        prestito= Prestito( nuovo_codice, data, id_strumento, cognome_allievo)
        self.__prestiti.append(prestito)
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestito_trovato = None

        #cerco il prestito tramite il suo codice identificativo
        for prestito in self.__prestiti:
            if prestito.id_prestito == id_prestito:
                prestito_trovato = prestito

        if prestito_trovato is None: #se non esiste sollevo eccezione!
            raise Exception(f"Codice non corrisponde ad alcun prestito esistente")

        self.__prestiti.remove(prestito_trovato) #una volta restituito lo strumento,
        # il prestito deve essere rimosso dalla lista dei prestiti

