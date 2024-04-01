import openai

# Configurar tu clave de API de OpenAI
api_key = "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"
openai.api_key = api_key

def obtener_respuesta_gpt3(context, usertask, userquery):
    try:.
        # Crear la solicitud para el API de OpenAI
        solicitud = {
            "model": "gpt-3.5-turbo-0125",
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": usertask},
                {"role": "user", "content": userquery}
            ],
            "temperature": 1,
            "max_tokens": 4096,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Obtener la respuesta del API de OpenAI
        respuesta = openai.ChatCompletion.create(**solicitud)

        # Devolver el contenido de la respuesta
        return respuesta.choices[0].message.content
    except Exception as e:
        print("Error al obtener respuesta de GPT-3:", e)
        return None

def main():
    while True:
        try:
            # Aceptar consulta del usuario
            context = input("Contexto de la conversación: ")
            usertask = input("Tarea del usuario: ")
            userquery = input("Consulta del usuario ('q' para salir): ")

            # Salir si el usuario ingresa 'q'
            if userquery.lower() == 'q':
                print("Saliendo del programa...")
                break

            # Verificar si la consulta tiene texto
            if userquery:
                print("Consulta del usuario:", userquery)

                # Obtener respuesta de chatGPT
                respuesta_gpt3 = obtener_respuesta_gpt3(context, usertask, userquery)

                if respuesta_gpt3:
                    # Imprimir respuesta de chatGPT
                    print("chatGPT:", respuesta_gpt3)
                else:
                    print("No se pudo obtener una respuesta.")
            else:
                print("La consulta está vacía. Intente nuevamente.")
        except Exception as e:
            print("Error en la ejecución del programa:", e)

if __name__ == "__main__":
    main()
