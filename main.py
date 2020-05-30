import logging.config
import tornado.ioloop
import yaml
import src
from config import base

with open("log.yaml", "r") as f_conf:
    dict_conf = yaml.load(f_conf, Loader=yaml.FullLoader)
    logging.config.dictConfig(dict_conf)

application = base.Application(**base.settings)
print(dir(src))
application.load_handler_module(src)
application.listen(8000)
tornado.ioloop.IOLoop.instance().start()
