## Day 2 (NumPy, qubits)

#### NumPy basics

1. Unless you are quite experienced with NumPy, work through this good, efficient tutorial on many of NumPy's basics: [GitHub - jrjohansson/scientific-python-lectures: Lectures on scientific computing with python, as IPython notebooks.](https://github.com/jrjohansson/scientific-python-lectures) 
   Note, though, that it is a bit dated - for example, you don't need the `matrix` type to do matrix multiplication: You can simply use the `@` operator between arrays.
   An excellent alternative, although not a notebook, is this great illustrated tutorial: [NumPy Illustrated: The Visual Guide to NumPy | by Lev Maximov | Better Programming](https://betterprogramming.pub/3b1d4976de1d?sk=57b908a77aa44075a49293fa1631dd9b).
2. Do the [GitHub - rougier/numpy-100: 100 numpy exercises (with solutions)](https://github.com/rougier/numpy-100) from the beginning - get as far as you can, but feel free to skip exercises you find irrelevant. Beware - they quickly get challenging! Be sure to think/try for a while before referring 

#### A simple quantum circuit simulator

There are probably a hundred or more quantum computing simulators out there, but let's add to that count! :)

1. If you are not familiar with qubits, quantum gates and quantum circuits, take a moment to skim chapters 2, 3, 4.1, 4.2, 5.3 and 7.1 of [Scott Aaronson's lecture notes](https://www.scottaaronson.com/qclec.pdf) - or go to Jonas for a quick intro.
   For a more rigorous treatment, see [these lessons by John Watrous](https://learning.quantum.ibm.com/course/basics-of-quantum-information).
   Somewhere in-between is the [Wikipedia page on quantum gates](https://omni.wikiwand.com/en/articles/Quantum_logic_gate).
   Wikipedia's [List of quantum logic gates](https://omni.wikiwand.com/en/articles/List_of_quantum_logic_gates) is a concise list of common gates.
2. Set up a new public repository on your Github account, to be used for this and the _Random circuit sampling_ exercise. While developing, remember to practice a git workflow: commit at appropriate times (remember meaningful commit messages), sync (pull-push), use branches if needed (or just for practice).
3. Now, build a quantum circuit simulator that can take an input state vector $|\psi_{{in}}\rangle$ and a series of gates $\{U_i\}$ and use this to calculate the output state vector $|\psi_{out}\rangle = U_n\ldots U_1 |\psi_{in}\rangle$. 
   Below are some hints and suggestions for different directions you could take:
	- You can make this as simple or as complex as you feel comfortable with, but it's a good idea to start simple, test that it works, and then expand the scope gradually.
	- A single-qubit simulator is significantly simpler than a simulator for multiple qubits. You may wish to start with just one qubit.
	- For multi-qubit circuits, you need the tensor product between the Hilbert spaces to get e.g. $|\psi\rangle_A \otimes |\phi\rangle_B$ and $U_A \otimes U_B$. The matrix of the tensor product is called the [Kronecker product](https://omni.wikiwand.com/en/articles/Kronecker_product) and is implemented in NumPy by `np.kron`.
	- No need to implement all possible gates. Just choose a representative set - it can easily be expanded later on.
	- You can optionally implement a measurement at the end: Given an $n$-qubit output state $|\psi_{out}\rangle$, the probability of measuring the bit string $x_1\ldots x_n$ is $|\langle x_1\ldots x_n|\psi_{out}\rangle|^2$. One way of sampling from this probability distribution is using `np.random.Generator.choice`.
	- If you're comfortable with object-oriented programming or wish to practice it, you could create classes representing e.g. states, gates, and circuits.
	- You can package your code.
	- If your code supports an arbitrary number of qubits, you could try to do a timing analysis: how does the simulation time scale with the number of qubits and gates?