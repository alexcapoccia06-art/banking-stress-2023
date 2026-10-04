"""Check local source CSVs against the exact analysed files. No dependencies."""
from hashlib import sha256
from pathlib import Path

EXPECTED = {
    "49_Industry_Portfolios_Daily.csv":
        "63cc949d0335ff5416e598b0e10a0ef4d2a3d9afa7360433d9b5dafd50326499",
    "F-F_Research_Data_Factors_daily.csv":
        "c2dc30c9e89eeea05a689c81fb426f4d76711270733b3731997615cbdff5b247",
}


def main():
    data = Path(__file__).resolve().parents[1] / "data" / "raw"
    problems = 0
    for name, expected in EXPECTED.items():
        path = data / name
        if not path.is_file():
            print(f"MISSING: {name}. See data/README.md for source instructions.")
            problems += 1
            continue
        digest = sha256(path.read_bytes()).hexdigest()
        if digest == expected:
            print(f"MATCH: {name}")
        else:
            print(f"DIFFERENT: {name}\n  SHA-256: {digest}")
            print("  This is not the exact analysed file. A later vintage or byte-level")
            print("  formatting change may be responsible; published results may differ.")
            problems += 1
    if not problems:
        print("Both source files match the analysed vintage.")
    return int(problems > 0)


if __name__ == "__main__":
    raise SystemExit(main())
