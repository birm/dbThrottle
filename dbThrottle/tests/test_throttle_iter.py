from dbThrottle import ThrottleIter
from dbThrottle import ThrottleMethod

def test_default_init():
    iterable = range(10)
    def performer(x):
        print(x)
    throttle = ["localhost", ThrottleMethod().test_metric, 0.5]
    ti = ThrottleIter(iterable, performer, throttle)
