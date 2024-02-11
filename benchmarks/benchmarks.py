from asv_runner.benchmarks.mark import SkipNotImplemented

class MemrayBenchmarks:
    params = [10, int(2e4)]

    def ray_sum(self, n):
        try:
            import numpy as np
        except ImportError:
            raise SkipNotImplemented("Can't run without NumPy")
        self.data = np.random.rand(n)
        np.sum(self.data)
