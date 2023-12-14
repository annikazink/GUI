from unittest.mock import MagicMock
import random

# Funktion zur Generierung eines zufälligen Datensatzes
def generate_random_data():
    data = {
        "ID": str(random.randint(10000000, 99999999)),
        "Zeitstempel": MagicMock(),
        "Zeitstempel_Unix_ms": str(random.randint(1000000000000, 9999999999999)),
        "Strom_gesamt": str(random.uniform(0, 10)),
        "Spannung_gesamt": str(random.uniform(200, 500)),
        "Wirkleistung_gesamt": str(random.uniform(0, 20)),
        "Blindleistung_gesamt": str(random.uniform(0, 5)),
        "Energie_gesamt_kwh": str(random.uniform(10000, 20000)),
        "CosPhi_gesamt": str(random.uniform(0.2, 0.9)),
        "Frequenz_gesamt": str(random.uniform(48, 52)),
        "Temperatur1": str(random.uniform(20, 30)),
        "Temperatur2": str(random.uniform(100, 200)),
        "Druck": str(random.uniform(0.5, 1.5)),
        "Durchfluss": str(random.uniform(100, 200)),
    }
    return data

# Erzeuge 12 zufällige Datensätze
datensaetze = [generate_random_data() for _ in range(12)]

# Ausgabe der Datensätze
for i, datensatz in enumerate(datensaetze):
    print(f"Datensatz {i + 1}: {datensatz}")

    import mysql.connector
    from mysql.connector import Error


    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection


    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")


    # Datenbank Konfiguration
    host = ("45484")
    user = "kompressor"
    password = "tsN*r1oeLxH-gCgy"
    database = "kompressor"

    # Verbindung erstellen
    connection = create_db_connection(host, user, password, database)

    # Beispielabfrage
    query = "SELECT * FROM Ihre_Tabelle;"  # Ersetzen Sie 'Ihre_Tabelle' mit dem tatsächlichen Tabellennamen
    execute_query(connection, query)