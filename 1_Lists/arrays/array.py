# Uma estrutura de dados capaz de armazenar varios elementos em uma única variável

# Em vez de fazer isto
carro1 = "Toyota"
carro2 = "Mercedez"
carro3 = "Ford"

# Você pode fazer isso
carros = ["Toyota", "Mercedez", "Ford"]

# Podendo acessa-lo atravez dos colchetes
print(carros[0]) # Saída: "Toyota"

# Ou até mesmo atravez de variáveis 
x = carros[2]
print(x) # Saída: "Ford"

# Adicionar elementos
carros.append("Hyundai")

# Removendo elementos
carros.pop() # o pop retira específicamente o ultimo elemento por padrão (isso será importante para as outras estruturas)
# Ou
carros.remove("Toyota") # Retira um elemento específico do array

# Para saber o tamanho do array
print(len(carros)) # Saída: 2

