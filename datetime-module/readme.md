# 🧑‍💻 python3 - `datetime` module

![](https://documents.lucid.app/documents/34a41359-6770-45fe-b0e4-1924ad357d21/pages/0_0?a=336&x=147&y=-142&w=705&h=463&store=1&accept=image%2F*&auth=LCA%20b76cdedd508c0beda04d8be71280904b54750facc3ef55fc22196272284d95d3-ts%3D1708148949)

## `date` & `time` - classes

```python
from datetime import date, time

d = date(2023, 1, 23)
print(d)
t = time(4, 23, 55)
print(t)
```

* `date` - class methods
  * `date + timedelta()`  - add/subtract time delta to date
  * `strftime()` - format date to string
  * `today()` - returns current local date
  * `replace()` - replace attributes like day, month, year
* `time` - class methods
  * `now` - get current time
  * `replace` - replace attributes like `hour`, `minutes`, `seconds`, `micro seconds` and `timezone`
  * `strftime()` - format time

## `datetime` class

```python
from datetime import datetime, timezone

dt = datetime(
 2022, month=11, day=1,
 hour=23, minute=10, second=58, microsecond=100,
 tzinfo=None
)
# print attributes
print(dt.year)
```

* methods
  * `now()` - current datetime object
  * `utcnow()` - current UTC date and time
  * `strptime()` - format datetime object to string
  * `strftime()` - format string to datetime object
  * `combine()` - create datetime object from date and time objects
  * `timestamp()` - returns unix timestamp
    * Unix time is a date and time representation widely used in computing. It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970, the Unix epoch.
  * `fromtimestamp()` - returns local datetime object
  * `utcfromtimestamp()` - returns UTC datetime object
  * `astimezone()` - returns datetime object with new timezone

## strftime & strptime methods

```python
from datetime import datetime
# use strftime
now = datetime.now()
result = now.strftime("%Y-%m-%d %H:%M:%S")
print(result)
print(type(result))
# use strptime
date_str = "2020-01-05 11:44:33"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt)
print(type(dt))
```

## formatting directives

| Directive | Meaning                                                       | Example                      |
| --------- | ------------------------------------------------------------- | ---------------------------- |
| `%Y`    | Year with century as a decimal number                         | `2022`                     |
| `%m`    | Month as a zero-padded decimal number                         | `01`(January)              |
| `%d`    | Day of the month as a zero-padded decimal number              | `05`                       |
| `%H`    | Hour (00-23)                                                  | `14`                       |
| `%M`    | Minute (00-59)                                                | `30`                       |
| `%S`    | Second (00-59)                                                | `45`                       |
| `%A`    | Full weekday name                                             | `Monday`                   |
| `%a`    | Abbreviated weekday name                                      | `Mon`                      |
| `%B`    | Full month name                                               | `January`                  |
| `%b`    | Abbreviated month name                                        | `Jan`                      |
| `%p`    | Locale’s equivalent of either AM or PM.                      |                              |
| `%c`    | Locale's date and time representation                         | `Mon Jan 10 14:30:45 2022` |
| `%x`    | Locale's date representation                                  | `01/10/22`                 |
| `%X`    | Locale's time representation                                  | `14:30:45`                 |
| `%j`    | Day of the year as a zero-padded decimal number               | `010`                      |
| `%U`    | Week number of the year (Sunday as the first day of the week) | `02`                       |
| `%W`    | Week number of the year (Monday as the first day of the week) | `02`                       |
| `%Z`    | Time zone name or abbreviation                                | `UTC`,`EST`,`PST`      |
| `%%`    | Literal `%`                                                 | `%`                        |

## `timedelta` class

```python
from datetime import timedelta

td = timedelta(
  days=0,
  seconds=0,
  microseconds=0,
  milliseconds=0,
  minutes=0,
  hours=0,
  weeks=0
)
```

* `days`: Number of days, can be positive or negative.
* `seconds`: Number of seconds, can be positive or negative.
* `microseconds`: Number of microseconds, can be positive or negative.
* `milliseconds`: Number of milliseconds, equivalent to `seconds * 1000`.
* `minutes`: Number of minutes, can be positive or negative.
* `hours`: Number of hours, can be positive or negative.
* `weeks`: Number of weeks, can be positive or negative.
* `total_seconds()` : Returns the total number of seconds in the duration.

## problems

1. convert below date strings to datetime objects
   1. `2022-03-20`
   2. `12/31/2024 11:44am`
   3. `Mon Jan 10 14:30:45 2022`
   4. `2022-06-30T21:00:00.000Z`
2. find the time difference between  `2020-01-02 11:33pm` and `2021-01-02 11:33am`
3. covert current datetime to `UTC`, `IST` and `PST` [i.e `UTC - 8`]
