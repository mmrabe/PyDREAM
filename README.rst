PyDREAMx
--------

A Python implementation of the MT-DREAM(ZS) algorithm presented in `Laloy and Vrugt 2012 <http://faculty.sites.uci.edu/jasper/files/2016/04/72.pdf>`_.

For example usage, see the examples folder.  Two of the examples, CORM and Robertson, require the Python modeling framework `PySB <https://github.com/LoLab-VU/pysb>`_.

Documentation is available at `Read the Docs <http://pydream.readthedocs.io>`_.

This is a fork of the original v1.0 implementation by `Erin Shockley <https://github.com/LoLab-VU/PyDREAM>`_ with the ability to toggle multiprocessing and likelihood reevaluation.

Shockley’s original implementation uses multiprocessing by default, as native Python is typically incapable of multicore computations. However, if the actual likelihood computation is performed by an external algorithm, such as a C Python module with OpenMP multithreading, multiprocessing may be disabled, as the multithreading is taken care of outside the Python GIL. In that case, all core DREAM operations are performed on a single core, while OpenMP in the external module takes care of the workload balancing across cores. In that case, run_dream accepts an additional parameter multiprocessing, which may be set to False to explicitly disable multiprocessing. If ignored or True, multiprocessing is used (as is the default in Shockley’s PyDREAM).

Moreover, the original implementation does not allow likelihood reevaluation, i.e. the reevaluation of the current state in the consecutive evaluations after acceptance. This, however, is necessary for non-deterministic/stochastic/noisy likelihood computations. You may use the additional parameter stochastic_loglike and set it to True in order to enable likelihood reevaluation. If ignores or False, the likelihood is not reevaluated (as is the default in Shockley’s PyDREAM).
