# Python - random module

* It's used to
  * generate random data
  * shuffle data
  * choose data randomly, etc
  * mostly used in statistics/probability

## Frequently used functions

| Function                              | Description                                                           | Example                              |
| ------------------------------------- | --------------------------------------------------------------------- | ------------------------------------ |
| *randint(lower_limit, upper_limit)* | Generates random integer between lower and upper limits               | random.randint(5, 15)                |
| *random()*                          | Generates a floating point number between 0 and 1                     | random.random()                      |
| *choice(sequence)*                  | Returns a random element from the sequence                            | random.choice([1,2,3,4,5])           |
| shuffle(list)                         | Takes a list as an input and shuffles the list [i.e updates the list] | l = [1,2,3,4]<br />random.shuffle(l) |

## Other functions

| Function                        | Description                                                                                                                                                                                                                                         | Example                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| *seed(value)*                 | same random numer sequence is generated for given seed value                                                                                                                                                                                        | random.seed(10)               |
| *uniform(a, b)*               | generate a random floating-point number N such that a <= N <= b                                                                                                                                                                                     | random.uniform(1, 10)         |
| *expovariate(lambd)*          | generates a random floating-point number following<br /> an exponential distribution with lambda                                                                                                                                                    | random.expovariate(0.5)       |
| *gammavariate(alpha, beta)*   | generate floating random numbers with gamma distribution                                                                                                                                                                                            | random.gammavariate(2, 2)     |
| *gauss(mu, sigma)*            | generate floating random numbers with a gaussian distribution                                                                                                                                                                                       | random.gauss(0, 1)            |
| *lognormvariate(mu, sigma)*   | generate random floating numbers with a log-normal distribution                                                                                                                                                                                     | random.lognormvariate(1, 2)   |
| *normalvariate(mu, sigma)*    | generate random floating numbers with normal distribution                                                                                                                                                                                           | random.normalvariate(0, 1)    |
| *paretovariate(alpha)*        | generate random floating numbers with Pareto distribution                                                                                                                                                                                           | random.paretovariate(2)       |
| *sample(population, k)*       | generate a random sample of elements from a population<br /> without replacement.                                                                                                                                                                   | random.sample([1,2,3,4,5], 3) |
| *triangular(low, high, mode)* | The triangular distribution is a continuous probability distribution<br /> with a lower limit `low`, an upper limit `high`, and a mode `mode` which represents the peak of the distribution.<br /> Values are more likely to be near the mode | random.triangular(0, 100, 50) |

### References:

* https://docs.python.org/3/library/random.html


.
