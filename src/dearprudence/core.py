from dataclasses import dataclass


__all__ = ["Cmip6Record", "SimpleRun"]


@dataclass
class Cmip6Record:
    activity_id: str
    experiment_id: str
    table_id: str
    variable_id: str
    source_id: str
    institution_id: str
    member_id: str
    grid_label: str
    version: str


@dataclass
class SimpleRun:
    target: str
    variable_id: str
    historical: Cmip6Record
    ssp: Cmip6Record
