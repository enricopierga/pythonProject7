from PyQt5.QtWidgets import QMainWindow

from GestioneDatabase.QueryGestioneDipendenti.TableDipendenti import TableDipendenti
from PyQt5 import QtWidgets
from Dipendenti.View.DipendentiView import DipendentiView


class ControllerDipendente(QMainWindow):
    def __init__(self, home):
        super(QMainWindow, self).__init__()
        self.home = home
        self.dipendenteView = DipendentiView()
        self.tableDipendenti = TableDipendenti()
        self.resultSearch = None


    def passaDipendenti(self):
        #from Home.View.Home import Home
        #self.home = Home()

        #inizializzazione interfaccia Dipendenti

        self.window = QtWidgets.QMainWindow()
        self.dipendenteView.homeDipendenti.setupUi(self.window)
        self.window.show()
        print("fatto")


        #funzioni per tornare alla home da gestione dipendenti
        self.dipendenteView.homeDipendenti.tornahome.clicked.connect(self.window.close)
        print("fatto")

        self.dipendenteView.homeDipendenti.tornahome.clicked.connect(self.home.mostra)

        self.dipendenteView.homeDipendenti.aggiungidip.clicked.connect(self.window.close)

        #funzione per chiudere l'interfaccia homedipendenti all'apertura dell'interfaccia per l'eliminazione
        self.dipendenteView.homeDipendenti.eliminadip.clicked.connect(self.window.close)

        #funzione per chiudere l'interfaccia homedipendenti all'apertura dell'interfaccia per la ricerca dell'utente da modificare
        self.dipendenteView.homeDipendenti.modificainfodip.clicked.connect(self.window.close)

        #funzione per chiamare le funzioni di inserimento,eliminazione e cancellazione
        self.passaBottoniDip()

    #funzione per richiamare i bottoni
    def passaBottoniDip(self):
        print("fatto")
        self.dipendenteView.homeDipendenti.aggiungidip.clicked.connect(self.passaInserisciDip)
        self.dipendenteView.homeDipendenti.eliminadip.clicked.connect(self.passaEliminaDip)
        self.dipendenteView.homeDipendenti.modificainfodip.clicked.connect(self.passaRicercaDip)

    def passaInserisciDip(self):
        #inizializzazione dell'interfaccia di inserimento
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.inserisciDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()

        #chiamata della funzione per l'inserimento di un dipendente
        self.dipendenteView.inserisciDip.aggiungidip.clicked.connect(self.inserisciDipendente)

        #funzione per tornare alla Home di gestioneDipendenti
        self.dipendenteView.inserisciDip.tornagestionedip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)
        self.dipendenteView.inserisciDip.tornagestionedip.clicked.connect(self.passaDipendenti)

    def passaEliminaDip(self):
        #funzione per inizializzare l'interfaccia di eliminazione
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.eliminaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()
        #funzione per eliminare un dipendente
        self.dipendenteView.eliminaDip.confermaricercacf.clicked.connect(self.eliminaDipendente)

        #funzione per tornare alla Home di gestioneDipendenti
        self.dipendenteView.eliminaDip.tornagestdip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)
        self.dipendenteView.eliminaDip.tornagestdip.clicked.connect(self.passaDipendenti)

    def passaRicercaDip(self):
        #funzione per inizializzare l'interfaccia di ricerca
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.ricercaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.dipendenteView.homeDipendenti.window.show()

        # funzione per ricercare un dipendente
        self.dipendenteView.ricercaDip.confermaricercacf.clicked.connect(self.ricercaDipendente)
        self.dipendenteView.ricercaDip.confermaricercacf.clicked.connect(self.dipendenteView.homeDipendenti.window.close)

        # funzioni per tornare alla home di gestioneDipendenti
        self.dipendenteView.ricercaDip.tornagestdip.clicked.connect(self.passaDipendenti)
        self.dipendenteView.ricercaDip.tornagestdip.clicked.connect(self.dipendenteView.homeDipendenti.window.hide)

    def passaModificaDip(self):
        #funzioni per inizializzare l'interfaccia di modificaDipendente
        self.dipendenteView.homeDipendenti.window = QtWidgets.QMainWindow()
        self.dipendenteView.modificaDip.setupUi(self.dipendenteView.homeDipendenti.window)
        self.caricaDipendente()
        #self.dipendenteView.modificaDip.cf.setEnabled(False)
        self.dipendenteView.homeDipendenti.window.show()

        #funzione per modificare il dipendente
        self.dipendenteView.modificaDip.salvamodifichedip.clicked.connect(self.dipendenteView.homeDipendenti.window.close)
        self.dipendenteView.modificaDip.salvamodifichedip.clicked.connect(self.modificaInfoDip)

        #funzione per tornare alla home di gestioneDIpendenti
        self.dipendenteView.modificaDip.tornagestionedip.clicked.connect(self.dipendenteView.homeDipendenti.window.close)
        self.dipendenteView.modificaDip.tornagestionedip.clicked.connect(self.passaDipendenti)

    def inserisciDipendente(self):
        cf, nome, cognome, citta, tel, mansione, ore, stip, username = self.dipendenteView.getInserisciLineEdit()

        params = {'cf': cf, 'nome': nome, 'cognome': cognome, 'citta': citta, 'tel': tel, 'mansione': mansione, 'ore': ore, 'stip': stip, 'username': username}

        result = self.tableDipendenti.insertQuery(params)
        if result == 0:
            self.dipendenteView.messageInserimentoCorretto()
        else:
            self.dipendenteView.messageWarningInserimento()

    def eliminaDipendente(self):

        #updateSicurezza = "DELETE FROM Sicurezza where nome_dipendente = '%s'" % (''.join(self.dipendenteView.eliminaDip.ricercacf.text()))
        cf = self.dipendenteView.getEliminaLineEdit()
        result = self.tableDipendenti.deleteQuery(cf)
        if result != 0:
            self.dipendenteView.messageWarningEliminazione()
        else:
            self.dipendenteView.messageEliminazioneAvvenuta()

    def ricercaDipendente(self):
        cf = self.dipendenteView.getRicercaLineEdit()
        self.resultSearch = self.tableDipendenti.searchQuery(cf)

        if self.resultSearch == 0:
            self.dipendenteView.messageWarningRicerca()
            self.passaDipendenti()
        else:
            self.passaModificaDip()

    def caricaDipendente(self):
        cf, nome, cognome, citta, tel, mansione, ore, stip, username = self.resultSearch
        print(cf, nome, cognome, citta, tel, mansione, ore, stip, username)
        oreText = str(ore)
        stipText = str(stip)

        while self.dipendenteView.modificaDip.oredip.text() == "":
            try:
                self.dipendenteView.modificaDip.oredip.setText(oreText)
                self.dipendenteView.modificaDip.stipendiodip.setText(stipText)
                self.dipendenteView.modificaDip.usernamedip.setText(username)
            except:
                print("ciaot")
        try:
            self.dipendenteView.modificaDip.cf.setText(cf)
            self.dipendenteView.modificaDip.nomedip.setText(nome)
            self.dipendenteView.modificaDip.congomedip.setText(cognome)
            self.dipendenteView.modificaDip.cittadip.setText(citta)
            self.dipendenteView.modificaDip.cellularedip.setText(tel)
            self.dipendenteView.modificaDip.mansionedip.setText(mansione)
        except:
            print(ore)
            print(stip)




    def modificaInfoDip(self):
        cf, nome, cognome, citta, tel, mansione, ore, stip, username = self.dipendenteView.getModificaLineEdit()
        params = {'cf': cf, 'nome': nome, 'cognome': cognome, 'citta': citta, 'tel': tel, 'mansione': mansione, 'ore': ore, 'stip': stip, 'username': username}

        self.tableDipendenti.modifyQuery(params)
        self.dipendenteView.messageCorrettoModify()
        self.passaDipendenti()