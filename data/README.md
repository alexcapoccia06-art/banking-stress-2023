# Data sources and provenance

The analysis uses two files from the Kenneth French Data Library. Raw CSVs are not included in this repository; place your local copies in `data/raw` before running the notebook.

| Expected local filename | Source and section used |
|---|---|
| `49_Industry_Portfolios_Daily.csv` | [49 Industry Portfolios](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_49_ind_port.html), daily **value-weighted** returns |
| `F-F_Research_Data_Factors_daily.csv` | [Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), **Fama/French 3 Factors, Daily, CSV**; retain only `Mkt-RF` and `RF` |

Download and extract the daily CSV archives. Keep the original file contents, including the introductory lines and table headers: the notebook uses these to locate the intended sections. Remove upload suffixes such as `(2)` from the filenames only.

## Exact analysed files

Both supplied source files identify the **202608 CRSP database vintage**. Newly downloaded files may have revised historical observations. Exact reproduction of the published numbers requires the same inputs; the source website does not necessarily serve this older vintage as its current download.

SHA-256 fingerprints:

```text
49_Industry_Portfolios_Daily.csv
63cc949d0335ff5416e598b0e10a0ef4d2a3d9afa7360433d9b5dafd50326499

F-F_Research_Data_Factors_daily.csv
c2dc30c9e89eeea05a689c81fb426f4d76711270733b3731997615cbdff5b247
```

Run `python scripts/check_data.py` from the repository root to verify local copies. A byte-level mismatch can reflect a newer vintage or a change in file encoding or line endings; it does not by itself diagnose which observations changed.

## Preparation and windows

The notebook selects the value-weighted industry table, treats `-99.99` and `-999` as missing, parses dates, and divides source percentages by 100. The market factor `Mkt-RF` is already an excess return; the risk-free return is subtracted from industry returns when fitting the market models.

| Use | Dates | Observations |
|---|---|---:|
| Benchmark estimation | 3 January–30 December 2022 | 251 |
| Monitoring | 3 January–28 April 2023 | 81 |
| Pre-stress descriptive window | 3 January–7 March 2023 | 44 |
| Stress descriptive window | 8–31 March 2023 | 18 |
| April descriptive window | 3–28 April 2023 | 19 |
| Monthly networks | February / March / April 2023 | 19 / 23 / 19 |

The selected network uses `Banks`, `Insur`, `RlEst`, `Fin`, `Softw`, `Chips`, `Util`, `Oil`, `Mach`, `Trans`, `Rtail` and `Food`. Source portfolio classifications determine membership. `Chips` should not be interpreted as a pure semiconductor portfolio, nor `Fin` as the entire financial sector.

The retained sample contains 332 common dates with no missing values in the selected series. Later data revisions must be checked again. Cite the French Data Library when using its data; the project's authorship does not extend to the source datasets.
