# coding: utf-8

from io import BytesIO
import folium
from folium.features import DivIcon
import geopandas as gpd
from IPython.display import display
import os
import pandas as pd
from urllib.request import urlopen
from zipfile import ZipFile


def download_unzip(zipurl, destination):
    """Download zipfile from URL and extract it to destination"""
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(destination)


class ArbreStras:

    URL_PREFIX = "https://www.strasbourg.eu/documents/976405/"
    STRASBOURG_COORD = (48.58, 7.75)
    ARBRES_ZIP = URL_PREFIX + "1168331/CUS_CUS_DEPN_ARBR.zip"
    ARBRES_CSV = "arbres/CUS_CUS_DEPN_ARBR.csv"
    QUARTIERS_ZIP = URL_PREFIX + "1168339/CUS_CUS_DUAH_QUART.zip"
    QUARTIERS_SHP = "quartiers/SHP/Quartiers_Strasbourg_15.shp"

    def __init__(self, force_download=False):
        """On crée les data et la carte"""
        self.force_download = force_download
        self._load_arbres()
        self._load_quartiers()

    def _load_arbres(self):
        if self.force_download or not os.path.isfile(self.ARBRES_CSV):
            download_unzip(self.ARBRES_ZIP, "arbres")

        arbres_all = pd.read_csv(self.ARBRES_CSV,
                                 encoding='latin',  # Pour prendre en compte l'encoding qui n'est pas utf-8
                                 delimiter=";",  # Le caractère séparateur des colonnes
                                 decimal=',')  # Pour convertir les décimaux utilisant la notation ,

        self.arbres = arbres_all[arbres_all['point vert VILLE'] == "STRASBOURG"]
        self.arbres = self.arbres.dropna(axis=0, how='any')
        self.essences = set(self.arbres['Libellé_Essence'])
        self.genre = set([essence.split()[0] for essence in self.essences])
        # On construit le dico {genre: essence1, essence2, etc.}
        self.essences_dict = {}
        for essence in self.essences:
            essence_splitted = essence.split()
            genre = essence_splitted[0]
            espece = ' '.join(essence_splitted[1:])
            try:
                especes = self.essences_dict[genre]
                especes.append(espece)
            except KeyError:
                especes = [espece]
                self.essences_dict.update({genre: especes})

    def _load_quartiers(self):

        if self.force_download or not os.path.isfile(self.QUARTIERS_SHP):
            download_unzip(self.QUARTIERS_ZIP, "quartiers")

        self.quartiers = gpd.read_file(self.QUARTIERS_SHP)
        self.quartiers["QUARTIER"] = self.quartiers["QUARTIER"].str.lower()
        self.quartiers["QUARTIER"] = self.quartiers["QUARTIER"].str.replace('_', ' ')

        convertion_dict = {"CENTRE": "centre ville",
                           ("BOURSE", "ESPLANADE", "KRUTENAU"): "bourse esplanade krutenau",
                           ("ORANGERIE", "CONSEIL-XV"): "orangerie conseil des xv",
                           ("GARE", "TRIBUNAL"): "gare tribunal",
                           ("HAUTEPIERRE", "POTERIE"): "hautepierre poteries",
                           "MUSAU": "NEUDORF",
                           "STOCKFELD": "NEUHOF2",
                           "PLAINE DES BOUCHERS": "MEINAU",
                           "POLYGONE": "NEUHOF",
                           "PORTE DE SCHIRMECK": "ELSAU",
                           ("ROBERTSAU", "WACKEN"): "ROBERTSAU WACKEN"}

        for k, v in convertion_dict.items():
            self.arbres['Point vert Quartier usuel'] = self.arbres['Point vert Quartier usuel'].replace(to_replace=k,
                                                                                                        value=v)
        self.arbres['Point vert Quartier usuel'] = self.arbres['Point vert Quartier usuel'].str.lower()

        self.quartiers['coords'] = self.quartiers['geometry'].to_crs(epsg='4326').apply(lambda x: x.centroid.coords[:])
        self.quartiers['coords'] = [coords[0] for coords in self.quartiers['coords']]

    def _create_map(self, data, legende):
        # On crée une carte initialement centrée sur Strasbourg
        fmap = folium.Map(self.STRASBOURG_COORD, zoom_start=11, tiles='cartodbpositron')

        # On ajoute les données des quartiers
        folium.GeoJson(self.quartiers).add_to(fmap)

        fmap.choropleth(geo_data=self.quartiers,
                        data=data,
                        key_on='feature.properties.QUARTIER',
                        fill_color='YlGn',
                        fill_opacity=0.5,
                        line_opacity=0.2,
                        legend_name=legende)

        for idx, row in self.quartiers.iterrows():
                nom = '<br>'.join(row["QUARTIER"].title().split())
                html_div = f'<div style="font-size: 7pt">{nom}</div>'
                folium.map.Marker((row['coords'][1], row['coords'][0]),
                                  icon=DivIcon(icon_size=(150, 36),
                                               icon_anchor=(0, 0),
                                               html=html_div)
                                  ).add_to(fmap)
        display(fmap)

    def plot(self, essence="tous", representation="densité"):
        """Trace la représentation géographique par quartier"""

        if essence == 'tous':
            libelle = ''
            df = self.arbres
            ds = self.arbres['Point vert Quartier usuel']
        else:
            libelle = "de " + essence.replace(r"'", r"\'")
            df = self.arbres[self.arbres['Libellé_Essence'] == essence]
            ds = df['Point vert Quartier usuel']
        hauteurs = df.groupby(['Point vert Quartier usuel'])['Hauteur arbre']

        if representation == "densité":
            data_count = ds.value_counts()
            aires = self.quartiers.area
            aires.index = self.quartiers["QUARTIER"]
            ds_plot = data_count / aires * 10000
            legende = r"Nombre {} par hectare".format(libelle)
        elif representation == "nombre":
            ds_plot = ds.value_counts()
            legende = "Nombre " + libelle
        elif representation == "hauteur moyenne":
            ds_plot = hauteurs.mean()
            legende = "Hauteur moyenne [m] " + libelle
        else:
            raise Exception(f"représentation inconnue: {representation}")

        ds_plot = ds_plot.fillna(0)
        self._create_map(ds_plot, legende)


if __name__ == '__main__':
    stras_arbres = ArbreStras()
    stras_arbres.plot()
    stras_arbres.plot(essence="tous", representation="nombre")
    stras_arbres.plot(essence='Abies grandis')
    stras_arbres.plot(essence='Abies grandis', representation="densité")

