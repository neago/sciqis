## Exercise set 1 (intro, packaging)

#### A: Package management

##### A.1: Set up an environment

1. Using `mamba` or `conda` on the command line, create and activate an environment to be used for the rest of today's work.
2. Install numpy, jupyterlab, and whatever else you think you need. Use the conda-forge channel instead of the default channel.
   (If you use miniforge, conda-forge is the only channel. Otherwise use the `-c conda-forge` option.)
   A few packages may be unavailable on conda channels and may need `pip` for installation. `qutip-qip` is currently one example, as it seemingly hasn't been packaged yet.
3. Try to export the environment to an `environment.yml` file, remove the environment, and recreate it from this file. And/or write the `environment.yml` file from scratch and create from that.
   If you edit this file, you can update the environment with `mamba env update -f environment.yml --prune`.

**References**

* [conda.org](https://conda.org/community)
	* [Getting started with conda — conda 24.7.2.dev18 documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
	* [Managing environments — conda 24.7.2.dev18 documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
	* [Cheatsheet — conda 24.7.2.dev18 documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).
* [conda-forge | community-driven packaging for conda](https://conda-forge.org)
* [Mamba User Guide — documentation](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html)

#### B: Version control

##### B.1: Configure git and Github

Only if you don't already have a working configuration:

1. [Install git](https://git-scm.com/downloads).
2. [Do basic git configuration](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) (the Your Identity section).
3. Create an account on [Github](https://github.com).
4. [Set up SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for authentication to Github.

##### B.2: Basic version control on the command line

1. [Create a new repository](https://github.com/new) on Github under your own account. This is just a sandbox for testing git, and can be deleted later.
2. From the green "Code" button, get the repository's SSH address.
3. Using git's command line interface, clone the repository to your local machine: `git clone <copied URL>`
4. Now, create and edit some text files and play around with git on the command line: Basic functionality if you're inexperienced or more advanced functionality (stash, merge, rebase, reset, revert, ...) if you're experienced.
   Examples of basic commands: `add`, `commit`, `push`, `pull`, `status`, `log`, `diff`, `rm`, `mv`, `branch`, `checkout`
   
Here's an excellent [interactive cheatsheet](https://ndpsoftware.com/git-cheatsheet.html) and [a PDF cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).

##### B.3: Version control in IDEs

1. Figure out (again, if you don't already know) how to do all the basic git functions, but now from inside your favourite IDE.
2. Do the same, now in JupyterLab and in VS Code.

##### B.4: Github features

1. Create a feature branch, open a pull request on Github, accept it.
2. Try to create an issue, referencing a pull request within it. Play around with some of the many features on Github.

**References**

* [IPython Cookbook - 2.4. A typical workflow with Git branching](https://ipython-books.github.io/24-a-typical-workflow-with-git-branching/)

#### C: Notebooks vs. .py files, package development

Let's try a typical scientific coding workflow: Goof around in a notebook, figure out that some of your code will be useful later, compartmentalise the code into functions and perhaps classes, refactor the reusable code into a .py script, and finally organise it into an installable package.

You can come up with completely arbitrary dummy code, but you could also consider creating a collection of functions you can imagine using again and again - a kind of personal formula collection.

1. Develop and test your code in a notebook. A "real" programmer would usually not use notebooks but code directly in .py files, but in science and data science it is very common since it matches the interactive and exploratory approach to coding.
   Then, when you have a useful function, copy it into a .py file.
2. Alternatively (or in addition), you may write your functions directly in a .py file. In that case, you should try to import the module from inside a notebook and test it out there.
3. Add documentation to the code!
4. Create the directory structure and config files needed to create a package with `setuptools` and `build` that you can import system-wide using an editable install (see references and [my template package](https://github.com/neago/bumpy-banana)).
5. Check that you can import your newly developed package from any folder on your system. Now play around with the namespaces of your package, e.g. by adding `import` statements to `__init__.py`.

**References**

* [Understanding setup.py, setup.cfg and pyproject.toml in Python – SomeBeans](https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/)
* [A Practical Guide to Setuptools and Pyproject.toml - Xebia](https://xebia.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/)
* [Quickstart - setuptools 72.2.0.post20240802 documentation](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)

#### D: IDEs

If you have nothing else left to do, try to discover new features in your favourite IDE and/or get to know one of the other IDEs: [VS Code](https://code.visualstudio.com), [JupyterLab](https://jupyter.org/), [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org) are probably the most common. [Google Colab](https://colab.research.google.com) is also worth knowing.