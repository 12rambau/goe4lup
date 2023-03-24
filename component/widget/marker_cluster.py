"""Custom implementation of the marker cluster to hide it at once."""

from ipyleaflet import MarkerCluster
from traitlets import Bool, observe


class MarkerCluster(MarkerCluster):

    visible = Bool(True).tag(sync=True)

    @observe("visible")
    def toggle_markers(self, change):
        """change the marker value according to the cluster viz."""
        for marker in self.markers:
            marker.visible = self.visible
