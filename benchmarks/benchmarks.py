from asv_samples.benchme import add_arr


class TimeSuite:
    """
    Benchmark that times various operations, including custom summation of
    lists.
    """

    def setup(self):
        self.list1 = [i for i in range(500)]
        self.list2 = [i for i in range(500, 1000)]

    def time_add_arr(self):
        """
        Time the add_arr function with two lists of numbers.
        """
        add_arr(self.list1, self.list2)
