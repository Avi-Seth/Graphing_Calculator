# Graphing Calculator

Ok so this is a command-line calculator and polynomial grapher written in Python, and here's the cool part: basically ALL the math is done from scratch. No `math` module. Sine and cosine? Taylor series. Natural log? Series expansion. Pi? Leibniz series. e? Its own series. The only thing imported is `matplotlib`, and that's just to actually draw the graphs, because I'm not writing a rendering engine in a terminal.

## What it does

- **Interactive CLI** with three modes: the main prompt, a `calc` mode for doing math, and a `graph` mode for plotting polynomials
- **Hand-rolled math**, as in:
  - sin, cos, and arccos built from Taylor series
  - ln from a series expansion, e from its series, pi from the Leibniz series
  - polynomial evaluation using synthetic division (yes, the thing from algebra class, it's secretly Horner's method and it's awesome)
- **Actual calculus**: polynomial derivatives, limits of rational functions (one-sided limits, limits at infinity, and 0/0 forms via L'Hopital's rule), and Riemann sums
- **Variable storage**: save results to one-letter variables like a real TI calculator, recall them, use them in expressions, delete them
- **Graphing**: plot any polynomial with custom labels, a title, and optional point-filtering conditions, saved as a PNG

## Getting started

You need Python 3 and matplotlib. That's literally it.

```bash
pip install matplotlib
python GraphingC.py
```

Type `options` at any prompt to see what you can do, or `options COMMAND` for details on a specific command.

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

| Command | What it does |
|---|---|
| `synDiv B POLY RES` | Synthetic division of `POLY` by (x - `B`). `RES 1` gives the remainder, which by the Remainder Theorem is also `POLY` evaluated at `B`. `RES 0` gives the full synthetic division row, meaning the quotient coefficients with the remainder tacked on as the last element |
| `fac NUM` | Factorial |
| `tylrcos TERMS` | Taylor polynomial for cosine with `TERMS` terms, in list form |
| `tylrsin TERMS` | Same but for sine |
| `arccos TERMS` | Taylor polynomial for arccosine (accurate for \|x\| < 1) |
| `polyDeriv POLY` | Takes the derivative of `POLY` |
| `lim VAL POLY1 POLY2 DIRECTION` | Limit of `POLY1`/`POLY2` as x approaches `VAL` (a number, `inf`, or `-inf`) from the `left` or `right`. Handles ordinary limits, one-sided infinities, limits at infinity, and 0/0 forms via L'Hopital |
| `rieSum LB UB POLY DX` | Left Riemann sum of `POLY` from `LB` to `UB` with step size `DX` |
| `ln NUM TERMS` | Natural log of `NUM` approximated with `TERMS` terms |
| `e TERMS` | Approximates e with `TERMS` series terms |
| `pi TERMS` | Approximates pi with `TERMS` Leibniz terms (bring lots of terms, it converges slowly) |
| `storemode BOOL` | Turn on with `True` and every result asks for a one-letter variable name and gets stored instead of printed. Recall by typing the name, or use it in expressions like `q+s` |
| `delete VAR` | Deletes a stored variable |
| `exit` | Back to the main prompt |

Bonus: anything else you type in calc mode just gets evaluated as regular arithmetic, so `2+2*10` gives you `22`.

### Graph mode

Graph mode walks you through some prompts:

1. **Interval for dx**: spacing between plotted points (smaller = smoother)
2. **Span of graph**: how far along the x-axis to go. Points are plotted from x = dx up to x = span, so positive x values only
3. **Number of ticks on the x-axis**
4. **Graphed polynomial**: in list form (see above)
5. **Filename**: your graph gets saved as a PNG in the current folder
6. **Axis labels and title**
7. **Graph condition(s)**: an optional filter written in terms of `x` and `y`, like `y > 0`, so only matching points get plotted. Leave it blank to plot everything

Graphing only handles polynomials (so no vertical asymptotes, sorry rational functions).

## Bug fix remarks (July 2026)

This code got a full audit and bug-fixing pass. Seven bugs were found and fixed, including a broken `lim` command, unwired `arccos`/`e`/`pi` handlers, a crash when recalling stored variables, and test prints that flooded the screen on startup. Every fix is documented in a REMARKS block at the top of each source file, and the original code is preserved in `# OLD:` comments right where each fix happened, so you can see exactly what changed and why. Nothing was silently deleted.

## Project structure

| File | What's in it |
|---|---|
| `GraphingC.py` | The interactive command-line interface |
| `GraphMathModule.py` | The math library: synthetic division, series expansions, derivatives, limits, Riemann sums |

## License

GPL-3.0. See [LICENSE](LICENSE) for the full legal saga.
