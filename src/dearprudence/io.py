import dataclasses
import json
from os import PathLike
from typing import Union, TextIO, BinaryIO, Any, TypedDict, Sequence

from dearprudence.core import Cmip6Record, SimpleRun


__all__ = ["read_params", "write_params"]


# TypedDict mappings representing intermediate dicts loaded from JSON.
class Cmip6RecordMapping(TypedDict):
    activity_id: str
    experiment_id: str
    table_id: str
    variable_id: str
    source_id: str
    institution_id: str
    member_id: str
    grid_label: str
    version: str


class SimpleRunMapping(TypedDict):
    variable_id: str
    target: str
    historical: Cmip6RecordMapping
    ssp: Cmip6RecordMapping


def _load_paramfile(
    urlpath: Union[str, Union[TextIO, BinaryIO]]
) -> Sequence[SimpleRunMapping]:
    # First readline() to pop-off and discard the first yaml bit of
    # the file, then load as JSON str. Keeps us from depending
    # on pyyaml.
    if isinstance(urlpath, str):
        with open(urlpath, "r") as fl:
            # Pop off and discard the first "yaml" bit.
            _ = fl.readline()
            return json.load(fl)
    else:
        # Pop off and discard the first "yaml" bit.
        _ = urlpath.readline()
        return json.load(urlpath)


def _unpack_simplerun(p: SimpleRunMapping) -> SimpleRun:
    return SimpleRun(
        target=p["target"],
        variable_id=p["variable_id"],
        historical=Cmip6Record(**p["historical"]),
        ssp=Cmip6Record(**p["ssp"]),
    )


def read_params(urlpath: Union[str, Union[TextIO, BinaryIO]]) -> list[SimpleRun]:
    """Read run parameters form yaml file"""
    return [_unpack_simplerun(x) for x in _load_paramfile(urlpath)]


class _DataclassJSONEncoder(json.JSONEncoder):
    """Encoder to dump dataclasses to JSON"""

    def default(self, o: Any) -> Any:
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def write_params(
    urlpath: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int],
    runlist: Sequence[SimpleRun],
    mode: str = "w",
    pretty: bool = True,
) -> None:
    """Write runs parameters to parameter file"""
    runlist = list(runlist)

    if pretty:
        # Whitespace, indenting, with additional 2 space indents because this
        # is a nested JSON string embedded in yaml.
        json_payload = json.dumps(runlist, cls=_DataclassJSONEncoder, indent=2).replace(
            "\n", "\n  "
        )
    else:
        # Remove pretty whitespace around key-value separators, etc.
        json_payload = json.dumps(
            runlist, cls=_DataclassJSONEncoder, separators=(",", ":")
        )

    with open(urlpath, mode=mode) as fl:
        fl.write("jobs: |\n")
        fl.write("  " + json_payload + "\n")
