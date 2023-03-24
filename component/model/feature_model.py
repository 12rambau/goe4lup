"""model to store drawn features."""
import geopandas as gpd
from sepal_ui import model
from traitlets import Dict, Int, List


class FeatureModel(model.Model):

    types = List([]).tag(sync=True)
    ids = List([]).tag(sync=True)
    lats = List([]).tag(sync=True)
    lngs = List([]).tag(sync=True)

    geo_interface = Dict({"type": "FeatureCollection", "features": []}).tag(sync=True)

    updated = Int(0).tag(sync=True)

    def get_features(self) -> gpd.GeoDataFrame:
        """retreive the geointerface as a geodataframe."""
        data = {
            "idx": self.ids,
            "type": self.types,
            "lng": self.lngs,
            "lat": self.lats,
            "geometry": gpd.points_from_xy(self.lngs, self.lats),
        }

        return gpd.GeoDataFrame(data, crs=4326)

    def get_index(self, id: int):
        """return the index of the ID in the lists."""
        return next(i for i, v in enumerate(self.ids) if v == id)

    def add_feature(self, lng: float, lat: float) -> None:
        """add a feature to the geointerface."""
        self.lats.append(lat)
        self.lngs.append(lng)
        self.ids.append(self.updated)
        self.types.append("NONE")

        self.updated += 1

        return

    def remove_feature(self, id: int) -> None:
        """remove a feature from the geo_interface."""
        index = self.get_index(id)

        self.lats.pop(index)
        self.lngs.pop(index)
        self.ids.pop(index)
        self.types.pop(index)

        self.updated += 1

        return
