class IntervalManager:
    def __init__(self):
        self.intervals = []

    def add_interval(self, interval):
        # Check if the interval is already engulfed by existing intervals
        existing_interval = self._find_engulfing_interval(interval)
        if existing_interval is not None:
            return

        # Remove pieces of intervals that are engulfed by the interval being added
        self._remove_engulfed_intervals(interval)

        # Combine two intervals into one if necessary
        self._combine_intervals(interval)

        # Add the interval
        self.intervals.append(interval)

    def contains(self, number):
        for interval in self.intervals:
            if interval[0] <= number <= interval[1]:
                return True
        return False

    def _find_engulfing_interval(self, interval):
        for i in self.intervals:
            if i[0] <= interval[0] and interval[1] <= i[1]:
                return i
        return None

    def _remove_engulfed_intervals(self, interval):
        self.intervals = [i for i in self.intervals if not (interval[0] <= i[0] and i[1] <= interval[1])]

    def _combine_intervals(self, interval):
        for i in self.intervals:
            if i[0] <= interval[0] <= i[1] or i[0] <= interval[1] <= i[1]:
                interval[0] = min(interval[0], i[0])
                interval[1] = max(interval[1], i[1])
                self.intervals.remove(i)
                self._combine_intervals(interval)
                break
    def print_subtracted_intervals(self, N):
        if self.intervals[0][0] == 0 and self.intervals[0][1] == N:
            print("All painted")
            return
        self.intervals.sort(key=lambda x: x[0])
        start = 0
        for interval in self.intervals:
            if start < interval[0]:
                print(f"{start} {interval[0]}")
            start = interval[1] 
        if start < N:
            print(f"{start} {N}")
im = IntervalManager()
l = int(input())
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    im.add_interval([a,b])

im.print_subtracted_intervals(l)