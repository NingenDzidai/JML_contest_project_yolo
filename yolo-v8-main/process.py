import glob
import os
import random
from sklearn.model_selection import train_test_split

# Текущая директория
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

current_dir +='/obj'

# Создание папок, если они не существуют
os.makedirs('data/train', exist_ok=True)
os.makedirs('data/val', exist_ok=True)
os.makedirs('data/test', exist_ok=True)

# Создание или очистка файлов train.txt, val.txt и test.txt
file_train = open('data/train.txt', 'w')
file_val = open('data/val.txt', 'w')
file_test = open('data/test.txt', 'w')

# Считаем все изображения в директории
image_files = glob.glob(os.path.join(current_dir, "*.jpg"))

# Функция для получения пути к файлу аннотации
def get_annotation_file(image_file):
    return os.path.splitext(image_file)[0] + ".txt"

# Проверяем, что для каждого изображения существует файл аннотации
image_files = [f for f in image_files if os.path.exists(get_annotation_file(f))]

# Разделение на тренировочную, валидационную и тестовую выборки
train_files, test_files = train_test_split(image_files, test_size=0.2, random_state=42)
train_files, val_files = train_test_split(train_files, test_size=0.1, random_state=42)

# Функция для записи путей к изображениям и аннотациям
def write_files(file_list, file_handle):
    for file in file_list:
        file_handle.write(file + "\n")

# Запись путей к файлам в соответствующие файлы
write_files(train_files, file_train)
write_files(val_files, file_val)
write_files(test_files, file_test)

# Закрытие всех файлов
file_train.close()
file_val.close()
file_test.close()

# Перемещение файлов в соответствующие директории
def move_files(file_list, target_folder):
    for file in file_list:
        annotation_file = get_annotation_file(file)
        os.rename(file, os.path.join(target_folder, os.path.basename(file)))
        os.rename(annotation_file, os.path.join(target_folder, os.path.basename(annotation_file)))

move_files(train_files, 'data/train')
move_files(val_files, 'data/val')
move_files(test_files, 'data/test')
