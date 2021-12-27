# Monty Hall Problem ([Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem))

This repo is meant as a demo of [Numba](https://numba.pydata.org/) and to compare speeds of a vanilla implementation of
a problem simulation vs the numba JIT-compiled implementation.

## Logic
1. Contestant chooses one of three doors
2. Host opens one door with a goat
3. Contestant chooses either to stay or to switch (-> new choice of the two remaining doors)
4. Win or Lose

In this simulation, both the contestant and host roles are done by code.
The aim is to see if switching doors on step 3 leads to more wins than staying with the original door choice.
Running this simulation shows that indeed, switching leads to ~ 2x more wins.

## Speeds

### 100.000 runs

- Python: ~ 0.3 seconds for each 1M
- Numba: ~ 1.5 seconds BUT only 0.08 on the next 100k. This shows that it takes some time for the compilation to
  complete, but the compiled code is much faster.
- Numpy[^*]: ~ 2.8 seconds for each 1M

### 1.000.000 runs of the simulation

- Python: ~ 3.1 seconds for each 1M
- Numba: ~ 2.4 seconds BUT only 0.86 on the next million. So numba is most efficient when working with lots of data or
  doing many runs, since it takes a while for this initial cost of compilation to "pay off" in increased code speed.
- Numpy[^*]: ~ 29.2 seconds for each 1M

### 10.000.000 runs:

- Python: ~ 31.5 seconds for each 10M
- Numba: ~ 9.6 seconds and 8.3 on the next 10M
- Numpy[^*]: (not even trying this)

[^*]: Since I am not very at home in Numpy, perhaps my implementation is very inefficient.
