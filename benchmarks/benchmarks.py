from asv_runner.benchmarks.mark import (
    skip_for_params,
    parameterize,
    SkipNotImplemented,
    skip_benchmark_if,
    skip_params_if,
    skip_benchmark,
)
import datetime


class TimeSuite:
    params = [100, 200, 300, 400, 500]
    param_names = ["size"]

    def setup(self, size):
        self.d = {}
        for x in range(size):
            self.d[x] = None

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_keys(self, size):
        for key in self.d.keys():
            pass

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_values(self, size):
        for value in self.d.values():
            pass

    @skip_benchmark_if(datetime.datetime.now().hour >= 12)
    def time_range(self, size):
        d = self.d
        for key in range(size):
            d[key]

    # Skip benchmarking when size is either 100 or 200 and the current hour is 12 or later.
    @skip_params_if([(100,), (200,)], datetime.datetime.now().hour >= 12)
    def time_dict_update(self, size):
        d = self.d
        for i in range(size):
            d[i] = i


# Fast because no setup is called
class SimpleFast:
    params = [False, True]
    param_names = ["ok"]

    @skip_for_params([(False,)])
    def time_failure(self, ok):
        if ok:
            x = 34.2**4.2


@parameterize({"ok": [False, True]})
class SimpleSlow:
    def time_failure(self, ok):
        if ok:
            x = 34.2**4.2
        else:
            raise SkipNotImplemented(f"{ok} is skipped")


@skip_benchmark
class TimeSuiteTwo:
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_values(self):
        for value in self.d.values():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            d[key]
