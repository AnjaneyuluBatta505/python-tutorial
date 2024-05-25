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
