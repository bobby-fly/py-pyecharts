from pyecharts import options as opts
from pyecharts.charts import Liquid, Page
from pyecharts.globals import SymbolType


def liquid_base() -> Liquid:
    c = (
        Liquid()
        .add(
            "lq",
            [0.6, 0.7],
            color="#67e0e3",
            #不要边框
            is_outline_show=False
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    )
    return c
liquid_base().render()