from __future__ import annotations

import dataclasses
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, List, no_type_check

from document_recognition.backends import PathLike


@dataclasses.dataclass
class Coordinates:
    x_min: float
    y_min: float
    x_max: float
    y_max: float


@dataclasses.dataclass
class Data:
    name: str
    type: str
    coordinates: Coordinates

    pose: Optional[str] = None
    truncated: Optional[bool] = None
    difficult: Optional[bool] = None


@dataclasses.dataclass
class Size:
    width: int
    height: int
    depth: int


@dataclasses.dataclass
class Template:
    path: PathLike
    size: Size
    objects: List[Data]

    @classmethod
    @no_type_check
    def from_xml(cls, xml_path: PathLike) -> Template:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        return cls(
            path=Path(root.find("path").text).resolve(),
            size=Size(
                width=int(root.find("size").find("width").text),
                height=int(root.find("size").find("height").text),
                depth=int(root.find("size").find("depth").text),
            ),
            objects=[
                Data(
                    name=object_node.find("name").text,
                    type=object_node.find("type").text,
                    coordinates=Coordinates(
                        x_min=float(object_node.find("bndbox").find("xmin").text),
                        y_min=float(object_node.find("bndbox").find("ymin").text),
                        x_max=float(object_node.find("bndbox").find("xmax").text),
                        y_max=float(object_node.find("bndbox").find("ymax").text),
                    ),
                    pose=object_node.find("pose").text,
                    truncated=object_node.find("truncated").text == "1",
                    difficult=object_node.find("difficult").text == "1",
                )
                for object_node in root.findall("object")
            ],
        )
