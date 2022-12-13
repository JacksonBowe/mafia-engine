import logging

logger = logging
logger.basicConfig(filename="log.txt",
        level=logging.DEBUG, 
        format="[%(filename)-15s][%(funcName)-15s][%(levelname)-8s] %(message)s",
        filemode="w")

