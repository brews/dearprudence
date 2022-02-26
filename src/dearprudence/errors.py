"""
Custom Exceptions
"""


class Cmip6CatalogError(Exception):
    """Raised when there has been an error with CMIP6 catalog entries"""

    pass


class Cmip6CatalogMultipleEntriesError(Cmip6CatalogError):
    """Raised when Cmip6Record has multiple CMIP6 catalog entries"""

    pass


class Cmip6CatalogNoEntriesError(Cmip6CatalogError):
    """Raised when Cmip6Record has no matching CMIP6 catalog entries"""

    pass


class ParameterFileValidationError(Exception):
    """Raised when run parameters do not validate"""

    pass


class ParameterFileValidationWarning(UserWarning):
    """Warning used when run parameters do not validate"""

    pass
