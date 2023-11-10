import spacy
from spacypdfreader.spacypdfreader import pdf_reader


nlp = spacy.load('es_core_news_sm')

# Convertir el texto del PDF a una lista de oraciones
doc = pdf_reader('SPT.pdf', nlp)

def procesar_consulta(consulta):
    palabras_clave = consulta.split()
    for palabra in palabras_clave:
        if palabra in ["diseño", "sistema", "puesta a tierra"]:
            return True

    # Agregar entidades nombradas al diccionario de palabras clave
    for entity in doc.ents:
        palabras_clave.append(entity.text)

    return palabras_clave in palabras_clave

def extraer_texto_relevante(doc, consulta):
    for sent in doc.sents:
        for token in sent:
            if token.text in consulta:
                respuesta = sent.text
                return respuesta
    return None

def imprimir_respuesta(respuesta):
    if respuesta is None:
        print("No se encontró información relevante")
    else:
        print(respuesta)

# Consulta del usuario
user_query = "¿Cómo puedo diseñar con IEEE-80?"

# Procesar la consulta
if procesar_consulta(user_query):
    # Extraer el texto relevante
    respuesta = extraer_texto_relevante(doc, user_query)
    # Imprimir la respuesta
    imprimir_respuesta(respuesta)
