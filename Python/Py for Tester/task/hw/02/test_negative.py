from checkers import checkoutneg
from logging_fucn import log_neg_step_info
import yaml

with open('D:\программирование\MyBibliotecForTask\Python\Py for Tester\\task\hw\\02\config.yaml') as f:
    data = yaml.safe_load(f)


def test_negstep1():
    STEP = 1
    log_neg_step_info(STEP)
    assert checkoutneg(
        f'cd {data["folder_out1"]}; 7zz e bad_arx.{data["arc_type"]} -o{data["folder_out2"]} -y', 'ERROR')


def test_negstep2():
    STEP = 2
    log_neg_step_info(STEP)
    assert checkoutneg(
        f'cd {data["folder_out1"]}; 7zz t bad_arx.{data["arc_type"]}', 'ERROR')


if __name__ == '__main__':
    test_negstep1()
    test_negstep2()
