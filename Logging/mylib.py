# @Author: @IamRezaMousavi
# @Date:   2022-04-14 06:16:23
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-14 06:29:38

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logHandler = logging.FileHandler('log/project.log')
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(
    logging.Formatter(
        '%(asctime)s|%(name)s|%(levelname)s|%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    ),
)
logger.addHandler(logHandler)


def doSomething():
    logger.debug("IT'S DONE")
