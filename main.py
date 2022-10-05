from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

"""
Main objective:
- simple test of a python based whatsapp bot

arq:
- based on python, flask, and ngrok, who communicates to Twilio

so:

question:
human -> whatsapp phone number (twilio) -> ngrok -> flask resource 

answer:
flask resource response -> ngrok -> twilio -> human 

"""

app = Flask(__name__)

@app.route('/bot', methods=['POST'])

def bot():
    
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    # this answers may be send to a api model that gave us feedback about question asked by human
    
    if 'quote' in incoming_msg:
        # return a quote
        r = request.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
        
    # hardcoded answers for testing
    
    if 'hola' in incoming_msg:
        obra = 'bienvenido al bot de Mapainversiones Argentina. Actualmente contamos con 5338 Obras y 1174 Proyectos de obra publicados.\n¿Qué desea hacer?\nEscriba: \n"obras" para conocer información de obras\nEscriba alguna provincia para conocer información de alguna provincia especifica (por ejemplo "Buenos Aires").\nTambién puede consultar por las obras de Infraestructura de cuidad escribiendo "cuidado".'
        msg.body(obra)
        responded = True

    
    if 'obras' in incoming_msg:
        obra = 'Quiere conocer información de cual obra?'
        msg.body(obra)
        responded = True
        
    if 'buenos aires' in incoming_msg:
        obra = 'Perfecto, para conocer información de obras en buenos aires puede hacer click en el siguiente link: https://mapainversiones.obraspublicas.gob.ar/localizacion/LocationProfile#/proyectos/?zoom=6&center=-37.2490331277768,-61.7053197152498&topLeft=-32.28841970442069,-77.1960423714998&bottomRight=-41.90341019349265,-46.2145970589998&departamento=06'
        msg.body(obra)
        responded = True
        
    if 'cuidado' in incoming_msg:
        obra = 'Perfecto, las obras de infraestructura del cuidado son obras destinadas a garantizar el derecho y las condiciones necesarias de quienes reciben y brindan cuidados para reducir brechas de desigualdad (de género, discapacidad, generacional y territorial).\nHaga click en el link para acceder a las obras de Centros de Desarrollo Infantil: https://mapainversiones.obraspublicas.gob.ar/Infra/FichaCentros/?id=10\nHaga click para en el link para acceder a las obras de Género y Diversidad: https://mapainversiones.obraspublicas.gob.ar/Infra/FichaCentros/?id=11\n o puede consultar Otras obras de Infraestructura del cuidado en el siguiente link: https://mapainversiones.obraspublicas.gob.ar/Infra/FichaCentros/?id=12'
        msg.body(obra)
        responded = True
                      
                      
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
             
        
        
                           
    if not responded:
        msg.body('sin respuesta')
        
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
