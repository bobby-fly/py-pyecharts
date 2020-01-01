# py-pyecharts
Using data analysis charts at work

install setting


windows 
Official reference link

https://github.com/pyecharts/pyecharts
pip install pyecharts
pip install pyecharts_snapshot

v1.0版本:

from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Bar3D,Pie,Grid
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import  Line

