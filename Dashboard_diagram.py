from pyecharts import options as opts
from pyecharts.charts import Gauge, Page


def gauge_base() -> Gauge:
    c = (
        Gauge()
        .add("", [("完成率", 66.6)],
            axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
            color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width = 30,
            )
    ),
             )
        .set_global_opts(title_opts=opts.TitleOpts(title="仪表盘实例"))
    )
    return c
gauge_base().render()