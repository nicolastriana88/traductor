import json
import unicodedata
from googletrans import Translator

def traducir_a_catalan(objeto_json):
    traductor = Translator()
    datos = objeto_json
    
    traducciones = {}
    for clave, valor in datos.items():
        deteccion_idioma = traductor.detect(valor)
        
        if deteccion_idioma.lang == 'it':
            traduccion = traductor.translate(valor, dest='ca')
            traduccion_texto = traduccion.text.encode('latin-1').decode('unicode-escape')
            traducciones[clave] = unicodedata.normalize('NFC', traduccion_texto)
        elif deteccion_idioma.lang == 'en':
            traducciones[clave] = valor  # No se necesita traducción si está en inglés
        else:
            traducciones[clave] = valor  # Mantener el valor original si no es italiano ni inglés
    
    resultado = json.dumps(traducciones)  # Convertir el diccionario traducido a JSON
    
    return resultado

# Ejemplo de uso
texto_ingles_italiano = {
    "empty-text": "Nessun dato",
    "remaining": "rimanente",
    "completed": "completato",
    "comingSoon": "Prossimamente",
    "underConstruction": "In costruzione",
    "menu": {
    "home": "Home",
    "jobs-search": "Ricerca lavoro",
    "jobs-list": "Lista lavori",
    "metrics": "Metriche",
    "users": "Utenti",
    "resources": "Risorse",
    "help": "Aiuto",
    "logout": "Logout",
    "profile": "Profilo",
    "catalog": "Catalogo",
    "routes": "Itinerari"
    },
    "job-models": {
    "PICK_AND_DELIVERY": "Ritiro e consegna",
    "PICK_AND_DELIVERY_WITH_STORAGE": "Ritiro e consegna con deposito",
    "PICK_AND_COLLECT": "Ritiro e ritiro in loco",
    "FULL_SERVICE": "Servizio completo",
    "PICK_AND_COLLECT_NO_TRANSFER": "Ritiro e ritiro in loco senza trasferimento",
    "PICK_AND_DELIVERY_WITH_STORAGE_NO_TRANSFER": "Ritiro e consegna con deposito senza trasferimento",
    "ZONE_PICKING_AND_DELIVERY_WITH_STORAGE": "Prelievo zona e consegna con deposito",
    "ZONE_PICKING_AND_COLLECT": "Prelievo zona e ritiro in loco"
    },
    "flags": {
    "comments": {
    "Client need help": "Il cliente ha bisogno di aiuto",
    "Picking need help": "Il prelievo ha bisogno di aiuto",
    "Task PICKING": "Prelievo",
    "Task DELIVERY": "Consegna",
    "Task FULL_SERVICE": "-",
    "undefined": "-"
    },
    "DELIVERING_FINISH": "Ritardo nella fine della consegna",
    "DELIVERING_START": "Ritardo nell'inizio della consegna",
    "GOING_TO_DESTINATION_FINISH": "Ritardo nella fine del percorso",
    "TRANSFERRING_TO_FINISH": "Ritardo nel trasferimento al conducente",
    "TRANSFERRING_FROM_FINISH": "Ritardo nel trasferimento dal prelievatore",
    "GOING_TO_DESTINATION_START": "Ritardo nell'inizio del percorso",
    "GOING_TO_ORIGIN_FINISH": "Ritardo nella fine del ritorno alla base",
    "CHECKING_OUT_FINISH": "Ritardo nella fine del checkout",
    "TRANSFERRING_TO_START": "Ritardo nell'inizio del trasferimento al conducente",
    "TRANSFERRING_FROM_START": "Ritardo nell'inizio del trasferimento dal prelievatore",
    "CHECKING_OUT_START": "Ritardo nell'inizio del checkout",
    "PICKING_FINISH": "Ritardo nella fine del prelievo",
    "PICKING_START": "Ritardo nell'assegnazione del compito di prelievo",
    "PICKING_WITH_PACKING_FINISH": "Ritardo nella fine del prelievo con imballaggio",
    "PICKING_WITH_PACKING_START": "Ritardo nell'assegnazione del compito di prelievo con imballaggio",
    "GOING_TO_ORIGIN_START": "Ritardo nell'inizio del ritorno alla base",
    "AUTOMATIC_ASSIGNATION_FAILED": "La assegnazione automatica è fallita",
    "USER_CHAT": "Un cliente ha bisogno di aiuto tramite chat",
    "GOING_TO_ORIGIN_DOING": "Sto andando all'origine per fare",
    "FINISHED_START": "Ritardo per iniziare a completare il lavoro",
    "FINISHED_FINISH": "Ritardo per completare il lavoro",
    "SEED_TRANSACTION_ERROR": "Qualcosa è andato storto con la transazione seed",
    "PRODUCTS_NOT_ACEPTED": "Alcuni prodotti non sono stati accettati dal cliente",
    "PAYMENT_ALERT_FLAG": "Qualcosa è andato storto con il pagamento del cliente",
    "SH_CHAT": "Uno Shopper ha bisogno di aiuto tramite chat",
    "CL_CHAT": "Un cliente ha bisogno di aiuto tramite chat",
    "PK_CHAT": "Un picker ha bisogno di aiuto tramite chat",
    "DR_CHAT": "Un autista ha bisogno di aiuto tramite chat",
    "FS_CHAT": "Un full service guy ha bisogno di aiuto tramite chat",
    "JOB_VERIFICATION": "Operazione manuale",
    "CLIENT_WANTS_TO_CANCEL": "Il cliente vuole annullare il lavoro",
    "SHOPPER_WANTS_TO_EXIT": "Uno shopper vuole uscire da questo compito",
    "REVERT_ONLINE_PAYMENT": "Il lavoro è stato annullato e richiede il rimborso della transazione del cliente",
    "CREATION_3PL_FAILED": "La creazione sul 3PL è fallita",
    "CANCELLATION_3PL_FAILED": "La cancellazione sul 3PL è fallita",
    "created": "Creato",
    "assigned": "Assegnato",
    "resolved": "Risolto",
    "viewed": "Visto",
    "CHANGE_PAYMENT_METHOD_FAILED": "Cambio del metodo di pagamento fallito",
    "TRANSFERRING_FROM_PICKING_TO_STORAGE_START": "Ritardo per iniziare il trasferimento dal picker allo storage",
    "TRANSFERRING_FROM_PICKING_TO_STORAGE_FINISH": "Ritardo per completare il trasferimento dal picker allo storage",
    "STORING_START": "Ritardo assegnato al compito di stoccaggio",
    "STORING_FINISH": "Ritardo per completare il compito di stoccaggio",
    "TRANSFERRING_TO_STORAGE_FROM_PICKING_START": "Ritardo per iniziare il trasferimento allo storage dal picker",
    "TRANSFERRING_TO_STORAGE_FROM_PICKING_FINISH": "Ritardo per completare il trasferimento allo storage dal picker",
    "TRANSFERRING_FROM_STORAGE_TO_DELIVERY_START": "Ritardo per iniziare il trasferimento dallo storage all'autista",
    "TRANSFERRING_FROM_STORAGE_TO_DELIVERY_FINISH": "Ritardo per completare il trasferimento dallo storage all'autista",
    "TRANSFERRING_TO_DELIVERY_FROM_STORAGE_START": "Ritardo per iniziare il trasferimento all'autista dallo storage",
    "TRANSFERRING_TO_DELIVERY_FROM_STORAGE_FINISH": "Ritardo per completare il trasferimento all'autista dallo storage",
    "DELIVERY_FAILED": "Fallimento della consegna 3PL"
    },
    "jobs-status": {
    "created": "Creato",
    "cancelled": "Annullato",
    "assigned": "Assegnato",
    "processing": "In elaborazione",
    "picking": "Raccolta",
    "delivery": "Consegna",
    "finished": "Terminato",
    "CREATION_3PL_SUCCESS": "Creazione 3PL riuscita",
    "CANCELLATION_3PL_SUCCESS": "Cancellazione 3PL riuscita",
    "PAYMENT_WAS_SUCCESSFUL": "Pagamento riuscito",
    "ORDER_UNBLOCKED": "Ordine sbloccato",
    "EXTERNAL_PAYMENT_UPDATED": "Pagamento esterno aggiornato",
    "EXTERNAL_PRICES_UPDATED": "Prezzi esterni aggiornati",
    "EXTERNAL_INVOICE_UPDATED": "Fattura esterna aggiornata"
    },
    "tasks-status": {
    "PICKING": "Raccolta",
    "DELIVERY": "Consegna",
    "FULL_SERVICE": "Servizio completo",
    "STORAGE": "Magazzino",
    "PICK_UP_FOR_DELIVERY": "Spedizione",
    "PICK_UP": "Ritiro",
    "PICKING_WITH_STORAGE": "Raccolta con magazzino",
    "DELIVERY_WITH_STORAGE": "Consegna con magazzino",
    "PICKING_AND_STORAGE": "Raccolta e magazzino",
    "PROCESSING": "Elaborazione",
    "ASSIGNED": "Assegnato",
    "DOING": "In corso",
    "CONSOLIDATION": "Consolidamento",
    "ZONE_PICKING": "Raccolta zona",
    "FINISHED": "Terminato",
    "CANCELED": "Annullato",
    "RE_ALLOCATED": "Riassegnato"
    },
    "steps-status": {
    "PICKING": "Raccolta",
    "PICKING_DOING": "Raccolta in corso",
    "PICKING_DONE": "Raccolta completata",
    "PICKING_PENDING": "Raccolta in sospeso",
    "PICKING_WITH_PACKING": "Raccolta con imballaggio",
    "PICKING_WITH_PACKING_DOING": "Raccolta con imballaggio in corso",
    "PICKING_WITH_PACKING_DONE": "Raccolta con imballaggio completata",
    "PICKING_WITH_PACKING_PENDING": "Raccolta con imballaggio in sospeso",
    "CHECKING_OUT": "Check-out",
    "CHECKING_OUT_DOING": "Check-out in corso",
    "CHECKING_OUT_DONE": "Check-out completato",
    "CHECKING_OUT_PENDING": "Check-out in sospeso",
    "TRANSFERRING_TO": "Trasferimento a",
    "TRANSFERRING_TO_DOING": "Trasferimento in corso",
    "TRANSFERRING_TO_DONE": "Trasferimento completato",
    "TRANSFERRING_TO_PENDING": "Trasferimento in sospeso",
    "GOING_TO_ORIGIN": "In viaggio verso l'origine",
    "GOING_TO_ORIGIN_DOING": "In viaggio verso l'origine in corso",
    "GOING_TO_ORIGIN_DONE": "In viaggio verso l'origine completato",
    "GOING_TO_ORIGIN_PENDING": "In viaggio verso l'origine in sospeso",
    "TRANSFERRING_FROM": "Trasferimento da",
    "TRANSFERRING_FROM_DOING": "Trasferimento da in corso",
    "TRANSFERRING_FROM_DONE": "Trasferimento da completato",
    "TRANSFERRING_FROM_PENDING": "Trasferimento da in sospeso",
    "GOING_TO_DESTINATION": "In viaggio verso la destinazione",
    "GOING_TO_DESTINATION_DOING": "In viaggio verso la destinazione in corso",
    "GOING_TO_DESTINATION_DONE": "In viaggio verso la destinazione completato",
    "GOING_TO_DESTINATION_PENDING": "In viaggio verso la destinazione in sospeso",
    "DELIVERING": "Consegna",
    "DELIVERING_DOING": "Consegna in corso",
    "DELIVERING_DONE": "Consegna completata",
    "DELIVERING_PENDING": "Consegna in sospeso",
    "FINISHED": "Completato",
    "FINISHED_DOING": "Completamento in corso",
    "FINISHED_DONE": "Completamento completato",
    "FINISHED_PENDING": "Completamento in sospeso",
    "TRANSFERRING_FROM_PICKING_TO_STORAGE_DOING": "Trasferimento da raccolta allo stoccaggio in corso",
    "TRANSFERRING_FROM_PICKING_TO_STORAGE_PENDING": "Trasferimento da raccolta allo stoccaggio in sospeso",
    "TRANSFERRING_FROM_PICKING_TO_STORAGE_DONE": "Trasferimento da raccolta allo stoccaggio completato",
    "TRANSFERRING_TO_STORAGE_FROM_PICKING_DOING": "Trasferimento dallo stoccaggio alla raccolta in corso",
    "TRANSFERRING_TO_STORAGE_FROM_PICKING_PENDING": "Trasferimento in sospeso",
    "TRANSFERRING_TO_STORAGE_FROM_PICKING_DONE": "Trasferimento completato",
    "STORING_DOING": "Stoccaggio in corso",
    "STORING_PENDING": "Stoccaggio in sospeso",
    "STORING_DONE": "Stoccaggio completato",
    "TRANSFERRING_FROM_STORAGE_TO_DELIVERY_DOING": "Trasferimento in corso",
    "TRANSFERRING_FROM_STORAGE_TO_DELIVERY_PENDING": "Trasferimento in sospeso",
    "TRANSFERRING_FROM_STORAGE_TO_DELIVERY_DONE": "Trasferimento completato",
    "TRANSFERRING_TO_DELIVERY_FROM_STORAGE_DOING": "Trasferimento in corso",
    "TRANSFERRING_TO_DELIVERY_FROM_STORAGE_PENDING": "Trasferimento in sospeso",
    "TRANSFERRING_TO_DELIVERY_FROM_STORAGE_DONE": "Trasferimento completato",
    "AUDITING_DOING": "Auditing in corso",
    "DONE": "Completato",
    "DOING": "In corso",
    "PENDING": "In sospeso",
    "(P)": "(P)",
    "(D)": "(D)",
    "(F)": "(F)",
    "(S)": "(S)",
    "(C)": "(C)",
    "(Z)": "(Z)"
    },
    "user-actions": {
    "JOB_RESCHEDULED": "Lavoro riprogrammato",
    "CANCELLED": "Lavoro cancellato",
    "PICKING RESET": "Compito di prelievo resettato",
    "DELIVERY RESET": "Compito di consegna resettato",
    "FULL_SERVICE_TASK_ASSIGNED": "Compito di servizio completo assegnato",
    "FULL_SERVICE_TASK_WAS_PROPOSED": "Compito di servizio completo proposto",
    "FULL_SERVICE RESET": "Servizio completo resettato",
    "PICKING_TASK_ASSIGNED": "Compito di prelievo assegnato",
    "DELIVERY_TASK_ASSIGNED": "Compito di consegna assegnato",
    "PICKING_TASK_WAS_PROPOSED": "Compito di prelievo proposto",
    "DELIVERY_TASK_WAS_PROPOSED": "Compito di consegna proposto",
    "STORAGE_TASK_ASSIGNED": "Compito di stoccaggio assegnato",
    "STORAGE_TASK_WAS_PROPOSED": "Compito di stoccaggio proposto",
    "STORAGE RESET": "Stoccaggio resettato",
    "PICK_UP_FOR_DELIVERY_TASK_ASSIGNED": "Compito di spedizione assegnato",
    "PICK_UP_FOR_DELIVERY_TASK_WAS_PROPOSED": "Compito di spedizione proposto",
     "PICK_UP_FOR_DELIVERY RESET": "La spedizione è stata resettata",
    "PICK_UP_TASK_ASSIGNED": "È stata assegnata la consegna",
    "PICK_UP_TASK_WAS_PROPOSED": "È stata proposta la consegna",
    "PICK_UP RESET": "La consegna è stata resettata",
    "PICKING_WITH_STORAGE_TASK_ASSIGNED": "È stata assegnata la selezione",
    "PICKING_WITH_STORAGE_TASK_WAS_PROPOSED": "È stata proposta la selezione",
    "PICKING_WITH_STORAGE RESET": "La selezione è stata resettata",
    "DELIVERY_WITH_STORAGE_TASK_ASSIGNED": "È stata assegnata la consegna con la selezione",
    "DELIVERY_WITH_STORAGE_TASK_WAS_PROPOSED": "È stata proposta la consegna con la selezione",
    "DELIVERY_WITH_STORAGE RESET": "La consegna con la selezione è stata resettata",
    "PICKING_AND_STORAGE_TASK_ASSIGNED": "È stata assegnata la selezione e la conservazione",
    "PICKING_AND_STORAGE_TASK_WAS_PROPOSED": "È stata proposta la selezione e la conservazione",
    "PICKING_AND_STORAGE RESET": "La selezione e la conservazione sono state resettate",
    "PRODUCTS_REJECTED": "Prodotti rifiutati",
    "CREATE ISSUE": "Problema creato",
    "RESET_DELIVERY_CODE": "Sblocca la consegna",
    "MAKES_DELIVERY": "Consegna completata",
    "CHANGE_PAYMENT_METHOD": "Il metodo di pagamento è stato cambiato",
    "UPDATE_PRICES": "Valore dell'ordine aggiornato dall'utente",
    "CHANGE_JOB_STORE": "Il negozio del lavoro è stato cambiato",
    "PRODUCTS_UNDO_REJECTION": "Prodotti rifiutati restituiti aggiunti",
    "CONSOLIDATION_TASK_ASSIGNED": "Assegnata attività di consolidamento",
    "ZONE_PICKING_TASK_ASSIGNED": "Assegnata attività di selezione in zona",
    "UPDATE_PAYMENT_INFO": "Fattura aggiornata",
    "UPDATE_PRODUCT": "Prodotto aggiornato"
    },
    "fleet-capabilities": {
    "DELIVERY": "Autisti",
    "FULL_SERVICE": "Servizio completo",
    "PICKING": "Selezionatori",
    "STORAGE": "Conservazione",
    "DELIVERY_WITH_STORAGE": "Autisti con conservazione",
    "PICKING_WITH_STORAGE": "Selezionatori con conservazione",
    "PICK_UP": "Ritiro",
    "PICK_UP_FOR_DELIVERY": "Ritiro per consegna",
    "PICKING_AND_STORAGE": "Selezionatori e conservazione",
    "ZONE_PICKING": "Selezione in zona",
    "CONSOLIDATION": "Consolidamento"
    },
    "fleet-types": {
    "OWN": "Propria flotta",
    "3PL": "Flotta esternalizzata",
    "CROWD_SOURCE": "Crowdsourcing"
    },
    "header": {
    "greet": "Ciao",
    "phone": {
    "sales": "Nuovo lavoro"
    }
    },
    "empty": {
    "no-data": "Nessun dato",
    "job": "Seleziona un lavoro per vedere i dettagli degli incidenti qui."
    },
    "home": {
    "job": {
    "info": {
    "created": "Creato"
    }
    },
    "title": "Lavori",
    "refresh": {
    "loading": "Ricaricamento...",
    "updated-at": "Ricaricato alle",
    "s": "Ricaricato pochi secondi fa",
    "m": "Ricaricato un minuto fa",
    "mm": "Ricaricato %d minuti fa"
    },
    "table": {
    "reference": "# Riferimento",
    "collectedItems": "Articoli raccolti",
    "checkout": "Creazione",
    "client": "Cliente",
    "pickedBy": "Raccoglitore",
    "deliveredBy": "Autista",
    "delivery": "Consegna",
    "not-assigned": "(Non assegnato)",
    "status": "Stato",
    "created": "Creato",
    "finished": "Finito",
    "filters": {
    "created": "Creato",
    "processing": "Elaborazione",
    "finished": "Finito",
    "cancelled": "Annullato"
    }
    },
    "filters": {
    "title": "Filtri",
    "reference": {
    "placeholder": "Ricerca: Riferimento, Cliente, Email, Telefono..."
    }
    },
    "city": {
    "all": "Tutte le città"
    },
    "stores": "Negozi",
    "status": "Stato",
    "date": "Data",
    "deliveryDate": "Data di consegna",
    "createdDate": "Data di creazione",
    "jobStatus": "Stato dell'ordine",
    "hours": "Orario di consegna",
    "operationModel": "Modello di operazione",
    "cleanFilters": "Pulisci filtri",
    "saveFilters": "Salva filtri",
    "multiSelect": {
    "buttonText": {
    "nothing": "Nessun negozio selezionato",
    "all": "Tutti i negozi selezionati",
    "some": "{{quantity}} negozi selezionati"
    },
    "stores": "Negozi",
    "searchText": "Cerca qui",
    "save": "Salva"
    },
    "rangeOfHours": {
    "title": "Da - A",
    "from": "Da",
    "to": "A",
    "allDay": "Tutto il giorno",
    "select": "Seleziona",
    "save": "Salva"
    },
    "hoursInfo": "Filtrando per l'ora di consegna vedrai tutti gli ordini il cui slot di consegna inizia e finisce entro l'intervallo di tempo scelto.",
    "partialStatus": {
    "title": "Stati parziali",
    "GOING_TO_ORIGIN": "In partenza per l'origine",
    "CREATED": "Creato",
    "PICKING": "Prelevando",
    "PICKING_WITH_PACKING": "Prelievo con imballaggio",
    "CHECKOUT": "Check-out",
    "TRANSFERRING": "Trasferimento",
    "STORING": "Imballaggio",
    "STORED": "Imballato",
    "GOING_TO_DESTINATION": "In partenza per la destinazione",
    "READY_FOR_PICKUP": "Pronto per il ritiro",
    "IN_ROUTE": "In viaggio",
    "DELIVERED": "Consegnando",
    "FINISHED": "Consegnato",
    "CANCELLED": "Annullato",
    "AUDITING": "Verifica"
    }
    },
    "jobModal": {
    "title": "Ordine"
    }
    }

resultado_traduccion = traducir_a_catalan(texto_ingles_italiano)

# Guardar el resultado en un archivo de texto
with open("resultado_traduccion.txt", "w") as archivo:
    archivo.write(resultado_traduccion)

print("La traducción se ha guardado en el archivo resultado_traduccion.txt")
