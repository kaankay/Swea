from datetime import datetime
from wea.settings import BASE_DIR
from weaeinkauf.models import Quelle, Vertrag, Angebot, Indikation, Schaetzung

def run():
    
    quellen = Quelle.objects.all()
    indikationen = Indikation.objects.all()
    vertrage = Vertrag.objects.all()
    angebote = Angebot.objects.all()
    schaetzungen = Schaetzung.objects.all()

    for quelle in quellen:
        for angebot in angebote:
            if quelle.alt_id == angebot.quellen_id:
                quelle.quellenart = "Angebot"
                print(f"Quelle Alt ID {quelle.alt_id} dem Angebot ID {angebot.id} zugeweisen")

        for indikation in indikationen:
            if quelle.alt_id == indikation.quellen_id:
                quelle.quellenart = "Indikation"
                print(f"Quelle Alt ID {quelle.alt_id} der Indikation ID {indikation.id} zugeweisen")
                
        for vertrag in vertrage:
            if quelle.alt_id == vertrag.quellen_id:
                quelle.quellenart = "Vertrag"
                print(f"Quelle Alt ID {quelle.alt_id} dem Vertrag ID {vertrag.id} zugeweisen")

        for schaetzung in schaetzungen:
            if quelle.alt_id == schaetzung.quellen_id:
                quelle.quellenart = "Schätzung"
                print(f"Quelle Alt ID {quelle.alt_id} der Schätzung ID {schaetzung.id} zugeweisen")


            

