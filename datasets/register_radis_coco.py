from detectron2.data.datasets import register_coco_instances

for d in ["train", "val"]:
    register_coco_instances(f"radis_{d}", {}, f"radis_coco/annotations/instances_{d}2017.json", f"radis_coco/{d}2017")