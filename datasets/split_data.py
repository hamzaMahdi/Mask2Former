import os
import random
from datumaro.components.dataset import Dataset
def split_coco_panoptic(input_dir, output_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1, seed=42):
    # Set random seed for reproducibility
    random.seed(seed)

    # Load the dataset
    dataset = Dataset.import_from(input_dir, 'coco')

    dataset.transform("random_split", splits=[("train", 0.8), ("val", 0.2)])
    dataset.export(output_dir, "coco_panoptic", save_media=True)
if __name__ == "__main__":
    input_dir = "unprocesed_coco/"
    output_dir = "coco/"
    
    split_coco_panoptic(input_dir, output_dir)