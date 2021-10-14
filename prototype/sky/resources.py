from typing import NamedTuple, Tuple

from sky import clouds


class Resources(NamedTuple):
    cloud: clouds.Cloud
    types: Tuple[str]

    def __repr__(self) -> str:
        return f'{self.cloud}({self.types})'

    def get_cost(self, seconds):
        """Returns cost in USD for the runtime in seconds."""
        cost = 0.0
        typs = self.types
        if type(typs) is str:
            typs = [typs]
        for instance_type in typs:
            hourly_cost = self.cloud.instance_type_to_hourly_cost(instance_type)
            cost += hourly_cost * (seconds / 3600)
        return cost