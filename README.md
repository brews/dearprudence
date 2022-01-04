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

Install from the bleeding edge with `pip`:
```shell
pip install git+https://github.com/brews/dearprudence
```

`dearprudence` requires Python > 3.7. No external packages are required. `intake_gsm` may need to be installed for `dearprudence.check_cmip6_catalog()`.

## Support
Source code is available online at https://github.com/brews/dearprudence/. This software is Open Source and available under the Apache License, Version 2.0.

## Development

Please file bugs in the [bug
tracker](https://github.com/brews/dearprudence/issues).

Want to contribute? Great! We’re following please follow [pep8](https://www.python.org/dev/peps/pep-0008/) and write unit tests. Fork away.
