"""A feature table to get the data set by the user."""

from sepal_ui import sepalwidgets as sw

from component import model as cmod
from component.message import cm


class TableIcon(sw.Icon):
    def __init__(self, gliph: str, id: int):
        """A custom icon that embeds the id of the feature."""
        super().__init__(
            children=[gliph],
            icon=True,
            small=True,
            attributes={"data-feature": id},
            style_="font: var(--fa-font-solid);",
        )


class FeatureRow(sw.Html):
    def __init__(self, model: cmod.FeatureModel, id: int):
        """A table row linked to the feature model. It allows to delete them."""
        # Get the model as a member
        self.model = model

        # Extract information from the model
        idx = self.model.get_index(id)
        type = self.model.types[idx]
        latitude = self.model.lats[idx]
        longitude = self.model.lngs[idx]

        # create the crud interface
        self.delete_btn = TableIcon("fa-solid fa-trash-can", id)

        # create the different cells
        td_list = [
            sw.Html(tag="td", children=[self.delete_btn]),
            sw.Html(tag="td", children=[type]),
            sw.Html(tag="td", children=[f"{longitude:.2f}"]),
            sw.Html(tag="td", children=[f"{latitude:.2f}"]),
        ]

        super().__init__(tag="tr", children=td_list)

        # add js behaviour
        self.delete_btn.on_event("click", self.on_delete)

    def on_delete(self, widget, *args) -> None:
        """remove the feature from the list."""
        self.model.remove_feature(widget.attributes["data-feature"])

        return


class FeatureTable(sw.SimpleTable):
    def __init__(self, model: cmod.FeatureModel) -> None:
        """A table to store the added features."""
        # save the model as member
        self.model = model

        # generate header
        header = sw.Html(
            tag="tr",
            children=[
                sw.Html(tag="th", children=[cm.feature_control.table.action]),
                sw.Html(tag="th", children=[cm.feature_control.table.type]),
                sw.Html(tag="th", children=[cm.feature_control.table.long]),
                sw.Html(tag="th", children=[cm.feature_control.table.lat]),
            ],
        )

        self.tbody = sw.Html(tag="tbody", children=[])
        self.set_rows()

        # create the table
        super().__init__(
            dense=True, children=[sw.Html(tag="thead", children=[header]), self.tbody]
        )

        # add js behaviour
        self.model.observe(self.set_rows, "updated")

    def set_rows(self, *args):
        """set the rows with respect to the current model state."""
        rows = []
        for idx in self.model.ids:
            rows.append(FeatureRow(self.model, idx))
        self.tbody.children = rows

        return
