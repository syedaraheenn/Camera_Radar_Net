# Copyright (c) OpenMMLab. All rights reserved.
from mmdet.core.anchor import build_prior_generator
from .anchor_3d_generator import (AlignedAnchor3DRangeGenerator,
                                  AlignedAnchor3DRangeGeneratorPerCls,
                                  Anchor3DRangeGenerator)
print("I am initiate in anchor")
__all__ = [
    'AlignedAnchor3DRangeGenerator', 'Anchor3DRangeGenerator',
    'build_prior_generator', 'AlignedAnchor3DRangeGeneratorPerCls'
]
