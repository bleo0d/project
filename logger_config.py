import logging
import os
os.makedirs('logs', exist_ok=True)

logging.basicConfig(level=logging.DEBUG,
                    filename='logs/app.log',
                    format='%(levelname)s %(asctime)s %(message)s (Line:%(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8',
                    filemode='a'
                    )