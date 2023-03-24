"""computation parmameters."""

from component.message import cm

bin_items = ["TILE100", "TILE20", "TILE10", "ADMIN0", "ADMIN1", "ADMIN2"]

gaul_codes = [
    "68",  # Democratic republic of the Congo
    "59",  # congo
    "89",  # gabon
    "45",  # cameroon
    "76",  # equatorial guinea
    "49",  # Central African Republic
]

# TODO UPDATE
# at the moment we use the example fragmentation map
viz = {
    "min": 1,
    "max": 6,
    "palette": ["#964B00", "#FFFF00", "#FFA500", "#90EE90", "#00FF00", "#D3D3D3"],
}
"viz parameters of the driver index"

drivers = [
    {"text": cm.feature_control.drivers.INFRA, "value": "INFRA"},
    {"text": cm.feature_control.drivers.URBAN, "value": "URBAN"},
    {"text": cm.feature_control.drivers.ART_AGR, "value": "ART_AGR"},
    {"text": cm.feature_control.drivers.INDUS_AGR, "value": "INDUS_AGR"},
    {"text": cm.feature_control.drivers.ART_FOR, "value": "ART_FOR"},
    {"text": cm.feature_control.drivers.INDUS_FOR, "value": "INDUS_FOR"},
    {"text": cm.feature_control.drivers.ART_MIN, "value": "ART_MIN"},
    {"text": cm.feature_control.drivers.INDUS_MIN, "value": "INDUS_MIN"},
    {"text": cm.feature_control.drivers.OTHER, "value": "OTHER"},
    {"text": cm.feature_control.drivers.NONE, "value": "NONE"},
]

driver_colors = {
    "NONE": ["white", "#FBFBFB"],
    "URBAN": ["gray", "#575757"],
    "INFRA": ["lightgray", "#A3A3A3"],
    "ART_AGR": ["lightred", "#FF8E7F"],
    "INDUS_AGR": ["red", "#D63E2A"],
    "ART_FOR": ["lightgreen", "#BBF970"],
    "INDUS_FOR": ["green", "#72B026"],
    "ART_MIN": ["lightblue", "#8ADAFF"],
    "INDUS_MIN": ["blue", "#38AADD"],
    "OTHER": ["purple", "#D252B9"],
}
