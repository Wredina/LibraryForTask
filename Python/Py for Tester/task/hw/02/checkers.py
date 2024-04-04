import logging
import yaml

with open('D:\программирование\MyBibliotecForTask\Python\Py for Tester\\task\hw\\02\config.yaml') as f:
    data = yaml.safe_load(f)

# Логгирование
FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO,
                    filename=data['logging_file_path'],
                    filemode="a", format=FORMAT, encoding="utf-8")


def log_assert_error(step, message):
    logging.error(f"Step {step}: {message}\n")


def log_step_info(step, message):
    logging.info(f'Step {step}: \n Result:\n{message}\n')


def log_neg_step_info(step):
    logging.info(f'Negative Step {step}')


def log_checkout_func(message):
    logging.info(f'Result def(checkout): \n {message}')


def log_checkout_negative_func(message):
    logging.info(f'Result def(checkout_negative): \n {message}')


def log_check_hash(output_hash):
    logging.info(f'Result def(checkhash): \n {output_hash}')


def log_check_crc32_hash(crc32c_hash):
    logging.info(f'Result def(calculate_crc32c): \n {crc32c_hash}')


def log_exception(step, message):
    logging.exception(f'{step}:\n {message}')
