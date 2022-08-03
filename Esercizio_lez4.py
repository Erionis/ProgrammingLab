# Esercizio
# Creare un oggetto CSVFile che rappresenti un file CSV, e che:
# venga inizializzato sul nome del file csv, e
# abbia un attributo "name" che ne contenga il nome
# abbia un metodo "get_data" che torni i dati dal file CSV come numeri di una lista

# creo oggetto CSVFile
class CSVFile():

    # costruttore della classe
    def __init__(self, name):
        self.name = name

    def get_data(self):
        # inizializzo una lista vuora per salvare i valori
        list_of_list = [[]]
        # apro e leggo il file linea per linea
        my_file = open(self.name,'r')
        for line in my_file:
            # faccio lo split di ogni riga sulla virgola
            elements  = line.split(',')
            # Se NON soto processando l'intestazione...
            if elements[0] != 'Date':
                # setto la data e il valore
                date = elements[0]
                value = elements[1]
                #aggiungo alla lista dei valori questo valore
                lists = [date, value]
                list_of_list.append(lists)
        return list_of_list

file_ = CSVFile('shampoo_sales.csv')
print(file_.get_data())