import pandas as pd
import intxeger
from time import time
from xeger import Xeger

rows = []
for nb_samples, regex in [
    (100, "[a-zA-Z]+"),
    (100, "[0-9]{3}-[0-9]{3}-[0-9]{4}"),
    (1000, "[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}"),
]:
    row = {"N": nb_samples, "regex": regex}

    x = intxeger.build(regex)
    start = time()
    for _ in range(10):
        x.sample(nb_samples)
    row["intxeger (ms)"] = round((time() - start)*1000, 2)

    x = intxeger.build(regex)
    x = intxeger.optimize(x)
    start = time()
    for _ in range(10):
        x.sample(nb_samples)
    row["intxeger.optimize (ms)"] = round((time() - start)*1000, 2)

    x = Xeger()
    start = time()
    for _ in range(10):
        [x.xeger(regex) for _ in range(nb_samples)]
    row["xeger (ms)"] = round((time() - start) * 1000, 2)

    rows.append(row)
df = pd.DataFrame(rows, columns=["regex", "N", "xeger (ms)", "intxeger (ms)", "intxeger.optimize (ms)"])

print(df.to_markdown(index=False))
