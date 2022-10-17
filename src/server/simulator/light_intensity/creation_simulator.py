import random

import requests


def create_light_intensity_point(url: str, sensor: str, value: float):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"sensor": sensor, "value": value}

    r = requests.post(url=url, headers=headers, json=data)
    r.raise_for_status()

    return r


class LightIntensityPointCreationSimulator:
    def __init__(self, url: str, sensor: str, n: int, min_val=0, max_val=1000):
        self._url = url
        self._sensor = sensor
        self._n = n
        self._data = []
        self._min_val = min_val
        self._max_val = max_val

        self._create_random_data(n)

    def _create_random_data(self, num: int):
        for _ in range(num):
            random_value = random.uniform(self._min_val, self._max_val)
            self._data.append(random_value)

    def _create_light_intensity_point(self, value):
        return create_light_intensity_point(self._url, self._sensor, value)

    def _simulate(self):
        for v in self._data:
            self._create_light_intensity_point(v)

    def _delete_all_simulation_points(self):
        url = f"{self._url}{self._sensor}/delete_all/"

        r = requests.get(url=url)
        r.raise_for_status()

        return r

    def _get_light_intenstiy_points(self):
        url = f"{self._url}{self._sensor}/points/"

        r = requests.get(url=url)
        r.raise_for_status()

        return r.json()

    def simulate_and_check(self):
        self._delete_all_simulation_points()
        print("Delete all points previously stored with the same sensor")

        self._simulate()
        print("Data points simulated")

        intensity_points = self._get_light_intenstiy_points()

        assert len(intensity_points) == self._n
        print("The number of intensity points matches the expectation")

        for i, intensity_point in enumerate(intensity_points):
            original_value = self._data[i]

            assert intensity_point["value"] == original_value
            assert intensity_point["sensor"] == self._sensor
        print("All points matched the expectation")

        self._delete_all_simulation_points()


if __name__ == "__main__":
    url = "http://localhost:8000/light_intensity_points/"
    sensor = "test"

    simulator = LightIntensityPointCreationSimulator(url, sensor, 100)
    simulator.simulate_and_check()
