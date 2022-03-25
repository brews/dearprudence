from functools import cache

from dearprudence.core import Cmip6Record
from dearprudence.errors import (
    Cmip6CatalogNoEntriesError,
    Cmip6CatalogMultipleEntriesError,
)


__all__ = ["cmip6_catalog_has", "esm_datastore"]


@cache
def esm_datastore(
    json_url: str = "https://storage.googleapis.com/cmip6/pangeo-cmip6-noQC.json",
):
    """
    Sugar to create an intake_esm.core.esm_datastore to pass into `in_cmip6_catalog`

    This is so we don't pummel public internet resources.

    Inputs
    ------
    json_url : str

    Returns
    -------
    intake_esm.core.esm_datastore
    """
    import intake

    return intake.open_esm_datastore(json_url)


def cmip6_catalog_has(x: Cmip6Record, datastore=None) -> bool:
    """Check that Cmip6Record has an entry in CMIP6-In-The-Cloud catalog

    This requires the ``intake-esm`` package to be installed.

    Inputs
    ------
    x : dearprudence.Cmip6Record
    datastore : intake_esm.core.esm_datastore or None, optional
        ESM datastore to search. If `None`, then read non-Quality Controled
        catalog for CMIP6. So we don't beat Public internet services to a pulp.

    Returns
    -------
    bool

    Raises
    ------
    Cmip6CatalogNoEntriesError
    Cmip6CatalogMultipleEntriesError

    See Also
    --------
    dearprudence.esm_datastore
    """
    if datastore is None:
        datastore = esm_datastore()

    cat = datastore.search(
        activity_id=x.activity_id,
        experiment_id=x.experiment_id,
        table_id=x.table_id,
        variable_id=x.variable_id,
        source_id=x.source_id,
        member_id=x.member_id,
        grid_label=x.grid_label,
        version=int(x.version),
    )

    n = len(cat)
    if n > 1:
        raise Cmip6CatalogMultipleEntriesError(f"Found {n} entries for {x}, expected 1")
    elif n < 1:
        raise Cmip6CatalogNoEntriesError(f"Found no entries for {x}, expected 1")

    return True
