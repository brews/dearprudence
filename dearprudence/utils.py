__all__ = ["in_cmip6_catalog", "esm_datastore"]


def esm_datastore(json_url="https://storage.googleapis.com/cmip6/pangeo-cmip6-noQC.json"):
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


def in_cmip6_catalog(x, datastore=None):
    """Check that Cmip6Record has an entry in CMIP6-In-The-Cloud catalog

    This requires the ``intake-esm`` package to be installed.

    Inputs
    ------
    x : dearprudence.Cmip6Record
    datastore : intake_esm.core.esm_datastore or None, optional
        ESM datastore to search. If `None`, then read non-Quality Controled
        catalog for CMIP6. Recommend passing in an existing Datastore so
        we don't beat Public internet services to a pulp.

    Returns
    -------
    bool

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
    # d = cat.to_dataset_dict(progressbar=False)
    # k = list(d.keys())
    if len(cat) != 1:
        # raise ValueError("catalog does not have one entry, reconsider input IDs so only one entry")
        return False
    return True
