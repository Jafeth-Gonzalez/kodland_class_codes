def get_significate(word , dictionary):
    if word in dictionary.keys():
        return dictionary[word]# devolver el significado de la palabra 
    else:
        return "No se encuentra en el diccionario , lo siento" # que le devuelvo ¿? no hay significado para su palabra
#el diccionario fue hecho por chatgpt , a mi me dio pereza 
slang_diccionario = {
    "LOL": "una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL": "una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}
significate = get_significate(input("Escribe una palabra que no entiendas (¡con mayúsculas!): "),slang_diccionario) #me es mas facil asi
print(significate)#no se que comentar ya que decir  que decir "devuelve  el significado" es muy obvio  y no se como dar contexto

