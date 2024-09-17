import requests  # Biblioteca para realizar solicitudes HTTP
import json  # Biblioteca para trabajar con datos en formato JSON


# Función para obtener direcciones IP y regiones desde un dominio
def obtenerIpDesdeDominio(dominio):
    # Imprime el dominio que se está procesando
    print("-----Dominio -> " + str(dominio) + "-----")

    # Realiza una solicitud a la API de Networkcalc para obtener registros DNS del dominio
    ResultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/" + str(dominio))

    # Verifica si la respuesta contiene registros DNS
    if ResultadoBusqueda.json()['records'] is not None:
        # Itera sobre cada registro de tipo 'A' (dirección IP) en la respuesta
        for i in range(len(ResultadoBusqueda.json()['records']['A'])):
            ip = ResultadoBusqueda.json()['records']['A'][i]['address']  # Obtiene la dirección IP
            print(ResultadoBusqueda.json()['records']['A'][i]['address'])  # Imprime la IP

            # Realiza una solicitud a la API de IPinfo para obtener la región de la IP
            ResultadoRegion = requests.get("https://ipinfo.io/" + str(ip) + "?token=279db8187a133d")

            # Imprime la región de la IP
            print("La región de la IP ->" + str(ip) + " es " + str(ResultadoRegion.json()["region"]))


# Lista de dominios de empresas para los cuales se puede obtener información
dominios_empresas = [
    "avianca.com",
    "bancolombia.com",
    "ecopetrol.com.co",
    "sura.com",
    "cemexcolombia.com",
    "grupobancolombia.com",
    "bancaria.co",
    "alpina.com",
    "grupobavaria.com",
    "une.com.co",
    "postobon.com",
    "hilton.com",
    "falabella.com.co",
    "elnacional.com.co",
    "davivienda.com",
    "unilab.com.co",
    "almacenesexito.com",
    "colpatria.com",
    "cemex.co",
    "sofase.com",
    "jbs.com.co",
    "agronet.gov.co",
    "grupoeconomico.com.co",
    "colsanitas.com",
    "nutresa.com",
    "conalvias.com",
    "dersa.com.co"
]


# Descomentar la siguiente línea para obtener IPs y regiones para cada dominio en la lista
for i in dominios_empresas:
    obtenerIpDesdeDominio(i)

# Función para obtener correos electrónicos desde un dominio
def obtenerEmailsDesdeDominio(dominio):
    # Realiza una solicitud a la API de Hunter.io para obtener correos electrónicos del dominio
    resultadoEmails = requests.get("https://api.hunter.io/v2/domain-search?domain=" + str(
        dominio) + "stripe.com&api_key=fa7e7df55a1b2987a143bad18ca7daab80f3060c")

# Verifica si la respuesta contiene correos electrónicos
    if resultadoEmails.json()['data']['emails'] is not None:
        # Itera sobre cada correo electrónico en la respuesta
        for correo in range(len(resultadoEmails.json()['data']['emails'])):
            # Imprime el correo electrónico
            print("Correo:" + str(resultadoEmails.json()['data']['emails'][correo]['value']))


# Llamada a la función para obtener correos electrónicos desde un dominio específico
# (Nota: El dominio 'stripe.com' en la URL es incorrecto y debería ser removido o reemplazado)
obtenerEmailsDesdeDominio("dersa.com.co")
