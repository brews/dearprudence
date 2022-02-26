[![Test](https://github.com/brews/dearprudence/actions/workflows/test.yaml/badge.svg)](https://github.com/brews/dearprudence/actions/workflows/test.yaml)

# dearprudence
Internal Python library filled with sugar for swallowing downscalingCMIP6 parameter files.

*This is a working prototype under active development. It may break things or radically change without warning.*

## Examples

```python
import dearprudence


tasmax_spec = dearprudence.read_params("GFDL-ESM4-tasmax.yaml")

print(tasmax_spec[0].ssp)
# Cmip6Record(activity_id='ScenarioMIP',
#             experiment_id='ssp370', 
#             table_id='day', 
#             variable_id='tasmax', 
#             source_id='GFDL-ESM4', 
#             institution_id='NOAA-GFDL', 
#             member_id='r1i1p1f1',
#             grid_label='gr1',
#             version='20180701')

tasmax_spec[0].variable_id = "foobar"
dearprudence.write_params("pointlessly_modified.yaml", tasmax_spec)

if dearprudence.cmip6_catalog_has(tasmax_spec[0].ssp):
    print("Exists in CMIP6 In The Cloud!")
```

## Installation

Install with `pip` using:
```shell
pip install dearprudence
```

`dearprudence` requires Python > 3.9. No external packages are required. The `intake_esm` package may need to be installed to use `dearprudence.check_cmip6_catalog()`.

Install the unreleased bleeding-edge version of the package with:
```shell
pip install git+https://github.com/brews/dearprudence
```

## Support
Source code is available online at https://github.com/brews/dearprudence/. This software is Open Source and available under the Apache License, Version 2.0.

## Development

Please file bugs in the [bug tracker](https://github.com/brews/dearprudence/issues).

Want to contribute? Great! Fork the main branch and file a pull request when you're ready. Please be sure to write unit tests and follow [pep8](https://www.python.org/dev/peps/pep-0008/). Fork away!
