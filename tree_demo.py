import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree
import asyncio
from aiohttp import TCPConnector, ClientSession



def tree_base() -> Tree:
    data = [
        {
            "name": "flare",
            "children": [
                {
                    "name": "analytics",
                    "children": [
                        {
                            "name": "cluster",
                            "children": [
                                {"name": "AgglomerativeCluster", "value": 3938},
                                {"name": "CommunityStructure", "value": 3812},
                                {"name": "HierarchicalCluster", "value": 6714},
                                {"name": "MergeEdge", "value": 743}
                            ]
                        },
                        {
                            "name": "graph",
                            "children": [
                                {"name": "BetweennessCentrality", "value": 3534},
                                {"name": "SpanningTree", "value": 3416}
                            ]
                        },
                        {
                            "name": "optimization",
                            "children": [
                                {"name": "AspectRatioBanker", "value": 7074}
                            ]
                        }
                    ]
                },
                {
                    "name": "animate",
                    "children": [
                        {"name": "Easing", "value": 17010},
                        {"name": "FunctionSequence", "value": 5842},
                        {
                            "name": "interpolate",
                            "children": [
                                {"name": "ArrayInterpolator", "value": 1983},
                                {"name": "ColorInterpolator", "value": 2047},
                                {"name": "RectangleInterpolator", "value": 2042}
                            ]
                        },
                        {"name": "ISchedulable", "value": 1041},
                        {"name": "Parallel", "value": 5176},
                        {"name": "TransitionEvent", "value": 1116},
                        {"name": "Tween", "value": 6006}
                    ]
                },
                {
                    "name": "data",
                    "children": [
                        {
                            "name": "converters",
                            "children": [
                                {"name": "Converters", "value": 721},
                                {"name": "DelimitedTextConverter", "value": 4294},
                                {"name": "JSONConverter", "value": 2220}
                            ]
                        },
                        {"name": "DataField", "value": 1759},
                        {"name": "DataSchema", "value": 2165},
                        {"name": "DataUtil", "value": 3322}
                    ]
                },
                {
                    "name": "display",
                    "children": [
                        {"name": "DirtySprite", "value": 8833},
                        {"name": "LineSprite", "value": 1732},
                        {"name": "RectSprite", "value": 3623},
                        {"name": "TextSprite", "value": 10066}
                    ]
                },
                {
                    "name": "flex",
                    "children": [
                        {"name": "FlareVis", "value": 4116}
                    ]
                },
                {
                    "name": "physics",
                    "children": [
                        {"name": "DragForce", "value": 1082},
                        {"name": "GravityForce", "value": 1336},
                        {"name": "Spring", "value": 2213},
                        {"name": "SpringForce", "value": 1681}
                    ]
                },
                {
                    "name": "query",
                    "children": [
                        {"name": "AggregateExpression", "value": 1616},
                        {"name": "And", "value": 1027},
                        {"name": "Arithmetic", "value": 3891},
                        {"name": "Average", "value": 891},

                        {"name": "Maximum", "value": 843},
                        {
                            "name": "methods",
                            "children": [
                                {"name": "add", "value": 593},
                                {"name": "and", "value": 330},
                                {"name": "-", "value": 264}
                            ]
                        },
                        {"name": "Minimum", "value": 843},
                        {"name": "Not", "value": 1554},
                        {"name": "Or", "value": 970},
                        {"name": "Variance", "value": 1876},
                        {"name": "Xor", "value": 1101}
                    ]
                },
                {
                    "name": "scale",
                    "children": [
                        {"name": "IScaleMap", "value": 2105},
                        {"name": "LinearScale", "value": 1316},
                        {"name": "TimeScale", "value": 5833}
                    ]
                },

                {
                    "name": "vis",
                    "children": [
                        {
                            "name": "axis",
                            "children": [
                                {"name": "Axes", "value": 1302},
                                {"name": "CartesianAxes", "value": 6703}
                            ]
                        },
                        {
                            "name": "controls",
                            "children": [
                                {"name": "AnchorControl", "value": 2138},
                                {"name": "ClickControl", "value": 3824},
                                {"name": "SelectionControl", "value": 7862},
                                {"name": "TooltipControl", "value": 8435}
                            ]
                        },
                        {
                            "name": "data",
                            "children": [
                                {"name": "Data", "value": 20544},
                                {"name": "EdgeSprite", "value": 3301},
                                {"name": "NodeSprite", "value": 19382},
                                {
                                    "name": "render",
                                    "children": [
                                        {"name": "ArrowType", "value": 698},
                                        {"name": "EdgeRenderer", "value": 5569},
                                        {"name": "IRenderer", "value": 353},
                                        {"name": "ShapeRenderer", "value": 2247}
                                    ]
                                },
                                {"name": "ScaleBinding", "value": 11275},
                                {"name": "Tree", "value": 7147},
                                {"name": "TreeBuilder", "value": 9930}
                            ]
                        },
                        {
                            "name": "events",
                            "children": [
                                {"name": "DataEvent", "value": 2313},
                                {"name": "VisualizationEvent", "value": 1117}
                            ]
                        },
                        {
                            "name": "legend",
                            "children": [
                                {"name": "Legend", "value": 20859},
                                {"name": "LegendItem", "value": 4614},
                                {"name": "LegendRange", "value": 10530}
                            ]
                        },
                        {
                            "name": "operator",
                            "children": [
                                {
                                    "name": "distortion",
                                    "children": [
                                        {"name": "BifocalDistortion", "value": 4461},
                                        {"name": "Distortion", "value": 6314},
                                        {"name": "FisheyeDistortion", "value": 3444}
                                    ]
                                },
                                {
                                    "name": "encoder",
                                    "children": [
                                        {"name": "ColorEncoder", "value": 3179},
                                        {"name": "Encoder", "value": 4060},
                                        {"name": "SizeEncoder", "value": 1830}
                                    ]
                                },
                                {
                                    "name": "filter",
                                    "children": [
                                        {"name": "FisheyeTreeFilter", "value": 5219},
                                        {"name": "GraphDistanceFilter", "value": 3165},
                                        {"name": "VisibilityFilter", "value": 3509}
                                    ]
                                },
                                {"name": "IOperator", "value": 1286},
                                {
                                    "name": "label",
                                    "children": [
                                        {"name": "Labeler", "value": 9956},
                                        {"name": "RadialLabeler", "value": 3899},
                                        {"name": "StackedAreaLabeler", "value": 3202}
                                    ]
                                },
                                {
                                    "name": "layout",
                                    "children": [
                                        {"name": "AxisLayout", "value": 6725},
                                        {"name": "BundledEdgeRouter", "value": 3727},
                                        {"name": "CircleLayout", "value": 9317},
                                        {"name": "TreeMapLayout", "value": 9191}
                                    ]
                                },
                                {"name": "Operator", "value": 2490},
                                {"name": "OperatorList", "value": 5248},
                                {"name": "SortOperator", "value": 2023}
                            ]
                        },
                        {"name": "Visualization", "value": 16540}
                    ]
                }
            ]
        }

    ]
    c = (
        Tree()
        .add("", data,collapse_interval=2,is_expand_and_collapse=True,pos_bottom=100,pos_right=100)
        .set_global_opts(title_opts=opts.TitleOpts(title="树形图展示"))
    )
    return c
tree_base().render()