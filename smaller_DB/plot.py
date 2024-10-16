import threading
from PIL import Image, ImageFilter
import time
import os
import psutil
import matplotlib.pyplot as plt

# Função para processar uma imagem
def process_image(filename, input_directory, output_directory):
    original_image = Image.open(os.path.join(input_directory, filename))
    box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
    output_filename = f"{os.path.splitext(filename)[0]}_blurred.jpg"
    box_blurred_image.save(os.path.join(output_directory, output_filename))

# Função para processar imagens sequencialmente
def process_images_sequentially(input_directory, output_directory):
    start_time = time.time()
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            original_image_path = os.path.join(input_directory, filename)
            original_image = Image.open(original_image_path)
            box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
            output_filename = f"{os.path.splitext(filename)[0]}_blurred.jpg"
            box_blurred_image.save(os.path.join(output_directory, output_filename))
    end_time = time.time()
    return end_time - start_time

# Função para processar imagens com threads
def process_images_with_threads(input_directory, output_directory):
    start_time = time.time()
    threads = []
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            thread = threading.Thread(target=process_image, args=(filename, input_directory, output_directory))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time

# Função para monitorar uso da CPU
def monitor_cpu_usage(duration):
    cpu_usage = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage.append(psutil.cpu_percent(interval=0.5))
    return cpu_usage

# Cria o diretório de saída, se não existir
output_directory = 'smaller_DB/images/outputs'
os.makedirs(output_directory, exist_ok=True)

# Caminho do diretório de entrada
input_directory = 'smaller_DB/images/inputs'

# Executa os processamentos e monitora a CPU
# Para processamento sequencial
start_cpu_monitor = time.time()
cpu_usage_sequential = monitor_cpu_usage(5)  # Monitora durante 5 segundos
sequential_time = process_images_sequentially(input_directory, output_directory)
end_cpu_monitor = time.time()

# Para processamento com threads
start_cpu_monitor = time.time()
cpu_usage_threaded = monitor_cpu_usage(5)  # Monitora durante 5 segundos
threaded_time = process_images_with_threads(input_directory, output_directory)
end_cpu_monitor = time.time()

# Plotando os resultados de tempo de processamento
methods = ['Sequencial', 'Threads']
times = [sequential_time, threaded_time]

plt.figure(figsize=(12, 5))

# Gráfico de Tempo de Processamento
plt.subplot(1, 2, 1)
plt.bar(methods, times, color=['blue', 'orange'])
plt.ylabel('Tempo de Processamento (segundos)')
plt.title('Comparação de Desempenho: Processamento de Imagens')
plt.grid(axis='y')

# Gráfico de Utilização da CPU
plt.subplot(1, 2, 2)
plt.plot(cpu_usage_sequential, label='Sequencial', color='blue')
plt.plot(cpu_usage_threaded, label='Threads', color='orange')
plt.ylabel('Uso da CPU (%)')
plt.title('Utilização da CPU durante o Processamento')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
