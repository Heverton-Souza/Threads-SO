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

# Função para processar imagens usando monothread
def process_images_monothread(input_directory, output_directory):
    start_time = time.time()
    for filename in os.listdir(input_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            process_image(filename, input_directory, output_directory)
    end_time = time.time()
    return end_time - start_time

# Função para processar usando multithreads
def process_images_multithreads(input_directory, output_directory):
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

# Função para monitorar recursos do sistema
def monitor_system_usage(duration):
    cpu_usage = []
    memory_usage = []
    disk_usage = []
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage.append(psutil.cpu_percent(interval=0.5))
        memory_usage.append(psutil.virtual_memory().percent)
        disk_usage.append(psutil.disk_usage('/').percent)
    return cpu_usage, memory_usage, disk_usage

# Caminhos de entrada e saída
output_directory = 'bigger_DB/images/outputs'
input_directory = 'bigger_DB/images/inputs'
os.makedirs(output_directory, exist_ok=True)

# Monitoramento e processamento usando monothread
cpu_usage_mono, memory_usage_mono, disk_usage_mono = monitor_system_usage(5)
monothread_time = process_images_monothread(input_directory, output_directory)

# Monitoramento e processamento usando multithreads
cpu_usage_multi, memory_usage_multi, disk_usage_multi = monitor_system_usage(5)
multithreads_time = process_images_multithreads(input_directory, output_directory)

# Comparação de tempo
methods = ['Monothread', 'Multithreads']
times = [monothread_time, multithreads_time]

# Gráficos
plt.figure(figsize=(15, 10))

# Gráfico de Tempo de Processamento
plt.subplot(2, 2, 1)
plt.bar(methods, times, color=['blue', 'orange'])
plt.ylabel('Tempo de Processamento (segundos)')
plt.title('Comparação de Desempenho: Tempo de Processamento')
plt.grid(axis='y')

# Gráfico de Utilização da CPU
plt.subplot(2, 2, 2)
plt.plot(cpu_usage_mono, label='Monothread', color='blue')
plt.plot(cpu_usage_multi, label='Multithreads', color='orange')
plt.ylabel('Uso da CPU (%)')
plt.title('Utilização da CPU')
plt.legend()
plt.grid()

# Gráfico de Utilização da Memória
plt.subplot(2, 2, 3)
plt.plot(memory_usage_mono, label='Monothread', color='blue')
plt.plot(memory_usage_multi, label='Multithreads', color='orange')
plt.ylabel('Uso da Memória (%)')
plt.title('Utilização da Memória')
plt.legend()
plt.grid()

# Gráfico de Utilização do Disco
plt.subplot(2, 2, 4)
plt.plot(disk_usage_mono, label='Monothread', color='blue')
plt.plot(disk_usage_multi, label='Multithreads', color='orange')
plt.ylabel('Uso do Disco (%)')
plt.title('Utilização do Disco')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
