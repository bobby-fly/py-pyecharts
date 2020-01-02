import json
import os

from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.faker import Collector
C = Collector()

def graph_weibo() -> Graph:
    with open(os.path.join("fixtures", r"C:\Users\jihuo369\PycharmProjects\work1\weibo.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
        print(j)
        nodes, links, categories, cont, mid, userl = j
    c = (
        Graph()
        .add(
            "",
            nodes,
            links,
            categories,
            repulsion=50,
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title="Graph-微博转发关系图"),
        )
    )
    return c
graph_weibo().render()