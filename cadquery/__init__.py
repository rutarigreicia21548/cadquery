"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It provides a clean, fluent API for creating complex shapes
using OpenCASCADE Technology (OCCT) as the underlying geometry kernel.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)
"""

from .cq import (
    CQContext,
    CQ,
    Workplane,
)
from .occ_impl.geom import Vector, Matrix, Plane, BoundBox
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
    CompSolid,
)
from .occ_impl.exporters import exporters
from .assembly import Assembly, Constraint
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    RadiusNthSelector,
    CenterNthSelector,
    DirectionMinMaxSelector,
    BinarySelector,
    AndSelector,
    SumSelector,
    SubtractSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch

# Version information
__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache-2.0"

__all__ = [
    # Core workplane
    "CQContext",
    "CQ",
    "Workplane",
    # Geometry primitives
    "Vector",
    "Matrix",
    "Plane",
    "BoundBox",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "CompSolid",
    # Assembly
    "Assembly",
    "Constraint",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "DirectionMinMaxSelector",
    "BinarySelector",
    "AndSelector",
    "SumSelector",
    "SubtractSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Sketch
    "Sketch",
    # Exporters
    "exporters",
]
