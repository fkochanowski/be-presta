import pandas as pd

kategorie = ["lampy wiszące", "lampy stojące",  "lampy sufitowe",  "kinkiety"]
df = pd.DataFrame(
    {
        "Nazwa": kategorie,
        "Główna kategoria": [0, 0, 0, 0]
    }
)
nazwy_podkategorii = ["designerskie", "industrialne", "nowoczesne", "szklane"]

b = []
for cat in kategorie:
    b += [cat] * 4

podkategorie = pd.DataFrame(
    {
        "Nazwa": nazwy_podkategorii * 4,
        "Główna kategoria": b
    }
)

df.to_csv('categories.csv', sep=";")
podkategorie.to_csv('subcategories.csv', sep=";")

