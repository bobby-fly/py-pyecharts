from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType




bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["华为", "OPPO", "VIVO"])
    .add_yaxis("华为", [150, 120, 360, 100, 75, 90, 80, 89, 95, 99, 119, 128])
    .add_yaxis("OPPO", [120, 60, 45, 120, 135, 66, 114, 98, 117, 118, 90, 125])
    .add_yaxis("VIVO", [50, 20, 76, 100, 75, 90, 75, 68, 89, 95, 112, 116, 121])
    .add_xaxis(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
    .set_global_opts(title_opts=opts.TitleOpts(title="某电商销售统计", subtitle="手机"))
)
bar.render()