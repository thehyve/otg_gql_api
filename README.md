# OpenTargets Genetics GraphQL API

## How to scan locus plot data

```python
from otg_scan_all_gecko import GeckoScanner

scanner = GeckoScanner('http://genetics-api.opentargets.io/graphql')

for gecko in scanner.scan_all_gecko():
    ...
```

## Print all variants, genes and studies

Below script scan all locus plot data and collects unique variants, genes and studies.
It outputs each line in `tsv` format as following: `study\tGCST003044`

```
    python print_all_vgs.py > output.tsv
```
