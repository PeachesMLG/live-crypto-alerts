class IntervalHistory():
    def __init__(self, interval):
        self.interval = interval
        self.emas = []
        self.ohlcv = []
