# ComplexTerrain-GAYOLO
ComplexTerrain-GAYOLO

If you want to refer to the paper’s model alongside the code: the model section is located in `PowerLine-MTYOLOv11` within the `v8` directory under `models`, and the `block` is in the `modules` directory. 

## How to Run

### Clone this Repository

```shell
git clone https://github.com/Tairan4356/ComplexTerrain-GAYOLO.git
cd ComplexTerrain-GAYOLO
```

### Install Requirements

```shell
# Python version 3.12
pip install -r requirements.txt
```

### Model Path

```shell
ultralytics/models/v8/PowerLine-MTYOLOv11.yaml
```

### train

```shell
python train.py
```

### validate

```shell
python val.py
```