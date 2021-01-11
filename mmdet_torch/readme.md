# Some modifications for the case of gt bbox feature extracting.
1. `tools/test.py` and `convfc_bbox_head.py` is seperately the modified files for the original file under test mode of mmdetection
2. `tools/embedding_projector_maker.py` is the script that generates the `.tsv` files for web tool ([embedding projector](https://projector.tensorflow.org/)) according to the data files `gt_labels.npy` and `feature.npy` from 1. 
