tamanho_pacote = float(input("Qual o tamanho do pacote a ser baixado:(MB) "))
velocidade_internet = float(input("Qual a velocidade de seu link de internet:(Mbps) "))
velocidadeMB = (velocidade_internet/8)*60
tempo_download = tamanho_pacote/velocidadeMB
print(f"Para baixar um pacote de {tamanho_pacote:.2f} MB com um link de {velocidade_internet:.2f} Mbps. Serão necessários {tempo_download:.2f} minutos.")
