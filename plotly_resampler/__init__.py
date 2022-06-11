"""**plotly\_resampler**: visualizing large sequences."""

from .aggregation import (
    LTTB,
    EfficientLTTB,
    EveryNthPoint,
    FuncAggregator,
    MinMaxOverlapAggregator,
)
from .figure_resampler import FigureResampler, FigureWidgetResampler

__docformat__ = "numpy"
__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"
__version__ = "0.6.4.2"

__all__ = [
    "__version__",
    "FigureResampler",
    "FigureWidgetResampler",
    "EfficientLTTB",
    "MinMaxOverlapAggregator",
    "LTTB",
    "EveryNthPoint",
    "FuncAggregator",
]


try:  # Enable ipywidgets on google colab!
    import sys

    if "google.colab" in sys.modules:
        from google.colab import output

        output.enable_custom_widget_manager()
except ImportError:
    pass
