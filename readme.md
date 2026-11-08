# Graphing Calculator

A command-line calculator and polynomial grapher written in Python, done from scratch without any math libraries. `matplotlib` is used for Graphing. Type `options` into the prompt to get a list of more things to do, and type `options [option]` to access the purpose of an option.

## Contributions and AI use

I wrote all the code in this repository (GraphingC.py and GraphMathModule.py) myself, without AI assistance. This README was drafted with help from Claude Opus (Anthropic)] and edited by me.

## What it does

- **Interactive CLI** with three modes: the main prompt, `calc` mode for doing math, and `graph` mode for plotting polynomials
- sin and cos built from Taylor series
- ln from a series expansion
- Polynomial evaluation using synthetic division (yes, the thing from algebra class, it's secretly Horner's method and it's awesome)
- Permits Polynomial derivatives and Riemann sums
- **Variable storage**: Allows storing variables like a real TI calculator
- **Graphing**: Plot polynomial with custom labels, title, and point-filtering conditions, saved as PNG

Additionally, the python shell can be used normally when the program is running, since it runs the code by using the exec() command.


```bash
pip install matplotlib
python GraphingC.py
```

When the program starts it prints two giant lists of Taylor series coefficients before the prompt appears. Leftover output from `GraphMathModule.py`, not a crash. Just scroll past it, the `<<<` prompt is down there.

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

Graph mode uses the following inputs to get the output graph:

1. **Interval for dx**: spacing between plotted points (smaller = smoother)
2. **Span of graph**: how far along the x-axis to go. Points are plotted from x = dx up to x = span
3. **Number of ticks on the x-axis**: asked for, but not currently applied to the plot
4. **Graphed polynomial**: in list form (see above)
5. **Filename**: your graph gets saved as a PNG in the current folder
6. **Axis labels and title**
7. **Graph condition(s)**: a filter written in terms of `x` and `y`, like `y > 0`, so only matching points get plotted. This one is NOT optional. Leaving it blank throws a syntax error, so if you just want the whole graph, type something always true like `1==1`

Graphing only handles polynomials (no vertical asymptotes).

## Known issues

A few things listed in the in-app options don't currently work. The causes below were found when reviewing the 2023 code later. Line numbers refer to the files in this repo.

- `lim` errors out when used in its documented format, and passing `inf` or `-inf` crashes the program
  - `GraphingC.py` line 222 passes the inputs in the order they're typed (`VAL POLY1 POLY2`), but `lim()` is defined as `lim(poly1, poly2, app, dr)` (`GraphMathModule.py` line 70). So `poly1` gets a number, and `len(poly1)` on line 75 fails
  - `eval('inf')` on line 222 raises a `NameError`. The `except` lines (231-238) don't catch `NameError`, so the whole program stops
  - Even with the inputs in the right order, `lim()` gets most answers wrong. Line 75 checks `(app == 'inf' or '-inf')`, which is always true because a non-empty string counts as true, so it returns 0 even at ordinary points (x/x^2 as x approaches 3 gives 0, not 1/3). Lines 81-91 return plus or minus infinity whenever the denominator is 0, without checking whether the numerator is also 0 ((x^2-4)/(x-2) as x approaches 2 gives `-inf`, not 4). Lines 92-95 take derivatives until both polynomials are constants, which isn't how L'Hôpital's rule works and can end in a division by zero
- `arccos`, `e`, and `pi` show up in the calc options list but have no command wired up, so they just give an OptionError
  - There's no `elif` for them in calc mode, so they fall through to the arithmetic fallback (lines 291-302). The `e()` and `pi()` functions in `GraphMathModule.py` do work; nothing calls them. (`pi()` uses the Leibniz series, which converges slowly)
  - `arccos()` itself (`GraphMathModule.py` lines 51-56) has three bugs: it never returns anything, line 55 uses `0.5**i` where the series needs (1/2)(3/2)(5/2)... so every term from x^5 on is wrong, and the constant term pi/2 is missing
- `options COMMAND` inside calc mode crashes for calc-only commands like `options synDiv` (it works fine at the main prompt)
  - Line 77 looks the command up in the main prompt's list (`options1.index`) instead of `optionscalc`. Calc-only commands aren't in that list, so it raises a `ValueError`, and `options exit` in calc mode shows synDiv's help instead
  - The help list `descalc` (lines 20-31) has 11 entries for 16 commands. There's no help for `arccos`, `ln`, `e` or `pi`, and a missing comma at the end of line 28 makes Python join the `polyDeriv` and `lim` help into one string. So fixing line 77 alone would still show the wrong help from `arccos` onward
- Storing variables with `storemode` works, but recalling a stored function result by typing its name can crash the program. Stored plain-arithmetic results recall fine
  - Each result is saved as a text recipe that line 70 runs with `eval()` on recall, and most recipes are broken. They call `function.` but the module is imported as `mathfunction` (line 2), the `fac` recipe has no module name at all, the `rieSum` recipe (line 251) is missing a closing bracket, and the `ln` recipe (line 276) re-reads `prompt`, which by then holds the new input. A recipe like `2+2` is valid Python, which is why arithmetic recalls fine
- The startup coefficient dump mentioned above
  - The test `print` lines at the bottom of `GraphMathModule.py` (lines 124-126) run every time `GraphingC.py` imports the module (line 2). Wrapping them in `if __name__ == "__main__":` would stop it

### Other bugs found later

- `ln` returns 0 for small inputs like `ln 0.05 10`, because its loop (`GraphMathModule.py` line 106) runs `int(TERMS*NUM)` times, which rounds down to 0. `ln -1 10` crashes with a division by zero on line 105
- `rieSum` with a `DX` of 0 (`GraphMathModule.py` line 99), or graph mode with a dx of 0 (`GraphingC.py` lines 346-347), crashes with a division by zero
- Graphing twice in one session draws the earlier curve onto the new image too, because the plot is never cleared between graphs (line 354)
- After `delete a`, typing `a` still prints the old value. Lines 104-105 remove the name from the stored lists but not the Python variable `exec()` created, so the arithmetic fallback still finds it
- A stored variable named `i`, `p` or `r` can be overwritten or lost, because graph mode uses `p` (line 321) and `i` (line 338), and `delete` uses `r` (line 104)


## Project structure

| File | What's in it |
|---|---|
| `GraphingC.py` | The interactive command-line interface |
| `GraphMathModule.py` | The math library: synthetic division, series expansions, derivatives, limits, Riemann sums |

## License

GPL-3.0. See [LICENSE](LICENSE) for the full legal saga.
