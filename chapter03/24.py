from time import sleep
from datetime import datetime

# デフォルト値に動的な値を入れたときにうまくいかない！
# 一度しか評価されないため


def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hi there!')
sleep(0.5)
log('Hi again!')

# 回避するためにNoneをデフォルトでいれる、そのことをdocstringで説明する


def log2(message, when=None):
    """Log a message to print.

    Args:
        message (str): Message to print.
        when ([type], optional): datetime of when the message occured.
                                  Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log2('Hi there!')
sleep(0.5)
log2('Hi again!')
