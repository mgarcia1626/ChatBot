import logging
from flask import current_app, jsonify
import json
import requests
from app.utils import variables
from app.utils.variables import socio

#print(variables.count)

# from app.services.openai_service import generate_response
import re


def log_http_response(response):
    logging.info(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")


def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )
    


def generate_response(response):
    # Return text in uppercase
    return response


def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
    }

    url = f"https://graph.facebook.com/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"

    try:
        response = requests.post(
            url, data=data, headers=headers, timeout=10
        )  # 10 seconds timeout as an example
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.Timeout:
        logging.error("Timeout occurred while sending message")
        return jsonify({"status": "error", "message": "Request timed out"}), 408
    except (
        requests.RequestException
    ) as e:  # This will catch any general request exception
        logging.error(f"Request failed due to: {e}")
        return jsonify({"status": "error", "message": "Failed to send message"}), 500
    else:
        # Process the response as normal
        log_http_response(response)
        return response


def process_text_for_whatsapp(text):
    # Remove brackets
    pattern = r"\【.*?\】"
    # Substitute the pattern with an empty string
    text = re.sub(pattern, "", text).strip()

    # Pattern to find double asterisks including the word(s) in between
    pattern = r"\*\*(.*?)\*\*"

    # Replacement pattern with single asterisks
    replacement = r"*\1*"

    # Substitute occurrences of the pattern with the replacement
    whatsapp_style_text = re.sub(pattern, replacement, text)

    return whatsapp_style_text


def process_whatsapp_message(body):
    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    message_body = message["text"]["body"]
           
    #if para salvar informacion

    if variables.count==0:
        ToSend="1) hacerme socio\n2) reservar cancha"
        variables.nuevo_Socio.poner_nombre(None)
        variables.nuevo_Socio.Poner_documento(None)
        variables.count=1
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)

    elif message_body=="1" and variables.count==1:
        #variables.nuevo_Socio.poner_nombre(None)
        #variables.nuevo_Socio.Poner_documento(None)
        ToSend="Introduzca nombre y apellido"
        variables.count=2
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)

    elif variables.count==2:
        variables.nuevo_Socio.poner_nombre(message_body)
        variables.count=3
        ToSend="Introduzca Documento"
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)

    elif variables.count==3:
        variables.nuevo_Socio.Poner_documento(message_body)
        variables.count=4
        #print("ESTE ES EL NUEVO SOCIO",variables.nuevo_Socio.nombre)
        ToSend="Estan sus datos correctos?"+"\nNombre y apellido : "+ str(variables.nuevo_Socio.nombre) + "\nDocumento : " + str(variables.nuevo_Socio.documento) + "\nResponda Si o No"
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)
        #data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(variables.nuevo_Socio))
        #send_message(data)

    elif variables.count==4 and message_body=="Si":
        variables.agregar_aLista(variables.nuevo_Socio)
        #print(str(variables.socios[0]))
        variables.count=0
        variables.data_socio()
        ToSend="Gracias , recuerde que no tenemos natacion"
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)

    elif variables.count==4 and message_body=="No":
        variables.count=2
        variables.nuevo_Socio.poner_nombre(None)
        variables.nuevo_Socio.Poner_documento(None)
        ToSend="Por favor vuelva a introducir su nombre y apellido"
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response(ToSend))
        send_message(data)

    elif message_body=="2":
        ToSend="Diga horario que desa reservar"
        variables.count=0
        data = get_text_message_input(current_app.config["RECIPIENT_WAID"], generate_response("GRACIAS"))
        send_message(data)
    
    else:
        ToSend="introduzca los datos correctamente"
        variables.count=200000000000
        print(variables.count)
    
    # TODO: implement custom function here
    #response = generate_response(ToSend)

    # OpenAI Integration
    # response = generate_response(message_body, wa_id, name)
    # response = process_text_for_whatsapp(response)

    #data = get_text_message_input(current_app.config["RECIPIENT_WAID"], response)
    #send_message(data)


def is_valid_whatsapp_message(body):
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.
    """
    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )
