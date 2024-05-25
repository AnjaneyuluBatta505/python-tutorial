# Python - logging module

* Logging is essential to understand the behaviour of the application
* Logging helps in debugging the unexpected issues or for simply tracking events.
* Logs can used to get insights, set monitoring alerts, etc.


## logging levels

* **Critical** - used when error occured but execution can't be continued
* **Error** - used when error occured but execution can be continued
* **Warning** - used when something unexpected happened in the application, a problem, or a situation that might disturb one of the processes.
* **Info** - used to when debugging the app with less details
* **Debug** - used to when debug the app with specific details.

## logging module

* built-in module to handle the logging.
* it can be extended to write custom loggers based on the dev needs.

Example:

```python
import logging

# config logging
logger = logging.getLogger(name='mylogger')
logging.basicConfig(level=logging.DEBUG)

def calculate_simple_interest(p, t, r):
    logger.info(f'principal={p} time={t} rate of interest={r}')
    amount = p * (1 + r * t)
    return amount

if __name__ == '__main__':
    interest = calculate_simple_interest(1000, 12, 0.2)
```

## log handlers

* Handlers are used to direct log messages to various outputs or destinations.
* Logger can have multiple handlers, and each handler can have different logging levels.
* When a log event occurs, the logger sends the event to all of its handlers.

    * Lets assume logger has two handlers 1. FileHandler 2. StreamHandler
    * If log event occurs then it will be sent and processed by the attached two handlers. Such as being written to a file and displayed on the console simultaneously.
 
Example: 

```python
import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('test.log')
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.info('information message')
```

## logging config

* It does basic configuration for the logging system by creating a stream handler with a default formatter.
* The debug, info, warning, error and critical call basicConfig automatically if no handlers are defined for the root logger.

```python
import logging

logging.basicConfig(
    filename='/tmp/test.log',
    format='%(filename)s: %(message)s',
    level=logging.DEBUG
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```
