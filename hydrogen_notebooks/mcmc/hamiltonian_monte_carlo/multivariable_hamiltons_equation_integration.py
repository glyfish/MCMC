%load_ext autoreload
%autoreload 2

import numpy
from matplotlib import pyplot
from glyfish import config
from glyfish import gplot
from glyfish import hamiltonian_monte_carlo as hmc
from glyfish import stats

%matplotlib inline

pyplot.style.use(config.glyfish_style)

# %%
# Integration parameters

t = 2.0*numpy.pi
ε = 0.1
nsteps = int(t/ε)

# %%
# Integration parameters
p0 = [-1.0, 1.0]
q0 = [1.0, -1.0]

m1 = 1.0
m2 = 1.0

σ1 = 1.0
σ2 = 1.0
γ = 0.0

dUdq = hmc.bivariate_normal_dUdq(γ, σ1, σ2)
dKdp = hmc.bivariate_normal_dKdp(m1, m2)
time = numpy.linspace(0.0, t, nsteps+1)

# %%

p, q = hmc.momentum_verlet(p0, q0, 2, dUdq, dKdp, nsteps, ε)
title = r"$\sigma_1=$" f"{σ1}, " + r"$\sigma_2=$" f"{σ2}, " + f"γ={γ}, Δt={ε}, steps={nsteps}"
hmc.phase_space_plot(p[:,0], q[:,0], title, [r"$q_1$", r"$p_1$"], (0.2, 0.7), "bivariate_normal_phase_space_plot_1")

# %%

hmc.phase_space_plot(p[:,1], q[:,1], title, [r"$q_2$", r"$p_2$"], (0.2, 0.7), "bivariate_normal_phase_space_plot_2")

# %%

