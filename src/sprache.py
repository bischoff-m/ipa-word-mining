# %%
from pathlib import Path
import pandas as pd
from IPython.display import display

if Path("de.csv").exists():
    df = pd.read_csv("de.csv")
else:
    with open("de.txt", "r", encoding="utf-8") as file:
        de = file.read().splitlines()

    word, ipa = [], []
    for line in de:
        w, i = line.split("\t")
        for j in i.split(","):
            word.append(w)
            ipa.append(j.strip())

    df = pd.DataFrame({"word": word, "ipa": ipa})
    df.to_csv("de.csv", index=False)

result = df[
    df["ipa"].str.endswith("ç/")
    & ~df["word"].str.endswith("ig").astype("bool")
    & ~df["word"].str.endswith("ich").astype("bool")
    & ~df["ipa"].str.endswith("ʁç/").astype("bool")
]
result.to_csv("query.csv", index=False)
display(result)
