import pytest
from checkers import checkout, getout
import yaml
import random
import string
from datetime import datetime

with open('D:\программирование\MyBibliotecForTask\Python\Py for Tester\\task\hw\\02\config.yaml') as f:
    data = yaml.safe_load(f)

# создание папок для тестовых данных


@pytest.fixture()
def make_folders():
    return checkout('mkdri {} {} {} {}'.format(data["folder_in"], data["folder_out1"], data["folder_out2"], data["folder_out3"]), '')

# очистка папок с тестовыми данными после тестов


@pytest.fixture()
def clear_folders():
    return checkout('rm -rf {}/* {}/* {}/* {}/*'.format(data["folder_in"], data["folder_out1"], data["folder_out2"], data["folder_out3"]), '')

# создание тестовых файлов


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data["count_test_files"]):
        filename = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=data["length_name_file"]))
        if checkout('cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock'.format(data["folder_in"], filename, data["bs"]), ''):
            list_of_files.append(filename)
    return list_of_files

# создание подпапки и файла в нем


@pytest.fixture()
def make_subfolder():
    testfile_name = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    subfolder_name = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    if not checkout('cd {}; mkdir {}'.format(data["folder_in"], subfolder_name), ''):
        return None, None
    if not checkout('cd {}/{}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock'.format(data["folder_in"], subfolder_name,
                                                                                              testfile_name, data["bs"]), ''):
        return subfolder_name, None
    else:
        return subfolder_name, testfile_name


@pytest.fixture()
def make_bad_arx():
    checkout(f"cd {data['folder_in']}; 7z a -t{data['arc_type']}{data['folder_out']}/bad_arx",
             "Everything is Ok")
    checkout(
        f"truncate -s 1 {data['folder_out']}/bad_arx.{data['arc_type']}", "")


@pytest.fixture(autouse=True)
def print_time():
    print(f'Start: {datetime.now().strftime("%H:%M:%s.%f")}')
    yield
    print(f'\nFinish: {datetime.now().strftime("%H:%M:%s.%f")}')


@pytest.fixture(autouse=True)
def stat_log():
    yield
    time = datetime.now().strftime("%H:%M:%s.%f")
    stat = getout('sysctl -n vm.loadavg')
    checkout(
        f"echo 'time:{time} count:{data['count_test_files']} size;{data['bs']} stat:{stat}' >> {data['stat_file_path']}", '')
