"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It provides a clean, fluent API for creating complex shapes
using OpenCASCADE Technology (OCCT) as the underlying geometry kernel.

Basic usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)

Note: This is a personal fork for learning and experimentation.
Upstream project: https://github.com/CadQuery/cadquery

Personal notes:
    - Exploring assembly constraints and multi-part models
    - Testing custom selector patterns for complex geometry filtering
    - See examples/ directory for personal experiments
    - TODO: investigate DirectionMinMaxSelector behavior on curved edges
    - NOTE: SumSelector and SubtractSelector are easy to confuse; SumSelector
      is OR logic, SubtractSelector is set-difference (not arithmetic)
    - NOTE: AndSelector is equivalent to set-intersection; combining with
      InverseSelector gives NOT logic, e.g. AndSelector(sel, InverseSelector(other))
    - NOTE: StringSyntaxSelector is the entry point for the string-based selector
      mini-language (e.g. "|X", "#Z", ">Y"); prefer it for interactive use
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

# Personal fork metadata
__fork_author__ = "personal"
__fork_purpose__ = "learning and experimentation"
# Upstream version this fork is based on, for easy diffing against upstream releases
__fork_base_version__ = "2.4.0"

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
