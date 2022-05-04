# py-logger

## 概要

ある程度汎用的に使いまわせるような Python の logger  
必要に応じて `logger.logger` の設定はいじる

## 使い方

```python
from logger import initialize_logger

logger = initialize_logger(__name__)

logger.debug('Debug Message')
logger.info('Info Message')
logger.warning('Warning Message')
logger.error('Error Message')
logger.critical('Critical Message')
```

## 出力結果

- コンソール

  ```plain
  INFO     2022/01/01 00:00:01; Info Message
  WARNING  2022/01/01 00:00:02; Warning Message
  ERROR    2022/01/01 00:00:03; Error Message
  CRITICAL 2022/01/01 00:00:04; Critical Message
  ```

- logs/app.log

  ```log
  INFO     2022/01/01 00:00:01 app.py::__main__::main::101; Info Message
  WARNING  2022/01/01 00:00:02 app.py::__main__::main::102; Warning Message
  ERROR    2022/01/01 00:00:03 app.py::__main__::main::103; Error Message
  CRITICAL 2022/01/01 00:00:04 app.py::__main__::main::104; Critical Message
  ```
