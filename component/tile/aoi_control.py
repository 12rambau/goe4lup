"""Set the specific AOI MenuControl."""

from sepal_ui import aoi
from sepal_ui import color as sc
from sepal_ui import mapping as sm

from component import parameter as cp
from component.message import cm


class AoiView(aoi.AoiView):
    def __init__(self, map_: sm.SepalMap, model: aoi.AoiModel, **kwargs):
        """Extend the aoi_view component from sepal_ui mapping to add.

        map_: the map to draw on
        aoi_model: the shared aoi_model
        """
        style = {
            "stroke": True,
            "color": sc.primary,
            "weight": 2,
            "opacity": 1,
            "fill": False,
        }

        # limit the interaction to 3 types:
        # custom asset
        # country
        # administrative level 1
        methods = ["ADMIN0", "ADMIN1", "ASSET"]

        super().__init__(
            map_=map_, methods=methods, model=model, map_style=style, **kwargs
        )

        # change the name of the custom asset to "subregional"
        tmp_item = self.w_method.items.copy()
        for i in tmp_item:
            if "value" in i:
                if i["value"] == "ASSET":
                    i["text"] = cm.aoi_control.subregion.capitalize()
                    break

        # forced to empty the item list to trigger the event
        self.w_method.items = []
        self.w_method.items = tmp_item

        # make the asset selector readonly
        self.w_asset.readonly = True

        # only use the countries that are in the CAFI project
        tmp_item = self.w_admin_0.items.copy()
        tmp_item = [i for i in tmp_item if i["value"] in cp.gaul_codes]
        self.w_admin_0.items = []
        self.w_admin_0.items = tmp_item

        # add js behaviour
        self.w_method.observe(self.select_subregional, "v_model")

        # select subregional by default
        self.w_method.v_model = "ASSET"

    def select_subregional(self, *args) -> None:
        """select the subregional asset and hide the asset selector."""
        if self.w_method.v_model is None:
            return

        if self.w_method.v_model == "ASSET":
            self.w_asset.hide()
            self.w_asset.w_file.v_model = "projects/ee-geo4lup/assets/cafi_LSIB"

        return


class AoiControl(sm.MenuControl):
    def __init__(self, map_: sm.SepalMap, aoi_model: aoi.AoiModel, **kwargs):
        """The custom AOI control.

        map_: the map to draw on
        aoi_model: the shared aoi_model
        """
        self.view = AoiView(model=aoi_model, map_=map_)
        self.view.elevation = False
        self.view.class_list.add("ma-5")

        # create the control
        super().__init__(
            "fa-solid fa-map-marker-alt",
            self.view,
            m=map_,
            card_title=cm.aoi_control.title,
            **kwargs
        )
