
mochila = ["pan","roca","sable de luz","agua","vendaje","ropa"]
contador=0

def usar_la_fuerza(lista,contador):
    if len(lista)==0:
        return -1
    elif lista[-1]=="sable de luz":
        return contador
    else:
        contador=contador+1
        return usar_la_fuerza(lista[:-1],contador)
contador=usar_la_fuerza(mochila,contador)
print ("fue necesario", [contador], "sacar objetos")      
