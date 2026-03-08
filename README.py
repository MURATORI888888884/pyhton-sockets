# pyhton-sockets
um codigo de ver quais portas estao abertas em determinados ips
import socket

client="45.33.32.156"#definindo o ip do alvo 

print(f"scaneando as portas disponiveis em {client}")
list_de_ports = [21, 22, 80, 111, 443, 3306]#criando um array com listas de portas possiveis


for scan in list_de_ports:#criando um laço for para scanear cada elemento do meu array
    ports=socket.socket()#definindo um socket
    ports.settimeout(1.0)#definindo um tempo para a conexao
    
    scanner = ports.connect_ex((client,scan))#scaneando e se conectando  
    #verificando quais portas estao abertas 
    if scanner == 0:
        print(f"[*] portas encontradas em{scanner}")
    else:
        print(f"porta {scanner} PORTA[-]: fechada")
    #fechando conexao 
ports.close()
print("concluido")
