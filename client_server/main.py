"""
Sa se implementeze o aplicatie client/server (modalitatea de comunicatie intre client si server e la latitudinea ta,
sockets, web requests, alt protocol, whatever) care sa fie impartita astfel:

    Clientul itereaza o cale data in linia de comanda, iterand directoare/subdirectoare/fisiere din calea respectiva si
    va trimite aceasta lista fisier cu fisier in timpul iterarii catre server prin protocolul ales anterior

    Serverul va primi aceasta lista si, intr-un mod efficient (adica multithreaded) va trebui sa proceseze fiecare
    fisier din lista si pentru fiecare fisier sa afiseze la consola un json output in care sa se regaseasca urmatoarele:
        Nume fisier
        Size fisier
        Data ultimei modificari
        Data crearii
        Un hash MD5 peste continutul fisierului
"""
from client import Client


#
# webServer = HTTPServer((hostName, serverPort), MyServer)
# print("Server started http://%s:%s" % (hostName, serverPort))

# webServer.serve_forever()
# webServer.server_close()
# print("Server stopped.")

"""
Questions:
- Cum se realizeaza transmiterea de creation_time si modified_date pentru fisiere transferate prin http
- md5 hash
- 
"""
