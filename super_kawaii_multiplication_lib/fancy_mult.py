from functools import reduce
import operator
from loguru import logger



def _private_multiplication(*args):
    return reduce(operator.mul, args, 1)

def private_but_not_really_multiplication(*args):
    return reduce(operator.mul, args, 1)

def fancy_multiplication(*args):
    logger.debug(f"Will multiply, in a fancy way, the following arguments: {args}")
    return _private_multiplication(*args)