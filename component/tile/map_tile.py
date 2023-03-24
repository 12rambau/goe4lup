"""The map displayed in the map application."""

from sepal_ui import aoi
from sepal_ui import mapping as sm
from sepal_ui import sepalwidgets as sw

from component import model as cmod

from .aoi_control import AoiControl
from .feature_control import FeatureControl


class MapTile(sw.Tile):
    def __init__(self):
        """Specific Map integrating all the widget components.

        Use this map to gather all your widget and place them on it. It will reduce the amount of work to perform in the notebook
        """
        # create a map
        self.m = sm.SepalMap(zoom=3)  # to be visible on 4k screens
        self.m.add_control(
            sm.FullScreenControl(
                self.m, fullscreen=True, fullapp=True, position="topright"
            )
        )

        # creat the models
        self.aoi_model = aoi.AoiModel()
        self.feature_model = cmod.FeatureModel()

        # create the controls
        aoi_control = AoiControl(self.m, self.aoi_model, position="bottomright")
        feature_control = FeatureControl(
            self.m, self.feature_model, position="bottomright"
        )

        # add them on the map
        self.m.add_control(feature_control)
        self.m.add_control(aoi_control)

        # create the tile
        super().__init__("map_tile", "", [self.m])
