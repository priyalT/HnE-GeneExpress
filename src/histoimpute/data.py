from dataclasses import dataclass
import numpy as np
import pandas as pd
import squidpy as sq
import scanpy as sc
from PIL import Image
from pathlib import Path
import anndata as ad



@dataclass
class VisiumDataset:
    image: np.ndarray 
    expression: ad.AnnData
    hvg: pd.DataFrame | None

    @classmethod
    def load_from_spaceranger(cls, p: Path) -> "VisiumDataset":
        img_path = p/"spatial"/"tissue_hires_image.png"
        img = np.array(Image.open(img_path))
        expression = sq.read.visium(
            p,
            var_names = "gene_symbols",
            cache=True
        )
        return cls(
            image = img,
            expression = expression,
            hvg = None,
        )
