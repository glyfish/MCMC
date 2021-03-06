# %%
%load_ext autoreload
%autoreload 2

import numpy

from matplotlib import pyplot
from glyfish import config
from glyfish import stats

%matplotlib inline

pyplot.style.use(config.glyfish_style)

# %%

def discrete_mean(p):
    x = numpy.arange(len(p))
    return numpy.sum(x*p)

def discrete_sigma(p):
    mean = discrete_mean(p)
    x = numpy.arange(len(p))
    return numpy.sqrt(numpy.sum(p*x**2) - mean**2)

# %%
# Inverse CDF Descrete random variable

df = numpy.array([1/12, 1/12, 1/6, 1/6, 1/12, 5/12])
cdf = numpy.cumsum(df)
x = numpy.array(range(len(df))) + 1

nsamples = 100000
df_samples = [numpy.flatnonzero(cdf >= cdf_star)[0] for cdf_star in numpy.random.rand(nsamples)]
multinomial_samples = numpy.random.multinomial(nsamples, df, size=1)/nsamples

# %%

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylim([0, 1.1])
axis.set_xlabel(r"$n$")
axis.set_title("Discrete Distribution")
axis.set_prop_cycle(config.bar_plot_cycler)
axis.bar(x - 0.2, df, 0.4, label=f"Distribution", zorder=5)
axis.bar(x + 0.2, cdf, 0.4, label=f"CDF", zorder=5)
axis.legend(bbox_to_anchor=(0.3, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "discrete_cdf")

# %%

bins = numpy.array([-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
hist, _ = numpy.histogram(df_samples, bins)
p = hist/numpy.sum(hist)

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylim([0, 0.5])
axis.set_xlabel(r"$n$")
axis.set_ylabel("Probability")
axis.set_prop_cycle(config.bar_plot_cycler)
axis.set_title("Sampled Discrete Distribution")
axis.bar(x - 0.2, df, 0.4, label=f"Target Distribution", zorder=5)
axis.bar(x + 0.2, p, 0.4, label=f"Samples", zorder=5)
axis.legend(bbox_to_anchor=(0.4, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "discrete_sampled_distribution")

# %%

μ = discrete_mean(df)
title = f"Sampled Discrete Distribution μ Convergence"
x = range(nsamples)

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_xlabel("Sample Number")
axis.set_ylabel("μ")
axis.set_title(title)
axis.set_xlim([1.0, nsamples])
axis.set_ylim([0.0, 6.0])
axis.set_yticks([1.0, 2.0, 3.0, 4.0, 5.0])
axis.semilogx(x, numpy.full(nsamples, μ), label="Target μ")
axis.semilogx(x, stats.cummean(df_samples), label="Sampled μ")
axis.legend(bbox_to_anchor=(1.0, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "discrete_sampled_mean_convergence")

# %%

σ = discrete_sigma(df)
title = f"Sampled Discrete Distribution σ Convergence"
x = range(nsamples)

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_xlabel("Sample Number")
axis.set_ylabel("σ")
axis.set_title(title)
axis.set_xlim([1.0, nsamples])
axis.set_ylim([0.0, 3.0])
axis.set_yticks([0.5, 1.0, 1.5, 2.0, 2.5])
axis.semilogx(x, numpy.full(nsamples, σ), label="Target σ")
axis.semilogx(x, stats.cumsigma(df_samples), label="Sampled σ")
axis.legend(bbox_to_anchor=(1.0, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "discrete_sampled_sigma_convergence")

# %%
# Inverse CDF sampling for exponential

nsamples = 100000
cdf_inv = lambda v: numpy.log(1.0 / (1.0 - v))
pdf = lambda v: numpy.exp(-v)

samples = [cdf_inv(u) for u in numpy.random.rand(nsamples)]
x = numpy.linspace(0.0, 6.0, 500)
dx = 6.0/499.0

# %%

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylim([0, 1.1])
axis.set_yticks([0.1, 0.3, 0.5, 0.7, 0.9])
axis.set_xlabel(r"$X$")
axis.set_title("Exponential Distribution")
axis.plot(x, pdf(x), label="PDF", zorder=5)
axis.plot(x, dx*numpy.cumsum(pdf(x)), label="CDF", zorder=5)
axis.legend(bbox_to_anchor=(0.9, 0.6))
config.save_post_asset(figure, "inverse_cdf_sampling", "exponential_cdf")


# %%

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylabel("PDF")
axis.set_xlim([0.0, 6.0])
axis.set_yticks([0.1, 0.3, 0.5, 0.7, 0.9])
axis.set_xlabel(r"$X$")
axis.set_title("Sampled Exponential Distribution")
axis.set_prop_cycle(config.distribution_sample_cycler)
axis.hist(samples, 60, density=True, rwidth=0.8, label=f"Samples", zorder=5)
axis.plot(x, pdf(x), label=f"Target PDF", zorder=6, color="#003B6F")
axis.legend(bbox_to_anchor=(0.9, 0.8))
config.save_post_asset(figure, "inverse_cdf_sampling", "exponetial_sampled_distribution")


# %%
# Inverse CDF sampling from weibull distribution

k = 5.0
λ = 1.0
nsamples = 100000
pdf = stats.weibull(k, λ)
cdf_inv = lambda u: λ * (numpy.log(1.0/(1.0 - u)))**(1.0/k)
x = numpy.linspace(0.001, 1.6, 500)
dx = 1.6/499.0

samples = [cdf_inv(u) for u in numpy.random.rand(nsamples)]

# %%

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylim([0, 2.0])
axis.set_xlabel(r"$X$")
axis.set_xlim([0.0, 1.6])
axis.set_yticks([0.2, 0.6, 1.0, 1.4, 1.8])
axis.set_title(f"Weibull Distribution, k={k}, λ={λ}")
pdf_values = [pdf(v) for v in x]
axis.plot(x, pdf_values, label="PDF", zorder=5)
axis.plot(x, dx*numpy.cumsum(pdf_values), label="CDF", zorder=5)
axis.legend(bbox_to_anchor=(0.3, 0.8))
config.save_post_asset(figure, "inverse_cdf_sampling", "weibull_cdf")

# %%

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_ylabel("PDF")
axis.set_ylim([0, 2.0])
axis.set_xlabel(r"$X$")
axis.set_yticks([0.2, 0.6, 1.0, 1.4, 1.8])
axis.set_xlim([0.0, 1.6])
axis.set_title(f"Sampled Weibull Distribution, k={k}, λ={λ}")
axis.set_prop_cycle(config.distribution_sample_cycler)
axis.hist(samples, 30, density=True, rwidth=0.8, label=f"Samples", zorder=5)
axis.plot(x, pdf_values, label=f"Target PDF", zorder=6)
pdf_values = [pdf(u) for u in x]
axis.legend(bbox_to_anchor=(0.35, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "weibull_sampled_distribution")


# %%

μ = stats.weibull_mean(k, λ)
title = f"Weibull Sampled Distribution μ Convergence, k={k}, λ={λ}"
x = range(nsamples)

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_xlabel("Sample Number")
axis.set_ylabel("μ")
axis.set_title(title)
axis.set_xlim([1.0, nsamples])
axis.set_ylim([0.5, 1.5])
axis.semilogx(x, numpy.full(nsamples, μ), label="Target μ")
axis.semilogx(x, stats.cummean(samples), label="Sampled μ")
axis.legend(bbox_to_anchor=(1.0, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "weibull_sampled_mean_convergence")


# %%

σ = stats.weibull_sigma(k, λ)
title = f"Weibull Sampled Distribution σ Convergence, k={k}, λ={λ}"
c = range(nsamples)

figure, axis = pyplot.subplots(figsize=(10, 6))
axis.set_xlabel("Sample Number")
axis.set_ylabel("σ")
axis.set_title(title)
axis.set_xlim([1.0, nsamples])
axis.set_ylim([0.0, 0.5])
axis.set_yticks([0.1, 0.2, 0.3, 0.4])
axis.semilogx(x, numpy.full(nsamples, σ), label="Target σ")
axis.semilogx(x, stats.cumsigma(samples), label=r"Sampled σ")
axis.legend(bbox_to_anchor=(1.0, 0.85))
config.save_post_asset(figure, "inverse_cdf_sampling", "weibull_sampled_std_convergence")
