# Graphing Calculator

Ok so this is a command-line calculator and polynomial grapher written in Python, and here's the cool part: basically ALL the math is done from scratch. No `math` module. Sine and cosine? Taylor series. Natural log? Series expansion. Pi? Leibniz series. The only thing imported is `matplotlib`, and that's just to actually draw the graphs, because I'm not writing a rendering engine in a terminal.

## What it does

- **Interactive CLI** with three modes: the main prompt, a `calc` mode for doing math, and a `graph` mode for plotting polynomials
- **Hand-rolled math**, as in:
  - sin and cos built from Taylor series
  - ln from a series expansion
  - polynomial evaluation using synthetic division (yes, the thing from algebra class, it's secretly Horner's method and it's awesome)
- **Actual calculus**: polynomial derivatives and Riemann sums
- **Variable storage**: save results to one-letter variables like a real TI calculator
- **Graphing**: plot any polynomial with custom labels, a title, and point-filtering conditions, saved as a PNG

## Getting started

You need Python 3 and matplotlib. That's literally it.

```bash
pip install matplotlib
python GraphingC.py
```

Heads up: when the program starts it prints two giant lists of Taylor series coefficients before the prompt appears. That's leftover test output at the bottom of `GraphMathModule.py`, not a crash. Just scroll past it, the `<<<` prompt is down there.

Type `options` at the main prompt to see what you can do.

## How polynomials work here

Polynomials go in as **lists with no spaces**, highest degree first. So the position in the list is the degree. Examples:

| Polynomial | List form |
|---|---|
| x^2 - 2 | `[1,0,-2]` |
| 3x^3 + x - 5 | `[3,0,1,-5]` |

## Commands

### Main prompt

| Command | What it does |
|---|---|
| `options` | Lists commands, or explains one with `options COMMAND` |
| `prev` | Lists your stored variables, or shows one with `prev VAR` |
| `calc` | Enter calc mode |
| `graph` | Enter graph mode |
| `credits` | Roll the credits |
| `exit` | Quit |

### Calc mode (`calc/<<<`)

These are the commands that work (see Known Issues for the ones that don't):

| Command | What it does |
|---|---|
| `synDiv B POLY RES` | Synthetic division of `POLY` by (x - `B`). `RES 1` gives the remainder, which by the Remainder Theorem is also `POLY` evaluated at `B`. `RES 0` gives the full synthetic division row, meaning the quotient coefficients with the remainder tacked on as the last element |
| `fac NUM` | Factorial |
| `tylrcos TERMS` | Taylor polynomial for cosine with `TERMS` terms, returned in list form |
| `tylrsin TERMS` | Same but for sine |
| `polyDeriv POLY` | Takes the derivative of `POLY` |
| `rieSum LB UB POLY DX` | Left Riemann sum of `POLY` from `LB` to `UB` with step size `DX`. Note the lowercase r: the in-app options list spells it `RieSum` but the command only works as `rieSum` |
| `ln NUM TERMS` | Natural log of `NUM` approximated with `TERMS` terms. Takes 2 parameters even though the in-app help claims 1 |
| `storemode BOOL` | Turn on with `True` and every result asks for a one-letter variable name and gets stored instead of printed (but see Known Issues about recalling them) |
| `delete VAR` | Deletes a stored variable |
| `exit` | Back to the main prompt |

Bonus: anything else you type in calc mode just gets evaluated as regular arithmetic, so `2+2*10` gives you `22`.

### Graph mode

Graph mode walks you through some prompts:

1. **Interval for dx**: spacing between plotted points (smaller = smoother)
2. **Span of graph**: how far along the x-axis to go. Points are plotted from x = dx up to x = span, so positive x values only
3. **Number of ticks on the x-axis**: asked for, but not currently applied to the plot
4. **Graphed polynomial**: in list form (see above)
5. **Filename**: your graph gets saved as a PNG in the current folder
6. **Axis labels and title**
7. **Graph condition(s)**: a filter written in terms of `x` and `y`, like `y > 0`, so only matching points get plotted. This one is NOT optional. Leaving it blank throws a syntax error, so if you just want the whole graph, type something always true like `1==1`

Graphing only handles polynomials (so no vertical asymptotes, sorry rational functions).

## Known issues

Being honest with you, a few things listed in the in-app options don't currently work:

- `lim` errors out when used in its documented format, and passing `inf` or `-inf` crashes the program
- `arccos`, `e`, and `pi` show up in the calc options list but have no command wired up, so they just give an OptionError
- `options COMMAND` inside calc mode crashes for calc-only commands like `options synDiv` (it works fine at the main prompt)
- Storing variables with `storemode` works, but recalling a stored function result by typing its name can crash the program. Stored plain-arithmetic results recall fine
- The startup coefficient dump mentioned in Getting Started

## Project structure

| File | What's in it |
|---|---|
| `GraphingC.py` | The interactive command-line interface |
| `GraphMathModule.py` | The math library: synthetic division, series expansions, derivatives, limits, Riemann sums |

## License

GPL-3.0. See [LICENSE](LICENSE) for the full legal saga.
