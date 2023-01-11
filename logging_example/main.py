
from logging_module import logging_module


log_obj1 = logging_module.setup_logger("logger_check1")
log_obj2 = logging_module.setup_logger("logger_check2")

log_obj1.info("logging started")
log_obj2.info("logging started")

