import pandas as pd
import json

# -------------------------------
# CONFIGURATION
# -------------------------------

excel_file = "inventaire.xlsx"          # ton fichier Excel
output_json = "inventaire_flat.json"    # fichier JSON de sortie

# Mapping des colonnes Excel vers Dublin Core
mapping = {
    "unittitle": "dc:title",
    "relation_href_noticePuppetPlays": "dc:subject",
    "unitdate": "dc:date",
    "physdesc": "dc:description",
    "institution_unittitle": "dc:publisher",
    "dao_href_fileNakala": "dc:identifier",
    "physloc": "dc:source",
    "language_langcode": "dc:language",
    "unitid": "dc:relation",
    "geogname": "dc:coverage",
    "legalstatus": "dc:rights",
}

# Champs fixes à ajouter à chaque objet
fixed_fields = {
    "dc:format": "jpg",
    "dc:contributor": "ERC PuppetPlays project (diffusion through Nakala)",
    "dc:type": "Text"
}

# Colonnes Excel à fusionner pour dc:creator
creator_columns = ["persname", "identifier"]

# -------------------------------
# FONCTIONS UTILES
# -------------------------------

def clean_value(val):
    """Supprime espaces/tabs superflus et convertit en string."""
    if pd.isna(val):
        return None
    val = str(val).strip()
    return val if val else None

def parse_multi(val):
    """Sépare les valeurs multi-éléments par , ou ; en liste JSON"""
    val = clean_value(val)
    if not val:
        return None
    if ',' in val:
        return [v.strip() for v in val.split(',') if v.strip()]
    elif ';' in val:
        return [v.strip() for v in val.split(';') if v.strip()]
    else:
        return val

# -------------------------------
# SCRIPT
# -------------------------------

# Lire toutes les feuilles
sheets = pd.read_excel(excel_file, sheet_name=None)

all_items = []

for sheet_name, df in sheets.items():
    for _, row in df.iterrows():
        item = {}
        
        # Mapping des colonnes
        for excel_field, dc_field in mapping.items():
            if excel_field in row:
                val = parse_multi(row[excel_field])
                if val:
                    item[dc_field] = val
        
        # Fusion des colonnes pour creator
        creators = []
        for col in creator_columns:
            if col in row:
                val = clean_value(row[col])
                if val:
                    creators.append(val)
        if creators:
            item["dc:creator"] = " ; ".join(creators)
        
        # Ajouter les champs fixes
        item.update(fixed_fields)
        
        # Ne garder l'objet que si au moins un champ du mapping est présent
        if len(item) > len(fixed_fields):
            all_items.append(item)

# Sauvegarder en JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(all_items, f, ensure_ascii=False, indent=2)

print(f"JSON aplati généré avec succès dans {output_json}")
