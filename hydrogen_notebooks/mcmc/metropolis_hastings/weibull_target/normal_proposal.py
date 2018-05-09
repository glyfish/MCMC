# %%

import numpy
from matplotlib import pyplot
from scipy import stats
from glyfish import config
from glyfish import metropolis_hastings as mh

%matplotlib inline

pyplot.style.use(config.glyfish_style)

#%%
target_pdf = mh.weibull(5.0)
x = numpy.linspace(0.001, 10.0, 200)
figure, axis = pyplot.subplots(figsize=(12, 5))
axis.set_xlabel("X")
axis.set_ylabel("PDF")
axis.set_xlim([0.0, 1.0])
axis.set_title(f"Weibull Distribution")
axis.plot(x, [mh.arcsine(j) for j in x])

#%%

nsample=100000
stepsize = 1.0
samples, accepted = metropolis_hastings.metropolis_hastings(pdf, mh.normal_proposal, mh.normal_generator, stepsize, nsample=nsample, x0=0.001)
accepted_percent = 100.0*float(accepted)/float(nsample)

#%%

figure, axis = pyplot.subplots(figsize=(12, 5))
axis.set_xlabel("X")
axis.set_ylabel("PDF")
axis.set_title(f"Weibull Distribution, Normal Proposal, Accepted {format(accepted_percent, '2.0f')}%")
_, bins, _ = axis.hist(samples, 50, density=True, color="#336699", alpha=0.6, label=f"Sampled Distribution", edgecolor="#336699", zorder=5)
delta = (bins[-1] - bins[0]) / 200.0
sample_distribution = [pdf(val) for val in numpy.arange(bins[0], bins[-1], delta)]
axis.plot(numpy.arange(bins[0], bins[-1], delta), sample_distribution, color="#A60628", label=f"Sampled Function", zorder=6)
axis.legend()

# %%

start = 5000
end = 5500

figure, axis = pyplot.subplots(figsize=(12, 5))
axis.set_xlabel("Time")
axis.set_ylabel("X")
axis.set_xlim([start, end])
axis.set_title(f"Wiebull Timeseries, Accepted {format(accepted_percent, '2.0f')}%")
axis.plot(time[start:end], samples[start:end], lw="1")