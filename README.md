### PuppetPlays Anthologie xml - Inventaire Dublin Core

Ici se trouvent toutes les transcriptions encodées en XML TEI de l'anthologie du projet **ERC PuppetPlays**. Ces fichiers sont aussi disponibles dans la collection Nakala : https://nakala.fr/collection/10.34847/nkl.1ded03r2
Ce dépôt contient aussi l’inventaire des textes de théâtre numérisés par le projet **ERC PuppetPlays**, ainsi que le script Python permettant de générer un fichier JSON conforme au Dublin Core à partir des fichiers Excel.
Ce projet est financé par le Programme de recherche et d'innovation Horizon 2020 de l'Union Européenne, dans le cadre du Grant Agreement ERC 835193.
Toutes les ressources de cette branche sont disponibles sous la licence Etalab : https://github.com/etalab/licence-ouverte/blob/master/open-licence.md. 

---

## Contenu du dépôt

| Fichier | Description |
|---------|-------------|
| `inventaire.xlsx` | Fichier Excel principal contenant les textes de théâtre avec toutes les métadonnées. Chaque feuille correspond à une partie différente de l’inventaire. |
| `inventaire_mapping.xlsx` | Fichier Excel qui contient le **mapping des colonnes Excel vers les champs Dublin Core**. Utilisé par le script pour renommer et transformer les colonnes lors de la conversion. |
| `inventaire_flat.json` | Fichier JSON généré par le script Python. Il contient **tous les enregistrements de toutes les feuilles** Excel fusionnés en une seule liste, avec les champs Dublin Core standard et les champs fixes ajoutés (`dc:format`, `dc:contributor`, `dc:type`). |
| `convert_excel_to_json.py` | Script Python principal qui :<br>• lit toutes les feuilles de `inventaire.xlsx`<br>• applique le mapping depuis `inventaire_mapping.xlsx`<br>• fusionne les colonnes `persname` et `identifier` en `dc:creator`<br>• transforme les colonnes multi-valeurs en listes JSON<br>• ajoute les champs fixes (`dc:format`, `dc:contributor`, `dc:type`)<br>• génère `inventaire_flat.json`. |

---

## Dépendances

Le script Python nécessite les packages suivants :

- `pandas`
- `openpyxl`

Pour les installer, exécuter :

```bash
pip install pandas openpyxl
