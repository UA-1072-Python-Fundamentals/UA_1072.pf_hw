import logging

logging.basicConfig(level=logging.INFO,
                    filename='app.log',
                    filemode='a',
                    format='%(asctime)s - %(process)d- %(levelname)s - %(name)s - %(message)s')

def log_param(func):
    def wrap(*args, **kwargs):
        logging.info(f"{func.__name__} {args=} {kwargs=}")
        result = func(*args, **kwargs)
        return result
    return wrap


if __name__ == "__main__":
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
