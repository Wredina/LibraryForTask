import subprocess


def execute_command_and_check_output(command, text_to_find):
    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode == 0 and text_to_find in result.stdout:
            # print(result.stdout)  # Пример: drwxr-xr-x  3 dmitrii_kobozev  staff   96 17 дек 22:24 HW_1
            return True
        else:
            return False
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return False


# Пример использования функции
command_to_execute = "ls -l"  # Команда, которую исполняем
text_to_find_in_output = "HW_1"  # Текст, который будет найден в выводе команды

result = execute_command_and_check_output(
    command_to_execute, text_to_find_in_output)
print(result)