hmc.phase_space_plot(q[:,0], q[:,1], title, [r"$q_1$", r"$q_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_3")

# %%

hmc.phase_space_plot(p[:,0], p[:,1], title, [r"$p_1$", r"$p_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_4")

# %%

hmc.multicurve(title, [q[:,0], q[:,1]], time, "Time", "q", [r"$q_1$", r"$q_2$"],  (0.2, 0.9), [-2.0, 2.0], "position-timeseries-1")

# %%

hmc.multicurve(title, [p[:,0], p[:,1]], time, "Time", "p", [r"$p_1$", r"$p_2$"],  (0.2, 0.9), [-2.0, 2.0], "momentum-timeseries-1")

# %%

U = hmc.bivariate_normal_U(γ, σ1, σ2)
K = hmc.bivariate_normal_K(m1, m2)

U_t = numpy.array([U(qt) for qt in q])
K_t =  numpy.array([K(pt) for pt in p])
H = U_t + K_t
hmc.time_series(title, H, time, [-0.1, 3.0], "hamiltonian-timeseries-1")

# %%
# Integration parameters

t = 5.0
ε = 0.001
nsteps = int(t/ε)

# %%
# Integration parameters
p0 = [-1.0, 1.0]
q0 = [-1.0, 1.0]

m1 = 1.0
m2 = 1.0

σ1 = 1.0
σ2 = 1.0
γ = 0.9

dUdq = hmc.bivariate_normal_dUdq(γ, σ1, σ2)
dKdp = hmc.bivariate_normal_dKdp(m1, m2)
time = numpy.linspace(0.0, t, nsteps+1)

# %%

p, q = hmc.momentum_verlet(p0, q0, 2, dUdq, dKdp, nsteps, ε)
title = r"$\sigma_1=$" f"{σ1}, " + r"$\sigma_2=$" f"{σ2}, " + f"γ={γ}, Δt={ε}, steps={nsteps}"
hmc.phase_space_plot(p[:,0], q[:,0], title, [r"$q_1$", r"$p_1$"], (0.2, 0.7), "bivariate_normal_phase_space_plot_5")

# %%

hmc.phase_space_plot(p[:,1], q[:,1], title, [r"$q_2$", r"$p_2$"], (0.225, 0.85), "bivariate_normal_phase_space_plot_6")

# %%

hmc.phase_space_plot(q[:,0], q[:,1], title, [r"$q_1$", r"$q_2$"], (0.9, 0.9), "bivariate_normal_phase_space_plot_7")

# %%

hmc.phase_space_plot(p[:,0], p[:,1], title, [r"$p_1$", r"$p_2$"], (0.8, 0.9), "bivariate_normal_phase_space_plot_8")

# %%

hmc.multicurve(title, [q[:,0], q[:,1]], time, "Time", "q", [r"$q_1$", r"$q_2$"],  (0.15, 0.8), [-2.25, 2.25], "position-timeseries-2")

# %%

hmc.multicurve(title, [p[:,0], p[:,1]], time, "Time", "p", [r"$p_1$", r"$p_2$"],  (0.2, 0.9), [-10.0, 10.0], "momentum-timeseries-2")

# %%

U = hmc.bivariate_normal_U(γ, σ1, σ2)
K = hmc.bivariate_normal_K(m1, m2)

U_t = numpy.array([U(qt) for qt in q])
K_t =  numpy.array([K(pt) for pt in p])
H = U_t + K_t
time = numpy.linspace(0.0, t, nsteps+1)
hmc.time_series(title, H, time, [-1.0, 25.0], "hamiltonian-timeseries-2")

# %%
# Integration parameters

t = 20.0
ε = 0.01
nsteps = int(t/ε)

# %%
# Integration parameters
p0 = [1.0, 1.0]
q0 = [-1.0, -1.0]

m1 = 1.0
m2 = 1.0

σ1 = 1.0
σ2 = 1.0
γ = 0.9

dUdq = hmc.bivariate_normal_dUdq(γ, σ1, σ2)
dKdp = hmc.bivariate_normal_dKdp(m1, m2)

# %%

p, q = hmc.momentum_verlet(p0, q0, 2, dUdq, dKdp, nsteps, ε)
title = r"$\sigma_1=$" f"{σ1}, " + r"$\sigma_2=$" f"{σ2}, " + f"γ={γ}, Δt={ε}, steps={nsteps}"
hmc.phase_space_plot(p[:,0], q[:,0], title, [r"$q_1$", r"$p_1$"], (0.8, 0.85), "bivariate_normal_phase_space_plot_9")

# %%

hmc.phase_space_plot(p[:,1], q[:,1], title, [r"$q_2$", r"$p_2$"], (0.8, 0.85), "bivariate_normal_phase_space_plot_10")

# %%

hmc.phase_space_plot(q[:,0], q[:,1], title, [r"$q_1$", r"$q_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_11")

# %%

hmc.phase_space_plot(p[:,0], p[:,1], title, [r"$p_1$", r"$p_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_12")

# %%

U = hmc.bivariate_normal_U(γ, σ1, σ2)
K = hmc.bivariate_normal_K(m1, m2)

U_t = numpy.array([U(qt) for qt in q])
K_t =  numpy.array([K(pt) for pt in p])
H = U_t + K_t
time = numpy.linspace(0.0, t, nsteps+1)
hmc.time_series(title, H, time, [-1.0, 15.0], "hamiltonian-timeseries-3")

# %%

hmc.multicurve(title, [q[:,0], q[:,1]], time, "Time", "q", [r"$q_1$", r"$q_2$"],  (0.15, 0.8), [-2.25, 2.25], "position-timeseries-3")

# %%

hmc.multicurve(title, [p[:,0], p[:,1]], time, "Time", "p", [r"$p_1$", r"$p_2$"],  (0.2, 0.9), [-10.0, 10.0], "momentum-timeseries-3")

# %%
# Integration parameters

t = 20.0
ε = 0.01
nsteps = int(t/ε)

# %%
# Integration parameters
p0 = [1.0, 1.0]
q0 = [-1.0, -1.0]

m1 = 1.0
m2 = 1.0

σ1 = 1.0
σ2 = 1.0
γ = 0.2

dUdq = hmc.bivariate_normal_dUdq(γ, σ1, σ2)
dKdp = hmc.bivariate_normal_dKdp(m1, m2)

# %%

p, q = hmc.momentum_verlet(p0, q0, 2, dUdq, dKdp, nsteps, ε)
title = r"$\sigma_1=$" f"{σ1}, " + r"$\sigma_2=$" f"{σ2}, " + f"γ={γ}, Δt={ε}, steps={nsteps}"
hmc.phase_space_plot(p[:,0], q[:,0], title, [r"$q_1$", r"$p_1$"], (0.225, 0.85), "bivariate_normal_phase_space_plot_13")

# %%

hmc.phase_space_plot(p[:,1], q[:,1], title, [r"$q_2$", r"$p_2$"], (0.225, 0.85), "bivariate_normal_phase_space_plot_14")

# %%

hmc.phase_space_plot(q[:,0], q[:,1], title, [r"$q_1$", r"$q_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_15")

# %%

hmc.phase_space_plot(p[:,0], p[:,1], title, [r"$p_1$", r"$p_2$"], (0.3, 0.85), "bivariate_normal_phase_space_plot_16")

# %%

U = hmc.bivariate_normal_U(γ, σ1, σ2)
K = hmc.bivariate_normal_K(m1, m2)

U_t = numpy.array([U(qt) for qt in q])
K_t =  numpy.array([K(pt) for pt in p])
H = U_t + K_t
time = numpy.linspace(0.0, t, nsteps+1)
hmc.time_series(title, H, time, [0.0, 8.0], "hamiltonian-timeseries-4")

# %%

hmc.multicurve(title, [q[:,0], q[:,1]], time, "Time", "q", [r"$q_1$", r"$q_2$"],  (0.15, 0.8), [-2.25, 2.25], "position-timeseries-4")

# %%

hmc.multicurve(title, [p[:,0], p[:,1]], time, "Time", "p", [r"$p_1$", r"$p_2$"],  (0.2, 0.9), [-10.0, 10.0], "momentum-timeseries-4")

# %%
# Integration parameters

t = 20.0
ε = 0.01
nsteps = int(t/ε)

# %%
# Integration parameters
p0 = [1.0, 1.0]
q0 = [-1.0, -1.0]

m1 = 1.0
m2 = 1.0

σ1 = 1.0
σ2 = 1.0
γ = 0.1

dUdq = hmc.bivariate_normal_dUdq(γ, σ1, σ2)
dKdp = hmc.bivariate_normal_dKdp(m1, m2)

# %%

p, q = hmc.momentum_verlet(p0, q0, 2, dUdq, dKdp, nsteps, ε)
title = r"$\sigma_1=$" f"{σ1}, " + r"$\sigma_2=$" f"{σ2}, " + f"γ={γ}, Δt={ε}, steps={nsteps}"
hmc.phase_space_plot(p[:,0], q[:,0], title, [r"$q_1$", r"$p_1$"], (0.225, 0.85), "bivariate_normal_phase_space_plot_17")

# %%

hmc.phase_space_plot(p[:,1], q[:,1], title, [r"$q_2$", r"$p_2$"], (0.225, 0.85), "bivariate_normal_phase_space_plot_18")

# %%

hmc.phase_space_plot(q[:,0], q[:,1], title, [r"$q_1$", r"$q_2$"], (0.3, 0.9), "bivariate_normal_phase_space_plot_19")

# %%

hmc.phase_space_plot(p[:,0], p[:,1], title, [r"$p_1$", r"$p_2$"], (0.3, 0.85), "bivariate_normal_phase_space_plot_20")

# %%

U = hmc.bivariate_normal_U(γ, σ1, σ2)
K = hmc.bivariate_normal_K(m1, m2)

U_t = numpy.array([U(qt) for qt in q])
K_t =  numpy.array([K(pt) for pt in p])
H = U_t + K_t
time = numpy.linspace(0.0, t, nsteps+1)
hmc.time_series(title, H, time, [0.0, 8.0], "hamiltonian-timeseries-5")

# %%

hmc.multicurve(title, [q[:,0], q[:,1]], time, "Time", "q", [r"$q_1$", r"$q_2$"],  (0.15, 0.8), [-2.25, 2.25], "position-timeseries-5")

# %%

hmc.multicurve(title, [p[:,0], p[:,1]], time, "Time", "p", [r"$p_1$", r"$p_2$"],  (0.2, 0.9), [-10.0, 10.0], "momentum-timeseries-5")
