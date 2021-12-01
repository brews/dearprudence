import dataclasses
import json

from dearprudence.core import Cmip6Record, DtrRun, SimpleRun


__all__ = ["read_params", "write_params"]


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


def read_params(urlpath):
    """Read run parameters form yaml file"""
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


class _DataclassJSONEncoder(json.JSONEncoder):
    """Encoder to dump dataclasses to JSON
    """
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def write_params(urlpath, runlist, mode="w"):
    """Write runs parameters to parameter file"""
    runlist = list(runlist)
    with open(urlpath, mode=mode) as fl:
        fl.write("jobs: |\n")
        fl.write("  " + json.dumps(runlist, cls=_DataclassJSONEncoder, separators=(",", ":")) + "\n")
