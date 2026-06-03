class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], 
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        if n == 0 or m == 0:
            return -1

        # Sort rides by start time
        land = sorted(zip(landStartTime, landDuration))
        water = sorted(zip(waterStartTime, waterDuration))

        land_starts = [s for s, _ in land]
        land_durations = [d for _, d in land]
        water_starts = [s for s, _ in water]
        water_durations = [d for _, d in water]

        # Precompute suffix minimums of finish times
        water_finish = [s + d for s, d in water]
        water_suffix_min = [0] * m
        water_suffix_min[-1] = water_finish[-1]
        for i in range(m - 2, -1, -1):
            water_suffix_min[i] = min(water_finish[i], water_suffix_min[i + 1])

        land_finish = [s + d for s, d in land]
        land_suffix_min = [0] * n
        land_suffix_min[-1] = land_finish[-1]
        for i in range(n - 2, -1, -1):
            land_suffix_min[i] = min(land_finish[i], land_suffix_min[i + 1])

        # Precompute prefix minimums of durations
        water_prefix_min_dur = [0] * m
        water_prefix_min_dur[0] = water_durations[0]
        for i in range(1, m):
            water_prefix_min_dur[i] = min(water_prefix_min_dur[i - 1], water_durations[i])

        land_prefix_min_dur = [0] * n
        land_prefix_min_dur[0] = land_durations[0]
        for i in range(1, n):
            land_prefix_min_dur[i] = min(land_prefix_min_dur[i - 1], land_durations[i])

        min_time = float('inf')

        # \U0001f501 For each land ride
        for l_start, l_dur in land:
            l_end = l_start + l_dur

            idx = bisect.bisect_right(water_starts, l_end)
            if idx > 0:
                min_dur = water_prefix_min_dur[idx - 1]
                finish_time = l_end + min_dur
                min_time = min(min_time, finish_time)

            idx = bisect.bisect_left(water_starts, l_end)
            if idx < m:
                finish_time = water_suffix_min[idx]
                min_time = min(min_time, finish_time)

        # \U0001f501 For each water ride
        for w_start, w_dur in water:
            w_end = w_start + w_dur

            idx = bisect.bisect_right(land_starts, w_end)
            if idx > 0:
                min_dur = land_prefix_min_dur[idx - 1]
                finish_time = w_end + min_dur
                min_time = min(min_time, finish_time)

            idx = bisect.bisect_left(land_starts, w_end)
            if idx < n:
                finish_time = land_suffix_min[idx]
                min_time = min(min_time, finish_time)

        return min_time if min_time != float('inf') else -1
