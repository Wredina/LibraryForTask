import os
import yaml
from checkers import checkout, calculate_crc32c, checkhash
from logging_fucn import log_step_info, log_assert_error, log_exception
from messages import error_message, positive_result

with open('D:\программирование\MyBibliotecForTask\Python\Py for Tester\\task\hw\\02\config.yaml') as f:
    data = yaml.safe_load(f)

# Простая архивация


def test_step1(make_folders, clear_folders, make_files):
    STEP = 1
    try:
        res = []
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        res.append(
            checkout(f'ls {data["folder_out1"]}', f'arx2.{data["arc_type"]}'))
        log_step_info(STEP, res)
        assert all(res), error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)

# Простое извлечение


def test_step2(clear_folders, make_files):
    STEP = 2
    try:
        res = []
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz e arx2.{data["arc_type"]} -o{data["folder_out2"]} -y', positive_result()))
        log_step_info(STEP, res)
        for item in make_files:
            res.append(checkout(f'ls {data["folder_out2"]} ', item))
            log_step_info(STEP, res)
        assert all(res), "test2 Fail"
    except AssertionError as e:
        log_exception(STEP, e)

# Тест архивирования


def test_step3(make_folders, clear_folders, make_files):
    STEP = 3
    try:
        res = checkout(
            f'cd {data["folder_out1"]}; 7zz t arx2.{data["arc_type"]}', positive_result())
        log_step_info(STEP, res)
        assert res, error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)

# Обновление архива


def test_step4(make_folders, clear_folders, make_files):
    STEP = 4
    try:
        res = []
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz u arx2.{data["arc_type"]}', positive_result()))
        log_step_info(STEP, res)
        assert all(res), error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)

# Удаление данных из архива


def test_step5(make_folders, clear_folders, make_files):
    STEP = 5
    try:
        res = []
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz d arx2.{data["arc_type"]}', positive_result()))
        log_step_info(STEP, res)
        assert all(res), error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)

# Просмотр файлов в архиве


def test_step6(make_folders, clear_folders, make_files):
    STEP = 6
    try:
        res = []
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        for item in make_files:
            res.append(
                checkout(f'cd {data["folder_out1"]}; 7zz l arx2.{data["arc_type"]}', item))
            log_step_info(STEP, res)
        assert all(res), error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)

# Извлечение с общим путем


def test_step7(clear_folders, make_files, make_subfolder):
    STEP = 7
    try:
        res = []
        # архивация
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        # разархивация
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz x arx2.{data["arc_type"]} -o{data["folder_out3"]} -y', positive_result()))
        log_step_info(STEP, res)
        # проверка с помощью subprocess что есть файлы не в под папке
        for item in make_files:
            res.append(checkout(f'ls {data["folder_out3"]}', item))
            log_step_info(STEP, res)
        # проверка с помощью os что есть файлы не в под папке
        for item in make_files:
            res.append(os.path.exists(os.path.join(data["folder_out3"], item)))
            log_step_info(STEP, res)
        # проверка с помощью subprocess что есть подпапка
        res.append(checkout(f'ls {data["folder_out3"]}', make_subfolder[0]))
        log_step_info(STEP, res)
        # проверка с помощью subprocess что в подпапке есть файл
        res.append(checkout(f'ls {data["folder_out3"]}', make_subfolder[1]))
        log_step_info(STEP, res)
        # проверка с помощью os что в подпапке есть файл
        res.append(os.path.exists(os.path.join(
            data["folder_out3"], make_subfolder[0], make_subfolder[1])))
        log_step_info(STEP, res)
        assert all(res), error_message(STEP)
    except AssertionError as e:
        log_exception(STEP, e)


def test_step8(make_folders, clear_folders, make_files):
    STEP = 8
    try:
        res = []
        # архивация
        res.append(checkout(
            f'cd {data["folder_in"]}; 7zz a -t{data["arc_type"]} {data["folder_out1"]}/arx2', positive_result()))
        log_step_info(STEP, res)
        # разархивация
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz e arx2.{data["arc_type"]} -o{data["folder_out2"]} -y', positive_result()))
        log_step_info(STEP, res)

        # проверка хэша файлов до разархивации
        for item in make_files:
            res.append(
                checkout(f'cd {data["folder_in"]}; 7zz h {item}', positive_result()))
            log_step_info(STEP, res)
            # считаем хэш через 7z
            actual_hash = checkhash(f'cd {data["folder_in"]}; 7zz h {item}')
            log_step_info(STEP, actual_hash)
            # считаем хэш через аналог crc32 для macos - cksum
            expected_hash = calculate_crc32c(
                os.path.join(data["folder_in"], item)).upper()
            log_step_info(STEP, expected_hash)
            # сравниваем хэши
            res.append(
                checkout(f'cd {data["folder_in"]}; 7zz h {item}', expected_hash))
            log_step_info(STEP, res)

        # проверка хэша архива
        # проверяем что хэш успешно посчитался через 7z
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz h arx2.{data["arc_type"]}', positive_result()))
        log_step_info(STEP, res)
        # считаем хэш через 7z
        actual_hash = checkhash(
            f'cd {data["folder_out1"]}; 7zz h arx2.{data["arc_type"]}')
        log_step_info(STEP, actual_hash)
        # считаем хэш через аналог crc32 для macos - cksum
        expected_hash = calculate_crc32c(os.path.join(
            data["folder_out1"], f'arx2.{data["arc_type"]}')).upper()
        log_step_info(STEP, expected_hash)
        # сравниваем хэши
        res.append(checkout(
            f'cd {data["folder_out1"]}; 7zz h arx2.{data["arc_type"]}', expected_hash))
        log_step_info(STEP, res)

        # проверка хэша файлов после разархивации
        # проверяем что хэш успешно посчитался через 7z
        for item in make_files:
            res.append(
                checkout(f'cd {data["folder_out2"]}; 7zz h {item}', positive_result()))
            log_step_info(STEP, res)
            # считаем хэш через 7z
            actual_hash = checkhash(f'cd {data["folder_out2"]}; 7zz h {item}')
            log_step_info(STEP, actual_hash)
            # считаем хэш через аналог crc32 для macos - cksum
            expected_hash = calculate_crc32c(
                os.path.join(data["folder_out2"], item)).upper()
            log_step_info(STEP, expected_hash)
            # сравниваем хэши
            res.append(
                checkout(f'cd {data["folder_out2"]}; 7zz h {item}', expected_hash))
            log_step_info(STEP, res)

        assert all(
            res), f"{error_message(STEP)}: \n Hash mismatch: Expected {expected_hash}, Actual {actual_hash}"
    except AssertionError as e:
        log_exception(STEP, e)

# очищаем все папки с файлами и проверяем что отчистилось


def test_step0(clear_folders):
    STEP = 0
    assert clear_folders, error_message(STEP, clear_folders)


if __name__ == '__main__':
    test_step1()
    test_step2()
    test_step3()
    test_step4()
    test_step5()

    test_step1()
    test_step6()
    test_step7()
    test_step8()

    test_step0()
