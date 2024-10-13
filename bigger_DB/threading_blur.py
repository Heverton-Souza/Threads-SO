import threading
from PIL import Image, ImageFilter
import time
import os

# Função para processar uma imagem
def process_image(filename, input_directory, output_directory):
    original_image = Image.open(os.path.join(input_directory, filename))
    box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
    output_filename = f"{os.path.splitext(filename)[0]}_blurred.jpg"
    box_blurred_image.save(os.path.join(output_directory, output_filename))

# Cria o diretório de saída, se não existir
output_directory = 'bigger_DB/images/outputs'

# Começa um timer
start_time = time.time()

# Lista para manter as threads
threads = []

# Caminho do diretório de entrada
input_directory = 'bigger_DB/images/inputs'

# Cria e inicia as threads para cada imagem no diretório
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filtra apenas arquivos de imagem
        thread = threading.Thread(target=process_image, args=(filename, input_directory, output_directory))
        threads.append(thread)  # Adiciona a thread à lista
        thread.start()  # Inicia a thread

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

# Para o timer
end_time = time.time()

# Calcula e printa o tempo de processamento
processing_time = end_time - start_time
print(f"Tempo de processamento: {processing_time:.4f} segundos")
