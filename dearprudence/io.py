import dataclasses
import json

from dearprudence.core import Cmip6Record, SimpleRun, DtrRun


__all__ = ["read_simpleruns", "read_dtr", "read_tasmax", "read_tasmin", "read_pr"]


def _read_paramfile(urlpath):
    payload=None
    with open(urlpath) as fl:
        # Pop off and discard the first "yaml" bit.
        _ = fl.readline()
        payload = json.load(fl)
    return payload


def read_simpleruns(urlpath):
    payload = _read_paramfile(urlpath)
    return [SimpleRun(target=items["target"], variable_id=items["variable_id"], historical=Cmip6Record(**items["historical"]), ssp=Cmip6Record(**items["ssp"])) for items in payload]


def read_tasmax(*args, **kwargs):
    return read_simpleruns(*args, **kwargs)


def read_tasmin(*args, **kwargs):
    return read_simpleruns(*args, **kwargs)


def read_pr(*args, **kwargs):
    return read_simpleruns(*args, **kwargs)


def read_dtr(urlpath):
    payload = _read_paramfile(urlpath)
    return [DtrRun(**items) for items in payload]


class PrudentJSONEncoder(json.JSONEncoder):
    # json.dumps(dataclass, cls=PrudentJSONEncoder)
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

