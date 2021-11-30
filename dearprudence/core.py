from dataclasses import dataclass
import dataclasses
import json


__all__ = ["Cmip6Record", "SimpleRun", "DtrRun", "read_paramfile"]


class _PrudentJSONEncoder(json.JSONEncoder):
    """Encoder used when dumping dataclasses to JSON
    """
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


class IoMixin:
    """
    Mixin so core dataclasses can dump to yaml parameter file
    """
    def to_yaml(self, urlpath, mode="w"):
        """Write parameterfile to urlpath"""
        with open(urlpath, mode=mode) as fl:
            fl.write("jobs: |\n")
            fl.write("  " + json.dumps([self], cls=_PrudentJSONEncoder) + "\n")


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
class SimpleRun(IoMixin):
    target: str
    variable_id: str
    historical: Cmip6Record
    ssp: Cmip6Record


@dataclass
class DtrRun(IoMixin):
    target: str
    variable_id: str
    tasmin: SimpleRun
    tasmax: SimpleRun


def _load_paramfile(urlpath):
    with open(urlpath) as fl:
        # Pop off and discard the first "yaml" bit.
        _ = fl.readline()
        return json.load(fl)


def _unpack_simplerun(p):
    return SimpleRun(
        target=p["target"],
        variable_id=p["variable_id"],
        historical=Cmip6Record(**p["historical"]),
        ssp=Cmip6Record(**p["ssp"])
    )


def read_paramfile(urlpath):
    """Read run parameter file"""
    payload = _load_paramfile(urlpath)

    out = []
    for entry in payload:
        if entry["variable_id"].lower() == "dtr":
            out.append(
                DtrRun(
                    target=entry["target"],
                    variable_id=entry["variable_id"],
                    tasmin=_unpack_simplerun(entry["tasmin"]),
                    tasmax=_unpack_simplerun(entry["tasmax"])
                )
            )
        else:
            out.append(_unpack_simplerun(entry))

    return out
