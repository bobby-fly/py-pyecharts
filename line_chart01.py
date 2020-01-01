from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Bar3D,Pie,Grid
from pyecharts.faker import Faker
#引入配置项入口
from pyecharts import options as opts
from pyecharts.charts import  Line


line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
    # .add_xaxis(['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子'])
    .add_xaxis(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
    .add_yaxis('商家A',[5,20,36,10,75,90,55,20,36,10,75,90])
    .add_yaxis('商家B',[15,6,45,20,35,66,41,34,54,35,47,48])
    .add_yaxis('商家C',[11,34,44,45,67,38,32,46,44,45,67,38])
    .set_global_opts(title_opts=opts.TitleOpts(title="xx公司",subtitle="某商品统计"))

)
# line.render()
line.render()