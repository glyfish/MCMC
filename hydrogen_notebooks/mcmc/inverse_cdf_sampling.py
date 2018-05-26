# %%
%load_ext autoreload
%autoreload 2

import numpy
import sympy

from matplotlib import pyplot
from scipy import stats
from glyfish import config

%matplotlib inline

pyplot.style.use(config.glyfish_style)

# %%
# Inverse CDF Descrete random variables


x = sympy.symbols('x')
sympy.Heaviside(0, 1)
steps = [sympy.Heaviside(x - i + 1, 1) for i in range(1, 7)]

steps[0]
steps[0].subs(x, 2)

cdf = sum(steps) / 6
cdf.subs(x, 3)

sympy.plot(cdf, (x, 0, 6), ylabel="CDF(x)", xlabel='x', ylim=(0, 1))

# %%
# The inverse of the heavyside distribution is given by
x = sympy.symbols('x')
intervals = [(1, sympy.Interval(0, 1 / 6, False, True).contains(x)),
             (2, sympy.Interval(1 / 6, 2 / 6, False, True).contains(x)),
             (3, sympy.Interval(2 / 6, 3 / 6, False, True).contains(x)),
             (4, sympy.Interval(3 / 6, 4 / 6, False, True).contains(x)),
             (5, sympy.Interval(4 / 6, 5 / 6, False, True).contains(x)),
             (6, sympy.Interval(5 / 6, 1, False, False).contains(x))]
inv_cdf = sympy.Piecewise(*intervals)
samples = [int(inv_cdf.subs(x, i)) for i in numpy.random.rand(10000)]
n, bins, _ = pyplot.hist(samples, bins=[1, 2, 3, 4, 5, 6, 7], density=True, align='left', rwidth=0.9, zorder=5, color="#336699", alpha=0.9)
pyplot.title("Simulated PDF")

# %%

sampled_cdf = numpy.cumsum(n)
cdf_values = [float(cdf.subs(x, i)) for i in range(0, 6)]

figure, axis = pyplot.subplots(figsize=(12, 5))
axis.set_xlabel("Sample")
axis.set_ylabel("Value")
axis.set_title("Simulated CDF")
axis.grid(True, zorder=5)
random_variable_values = [i + 0.2 for i in range(1, 7)]
axis.bar(random_variable_values, sampled_cdf, 0.4, color="#993333", label=f"Sampled CDF Estimate", alpha=0.6, lw="3", edgecolor="#993333", zorder=5)
random_variable_values = [i - 0.2 for i in range(1, 7)]
axis.bar(random_variable_values, cdf_values, 0.4, color="#336699", label=f"CDF", alpha=0.6, lw="3", edgecolor="#336699", zorder=6)
axis.legend()

# %%
# For the continuous distribution exp(x)

f_inv = lambda v: numpy.log(1.0 / (1.0 - v))
samples = [f_inv(v) for v in numpy.random.rand(10000)]

figure, axis = pyplot.subplots(figsize=(12, 5))
axis.set_xlabel("Sample")
axis.set_ylabel("PDF")
axis.set_title("Inverse Sampling")
axis.grid(True, zorder=5)
_, bins, _ = axis.hist(samples, 50, density=True, color="#336699", alpha=0.6, label=f"Sampled Density", edgecolor="#336699", lw="3", zorder=10)
sample_values = [numpy.exp(-v) for v in bins]
axis.plot(bins, sample_values, color="#A60628", label=f"Sampled Function", lw="3", zorder=10)
axis.legend()