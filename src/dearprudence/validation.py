import logging

from dearprudence.errors import ParameterFileValidationError
from dearprudence.utils import check_dtr_data_exists, check_simplerun_data_exists


def _validate_matching_key_attrs(a, b, error_attrs=None, warn_attrs=None):
    """Raise error or warning if attrs do not match between a and b"""
    if not error_attrs:
        error_attrs = ("table_id", "source_id", "grid_label")

    if not warn_attrs:
        warn_attrs = ("member_id",)

    for attr in error_attrs:
        if getattr(a, attr) != getattr(b, attr):
            raise ParameterFileValidationError(
                f"{attr} does not match between {a} and {b}"
            )

    for attr in warn_attrs:
        if getattr(a, attr) != getattr(b, attr):
            # warnings.warn(f"{attr} does not match between {a} and {b}", ParameterFileValidationWarning)
            logging.warning(f"{attr} does not match between {a} and {b}")

    return True


def _validate_simplerun_variable_id(a, goal_variable_id):
    """Raise error if variable_id does not match across root, ssp, historical"""

    if a.variable_id != goal_variable_id:
        raise ParameterFileValidationError(
            f".variable_id does not equal {goal_variable_id} in {a}"
        )

    if a.ssp.variable_id != goal_variable_id:
        raise ParameterFileValidationError(
            f".ssp.variable_id does not equal {goal_variable_id} in {a}"
        )

    if a.historical.variable_id != goal_variable_id:
        raise ParameterFileValidationError(
            f".historical.variable_id does not equal {goal_variable_id} in {a}"
        )

    return True


def validate_simplerun(r, variable_id=None):
    """Basic sanity-check validation of a SimpleRun"""
    _validate_matching_key_attrs(r.ssp, r.historical)
    _validate_simplerun_variable_id(r, goal_variable_id=variable_id)
    return True


def _validate_dtr_targets(r):
    """Raise error if dtr, tasmin, tasmax do not share the same 'target'"""
    if r.target != r.tasmin.target:
        raise ParameterFileValidationError(
            f".target does not equal .tasmin.target in {r}"
        )

    if r.target != r.tasmax.target:
        raise ParameterFileValidationError(
            f".target does not equal .tasmax.target in {r}"
        )

    return True


def validate_dtrrun(r):
    """Basic sanity-check validation of a DtrRun"""
    if r.variable_id != "dtr":
        raise ParameterFileValidationError(f".variable_id does not equal 'dtr' in {r}")

    _validate_dtr_targets(r)

    validate_simplerun(r.tasmin, variable_id="tasmin")
    validate_simplerun(r.tasmax, variable_id="tasmax")

    _validate_matching_key_attrs(r.tasmax.ssp, r.tasmin.ssp)
    _validate_matching_key_attrs(r.tasmax.historical, r.tasmin.historical)

    return True


def validate_params(runs, check_inputs_exist=False):
    for r in runs:

        if r.variable_id == "dtr":
            validate_dtrrun(r)
            if check_inputs_exist:
                check_dtr_data_exists(r)

        elif r.variable_id in ("tasmax", "tasmin", "pr"):
            validate_simplerun(r, str(r.variable_id))
            if check_inputs_exist:
                check_simplerun_data_exists(r)

    return True
