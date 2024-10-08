## Exercise set 4 (QuTiP, animations, interactive plots)

## A: Widgets and interactive plots

1. Create an interactive visualisation using `ipywidgets` that shows the Wigner function of a vacuum state with various operations applied to it: displacement, squeezing, photon addition, etc.  Use either your own Wigner function code (should at least be possible to apply it to different number states $|0\rangle, \hat a^\dagger|0\rangle=|1\rangle, \cdots$) or QuTiP to calculate the Wigner functions.

## B: Animations in Matplotlib

1. Create a simple animation, for example of a plot of $\cos(\omega t + \phi)$ where $\phi$ is varied. Try using both `ArtistAnimation` and `FuncAnimation` as [described in the Matplotlib docs](https://matplotlib.org/stable/users/explain/animations/animations.html). Check also [this tutorial](https://matplotlib.org/stable/gallery/animation/dynamic_image.html) and [this tutorial](https://matplotlib.org/stable/gallery/animation/simple_anim.html) (which is actually doing more or less what you're asked to do here - so try to expand on the example).

## C: Solving master equations with QuTiP

1. Starting from [this QuTiP tutorial](https://nbviewer.org/urls/qutip.org/qutip-tutorials/tutorials-v5/time-evolution/006_photon_birth_death.ipynb) which replicates [one of the papers on cavity QED](http://dx.doi.org/10.1038/nature05589) that contributed to the 2012 Nobel prize of Serge Haroche, try to come up with new ways to visualise the results. This could be as a static plot, an animation, or an interactive plot. 
2. Change the parameters of the simulation, like changing the initial state, the time steps, the number of trajectories, the coupling rate, environment temperate, etc. - you may discover something interesting by varying these.

Note that you can store all trajectories with the `keep_runs_results` option to `mcsolve` described [here](https://qutip.readthedocs.io/en/master/apidoc/classes.html#qutip.solver.mcsolve.MCSolver.options), and then access e.g. the expectation of the operators in `e_ops` at each time with the result's `runs_expect` property.