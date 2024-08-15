## Exercise set 3 (NumPy, qubits, CV)


#### A: More NumPy practice

1. Read this tutorial on the powerful but confusing `einsum` function while testing it on the side: [Einsum Visualized. A Swiss army knife of the array… | by Lev Maximov | Better Programming](https://betterprogramming.pub/einsum-visualized-c050903145ef)
2. Read [this tutorial on RealPython](https://realpython.com/numpy-random-number-generator/) about random number generation and randomisation or, if you prefer, the [NumPy documentation about its random generator](https://numpy.org/doc/stable/reference/random/generator.html). Note that there was a large overhaul of the `np.random` module with version 1.17 (in 2019) as documented [here](https://numpy.org/doc/stable/reference/random/new-or-different.html), so quite a bit of the tutorials you find online may be using the deprecated version. Play around a bit as you go along.

#### B: Random circuit sampling

You should now try to sample random quantum circuits. Experimentally sampling random circuits has been used e.g. by [Google](https://www.nature.com/articles/s41586-019-1666-5), [USTC](https://www.science.org/doi/full/10.1126/science.abe8770) and [Xanadu](https://www.nature.com/articles/s41586-022-04725-x) to demonstrate quantum computational advantage (or supremacy). Read the first few pages of [Mullane - Sampling random quantum circuits: a pedestrian's guide](https://arxiv.org/abs/2007.07872) for a rough idea of what random circuit sampling entails and why it is interesting.

Here, you are not going to perform quantum experiments or to do classical simulation at the cutting edge, but simply use your quantum circuit simulator to generate more or less random circuits from fixed gates (H, X, Y, Z, CNOT, etc.) and/or parametrised gates (RX(θ), RY(θ), RZ(θ), CR(θ), XX(θ), etc.).

[Sim et al.](https://onlinelibrary.wiley.com/doi/abs/10.1002/qute.201900070) defines the _expressibility_ of a quantum circuit as the [Kullback-Leibler divergence](https://omni.wikiwand.com/en/articles/Kullback%E2%80%93Leibler_divergence#Definition) of the discrete distribution $P(F)$ with the discrete distribution $Q(F)=(N-1)(1-F)^{(N-2)}$. The idea of expressibility is to quantify how close to a truly random circuit you can get. Lower values are better.

Here, $P(F)$ (or $\hat P_\text{PQC}(F;\theta)$ ) is the distribution of fidelities $F = |\langle\psi_\Theta| \psi_\Phi\rangle|^2$ between pairs of states sampled from the output of a random circuit - here, specifically for parametrised circuits where $\Theta$ and $\Phi$ represent the set of randomly sampled gate parameters. $P(F)$ is continuous, but in a numerical experiment it will be discretised by building a histogram of the sampled fidelities.

$Q(F)$ (or $P_\text{Haar}(F)$ ) is the theoretical distribution of fidelities when the unitary $U$ of the circuit is sampled uniformly from the distribution of all $n$-qubit unitaries (Haar-distributed).

1. Read sections 3.1.1 and 3.1.2 of Sim et al. and study Figure 1. This should give you a good idea of the main concept.
2. Using your circuit simulator, set up some code for generating random circuits. You can sample from a set of fixed gates, as described at the top of p.5 of Mullane, or you can sample parameters of a fixed configuration of parametrised gates, as in Sim et al. -- or you can combine both.
3. Now create some code for calculating the expressibility of the circuit. Compare shallow (few-gate) with deeper circuits - and if possible, try to vary the number of qubits as well.

#### C: Continuous variables and the harmonic oscillator

Quantum states of a harmonic oscillator like an optical field mode can be described in a number of different mathematical forms. For pure states, there's the wavefunction in the discrete Fock state basis $\sum_n c_n|n\rangle$ with $c_n=\langle n|\psi\rangle$ or the continuous position basis $\int_{-\infty}^\infty \psi(x)|x\rangle$ with $\psi(x)=\langle x|\psi\rangle$. For general, possibly mixed states, the equivalent representations are the density matrix in the Fock basis $\hat\rho_{mn} = \langle m|\hat\rho|n \rangle$ and the Wigner function $W(x,p) = \frac{1}{2\pi} \int_{-\infty}^\infty e^{iyp}\langle x-\frac{y}{2}|\hat\rho|x+\frac{y}{2}\rangle dy$.

These two formulations - density matrix and Wigner function - are equivalent, but useful for different purposes. There are some compact formulas for conversion between them, as presented in [my thesis](https://www.researchgate.net/profile/Jonas-Neergaard-Nielsen/publication/236134209_Generation_of_single_photons_and_Schrodinger_kitten_states_of_light/links/5411626e0cf29e4a232953a5/Generation-of-single-photons-and-Schroedinger-kitten-states-of-light.pdf) on the lower half of p. 10. 

1. Construct functions that can convert between the density matrix and Wigner function descriptions of a single-mode quantum state of the harmonic oscillator.
2. Test your code on some sample states: Fock states and superpositions of these (easy to define in Fock space), Gaussian states (that have simple Wigner functions), cat states (Wigner and Fock basis descriptions in my thesis pp. 20-21), etc.
3. Profile your code e.g with %timeit, %prun, %lprun and identify potential bottlenecks. See if there may be potential to speed it up with algorithm optimisation, vectorisation, caching (lru_cache), compilation (Numba, numexpr, Cython).  
Be sure to keep your different versions around to be able to present your findings.
