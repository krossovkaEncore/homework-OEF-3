import os
import sys
import platform


os_name = os.name
current_directory = os.getcwd()
python_version = sys.version
system_name = platform.system()
system_version = platform.version()
machine = platform.machine()
processor = platform.processor()


system_info = [
    os_name,
    current_directory,
    python_version,
    system_name,
    system_version,
    machine,
    processor
]

while True:
    sys.stdout.write("\n")
    sys.stdout.write("===== ДИАГНОСТИКА СИСТЕМЫ =====\n")
    sys.stdout.write("1. тип операционной системы\n")
    sys.stdout.write("2. текущая директория\n")
    sys.stdout.write("3. аерсия Python\n")
    sys.stdout.write("4. название операционной системы\n")
    sys.stdout.write("5. версия операционной системы\n")
    sys.stdout.write("6. архитектура компьютера\n")
    sys.stdout.write("7. процессор\n")
    sys.stdout.write("0. выход\n")
    sys.stdout.write("===============================\n")

    sys.stdout.write("Выберите пункт: ")
    sys.stdout.flush()

    choice = sys.stdin.readline().strip()

    match choice:
        case "1":
            sys.stdout.write(f"тип ОС: {system_info[0]}\n")

        case "2":
            sys.stdout.write(f"текущая директория: {system_info[1]}\n")

        case "3":
            sys.stdout.write(f"версия Python: {system_info[2]}\n")

        case "4":
            sys.stdout.write(f"операционная система: {system_info[3]}\n")

        case "5":
            sys.stdout.write(f"версия ОС: {system_info[4]}\n")

        case "6":
            sys.stdout.write(f"архитектура: {system_info[5]}\n")

        case "7":
            sys.stdout.write(f"процессор: {system_info[6]}\n")

        case "0":
            sys.stdout.write("программа завершена.\n")
            break

        case _:
            sys.stdout.write("error: такого пункта нет.\n")
