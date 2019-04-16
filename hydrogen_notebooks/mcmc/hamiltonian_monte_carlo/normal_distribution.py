%load_ext autoreload
%autoreload 2

import numpy
from matplotlib import pyplot
from glyfish import config
from glyfish import gplot
from glyfish import hamiltonian_monte_carlo as hmc

%matplotlib inline

pyplot.style.use(config.glyfish_style)

# %%
# Momentum Verlet integration of Hamiltons's equations used by HMC algorithm

def momentum_verlet_hmc(p0, q0, dUdq, dKdp, nsteps, ε):
    p = p0
    q = q0
    ΔU = dUdq(q)

    for _ in range(nsteps):
        p = p - ε*ΔU/2.0
        q = q + ε*dKdp(p)
        ΔU = dUdq(q)
        p = p - ε*ΔU/2.0

    return p, q

# Hamiltonian Monte Carlo

def HMC(q0, mass, U, K, dUdq, dKdp, integrator, nsample, nsteps, ε):
    current_q = q0
    H = numpy.zeros(nsample)
    qall = numpy.zeros(nsample)
    pall = numpy.zeros(nsample)
    accepted = 0

    for j in range(nsample):

        q = current_q

        # generate momentum sample
        current_p = numpy.random.normal(0.0, numpy.sqrt(mass))

        # integrate hamiltons equations using current_p and current_q to obtain proposal samples p and q
        # and negate p for detailed balance
        p, q = integrator(current_p, current_q, dUdq, dKdp, nsteps, ε)
        p = -p

        # compute acceptance probability
        current_U = U(current_q)
        current_K = K(current_p)
        proposed_U = U(q)
        proposed_K = K(p)
        α = numpy.exp(current_U-proposed_U+current_K-proposed_K)

        # accept or reject proposal
        accept = numpy.random.rand()
        if accept < α:
            current_q = q
            qall[j] = q
            pall[j] = p
            accepted += 1
        else:
            qall[j] = current_q
            pall[j] = current_p

        H[j] = U(current_q) + K(current_p)

    return H, pall, qall, accepted

# %%
# Here Hamiltonian Monte Carlo is used to generate samples for single variable
# Unit Normal distribution. The Potential and Kinetic Energy are given by assuming a mass of 1

def potential_energy(σ):
    def f(q):
        return q**2/(2.0 * σ**2)
    return f

def kinetic_energy(mass):
    def f(p):
        return p**2/(2.0 * mass)
    return f

def dUdq(σ):
    def f(q):
        return q/σ**2
    return f

def dKdp(mass):
    def f(p):
        return p/mass
    return f

def target_pdf(σ):
    u = potential_energy(σ)
    def f(q):
        return numpy.exp(-u(q))/numpy.sqrt(2.0*numpy.pi*σ**2.0)
    return f

def momentum_pdf(mass):
    k = kinetic_energy(mass)
    def f(p):
        return numpy.exp(-k(p))/numpy.sqrt(2.0*numpy.pi*mass)
    return f

def pdf_gridded(pdf, xrange, yrange, npts):
    x = numpy.linspace(xrange[0], xrange[1], npts)
    y = numpy.linspace(yrange[0], yrange[1], npts)

    x_grid, y_grid = numpy.meshgrid(x, y)
    f = numpy.zeros((npts, npts))
    for i in numpy.arange(npts):
        for j in numpy.arange(npts):
            f[i, j] = pdf(x_grid[i,j], y_grid[i,j])

    dx = (xrange[1] - xrange[0])/npts
    dy = (yrange[1] - yrange[0])/npts

    return f/(dx*dy*numpy.sum(f)), x_grid, y_grid

# %%

σ = 1.0
mass = 1.0

t = 5.0
ε = 0.1
nsteps = int(t/ε)
nsample = 10000
q0 = 1.0

# %%

pdf = target_pdf(σ)
x = numpy.linspace(-3.0*σ, 3.0*σ, 500)
figure, axis = pyplot.subplots(figsize=(10, 7))
axis.set_xlabel("q")
axis.set_ylabel("PDF")
axis.set_xlim([x[0], x[-1]])
axis.set_title(f"Normal Target PDF, σ={σ}")
axis.plot(x, [pdf(j) for j in x])
config.save_post_asset(figure, "hamiltonian_monte_carlo", "hmc_normal_target_pdf-1")

# %%

pdf = momentum_pdf(mass)
x = numpy.linspace(-3.0*mass, 3.0*mass, 500)
figure, axis = pyplot.subplots(figsize=(10, 7))
axis.set_xlabel("p")
axis.set_ylabel("PDF")
axis.set_xlim([x[0], x[-1]])
axis.set_title(f"Momentum PDF, mass={mass}")
axis.plot(x, [pdf(j) for j in x])
config.save_post_asset(figure, "hamiltonian_monte_carlo", "hmc_momentum_pdf-1")

# %%

hmc.canonical_distribution_contour_plot(kinetic_energy(mass),
                                        potential_energy(σ),
                                        [0.02, 0.1, 0.2, 0.4, 0.6, 0.8],
                                        "Canonical Distribution",
                                        "hmc_normal_target_phase_space-1")

# %%

H, p, q, accept = HMC(q0, mass, potential_energy(σ), kinetic_energy(mass), dUdq(σ), dKdp(mass), momentum_verlet_hmc, nsample, nsteps, ε)

# %%

xrange = [-3.0*σ, 3.0*σ]
yrange = [-3.0*mass, 3.0*mass]
npts = 500
bins = [numpy.linspace(xrange[0], xrange[1], 100), numpy.linspace(yrange[0], yrange[1], 100)]

pdf, x, y = pdf_gridded(hmc.canonical_distribution(potential_energy(σ), kinetic_energy(mass)), xrange, yrange, npts)
figure, axis = pyplot.subplots(figsize=(10, 8))
axis.set_xlabel("q")
axis.set_ylabel("p")
axis.set_xlim(xrange)
axis.set_title("Phase Space Samples")
hist, _, _, image = axis.hist2d(p, q, normed=True, bins=bins, cmap=config.alternate_color_map)
contour = axis.contour(x, y, pdf, cmap=config.alternate_contour_color_map)
axis.clabel(contour, contour.levels[::2], fmt="%.1f", inline=True, fontsize=15)
figure.colorbar(image)
config.save_post_asset(figure, "hamiltonian_monte_carlo", "phase_space_histogram-1")

# %%

σ = 1.0
pdf = target_pdf(σ)

title = f"HMC Normal Target: Δt={ε}, nsteps={nsteps}, nsample={nsample}, accepted={accept}"
gplot.pdf_samples(title, pdf, q, "hamiltonian_monte_carlo", "normal_sampled_pdf-1")