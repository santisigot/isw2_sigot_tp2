import openai

# Configura tu clave de API de OpenAI
api_key = "sk-zVEphpsqWn2bdRBxjq5pT3BlbkFJ9zBjEL2FKzRyEVBPR7wd2"
openai.api_key = api_key

def obtener_respuesta_gpt3(consulta):
    # Configura el modelo y los parámetros
    modelo = "text-davinci-003" # Cambiar al modelo deseado
    temperatura = 0.7
    max_tokens = 150
    top_p = 1
    penalizacion_frecuencia = 0
    penalizacion_presencia = 0

    # Crea la solicitud para el API de OpenAI
    solicitud = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": "Contexto de conversación."},
            {"role": "user", "content": f"You: {consulta}"}
        ],
        "temperature": temperatura,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": penalizacion_frecuencia,
        "presence_penalty": penalizacion_presencia
    }

    # Obtiene la respuesta del API de OpenAI
    respuesta = openai.Completion.create(**solicitud)

    # Devuelve el contenido de la respuesta
    return respuesta.choices[0].message.content

def main():
    # Solicita consulta al usuario
    consulta_usuario = input("Ingrese su consulta: ")

    # Verifica si la consulta tiene texto
    if consulta_usuario:
        print("Consulta del usuario:", consulta_usuario)

        # Obtiene respuesta de chatGPT
        respuesta_gpt3 = obtener_respuesta_gpt3(consulta_usuario)

        # Imprime respuesta de chatGPT
        print("chatGPT:", respuesta_gpt3)
    else:
        print("La consulta está vacía. Intente nuevamente.")

if __name__ == "__main__":
    main()