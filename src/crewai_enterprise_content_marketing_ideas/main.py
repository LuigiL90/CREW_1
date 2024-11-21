from crew import SurpriseTravelCrew

def run_crew():
    origin = input("Inserisci la città di origine (es. 'New York City'): ")
    destination = input("Inserisci la destinazione (es. 'Rome'): ")
    age = int(input("Inserisci la tua età: "))
    hotel_location = input("Inserisci la posizione dell'hotel (es. 'Rome'): ")
    trip_duration = input("Inserisci la durata del viaggio (es. '5 days'): ")
    trip_dates = input("Inserisce la data di arrivo e la data di partenza (es. 21.04.2024 - 25.04.2024): ")
    language = input("Inserisci la lingua in cui vorresti che l'itinerario sia tradotto: ")
    # Crea il dizionario inputs con i dati forniti dall'utente
    inputs = {
        'origin': origin,
        'destination': destination,
        'age': age,
        'hotel_location': hotel_location,
        'trip_duration': trip_duration,
        'trip_dates': trip_dates,
        'language' : language,
    }

    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    print(result)

run_crew()