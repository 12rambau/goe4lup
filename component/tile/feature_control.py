"""Set the specific feature control."""

from ipyleaflet import AwesomeIcon, Marker
from sepal_ui import mapping as sm
from sepal_ui import sepalwidgets as sw
from traitlets import Bool

from component import model as cmod
from component import widget as cw
from component.message import cm


class FeatureView(sw.Tile):

    activated = Bool(False).tag(sync=True)
    "signal the rest of the application that the menu is activated"

    marker_cluster = cw.MarkerCluster()
    "a marker cluster to show the identified points"

    def __init__(self, model: cmod.FeatureModel, m: sm.SepalMap):
        """Create a selector to add driver feature to the map."""
        # set the model as member
        self.model = model
        self.m = m

        # create a table to display the existing features
        table = cw.FeatureTable(self.model)

        # add the marker cluster to the map
        # and hide it
        self.marker_cluster.visible = False
        self.m.add(self.marker_cluster)

        super().__init__("nested", cm.feature_control.title, [table])

        # add js behavior
        self.m.on_interaction(self.read_data)

    def read_data(self, **kwargs) -> None:
        """Read the data when the map is clicked with the vinspector activated."""
        # check if the feature selector is active
        clicked = kwargs.get("type") == "click"
        if not (clicked and self.activated):
            return

        # get the coordinates as (x, y)
        lng, lat = [c for c in reversed(kwargs.get("coordinates"))]

        # add the marker to the layer
        icon = AwesomeIcon(marker_color="white")
        marker = Marker(icon=icon, location=(lat, lng))
        self.marker_cluster.markers = (*self.marker_cluster.markers, marker)
        marker.idx = self.model.updated  # use the updated var as an index value.

        # add the partial data to the model
        # it will trigger the rebuild of the table
        self.model.add_feature(lng, lat)


class FeatureControl(sm.MenuControl):
    def __init__(self, m: sm.SepalMap, model: cmod.FeatureModel, **kwargs):
        """Custom menu control dedicated to feature selection."""
        self.view = FeatureView(model, m)
        super().__init__(
            icon_content="fa-solid fa-cogs", card_content=self.view, m=m, **kwargs
        )

        # add js behavior
        self.menu.observe(self.toggle_cursor, "v_model")

    def toggle_cursor(self, *args) -> None:
        """Toggle the cursor and marker display.

        Toggle the cursor on the map to notify to the user that the point
        mode is activated. also activate previous markers if features already exist
        """
        cursors = [{"cursor": "grab"}, {"cursor": "crosshair"}]
        self.m.default_style = cursors[self.menu.v_model]
        self.view.activated = self.menu.v_model
        self.view.marker_cluster.visible = self.menu.v_model
