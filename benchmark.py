import pandas as pd
import exrex
import intxeger
from time import time
from xeger import Xeger

rows = []
for nb_samples, regex in [
    (100, r"[a-zA-Z]+"),
    (100, r"[0-9]{3}-[0-9]{3}-[0-9]{4}"),
    (1000, r"[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}"),
    (1000, r"/json/([0-9]{4})/([a-z]{4})"),
]:
    row = {"N": nb_samples, "regex": regex}

    x = intxeger.build(regex)
    start = time()
    x.sample(nb_samples)
    row["intxeger"] = round((time() - start)*1000, 2)

    x = Xeger()
    start = time()
    [x.xeger(regex) for _ in range(nb_samples)]
    row["xeger"] = round((time() - start) * 1000, 2)

    start = time()
    [exrex.generate(regex) for _ in range(nb_samples)]
    row["exrex"] = round((time() - start) * 1000, 2)

    rows.append(row)
df = pd.DataFrame(rows, columns=["regex", "N", "xeger", "exrex", "intxeger"])

print(df.to_markdown(index=False))
