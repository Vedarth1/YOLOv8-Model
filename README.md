# **Licence-Plate-Detection-using-YOLO-V8**

Welcome to the detection model repository

**Few things to note**

1.   The images used as well as detected images in ``results`` directory are only for demo purpose here, new images should be used for detection purpose.

2. ``newpts.pt`` is an entire trained model for this project and should not be changed or removed anyhow...

3. This model is not yet integrated and hence you can use it saperately


## Run Locally

Clone the project

```bash
  git clone https://github.com/Vedarth1/YOLOv8-Model
```

Go to the project directory

```bash
  cd YOLOv8-Model
```

Create virtual environment

```bash
  python -m venv myenv
```

Activate virtual environment

```bash
  source myenv/bin/activate #for mac
```

Install Dependencies: 

(use any IDE like pycharm or jupyter notebook and ensure your interpreter is properly configured for python 3, else download python3 and set its environment variable globally.. also if need, update pip command)

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```


## Run by using Console

1. open python console or powershell in same IDE:

   For python console:

   ``!python ultralytics/yolo/v8/detect/predict.py model='newpts.pt' source='/replace with image path'``

   for powershell:

   ``python ultralytics/yolo/v8/detect/predict.py model='newpts.pt' source='/image path'``

2. If cuda and pytorch is properly configured in your model then you will be able to see detected image in ``results`` directory..
## API Reference

### Test API

```http
  GET /
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `None` | Returns hello! |

### Get item

```http
  POST /predict
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `file` | **Required**. image |

##### Returns zip file of Detected number plates of vehicles


## 🔗 Links
[![portfolio](https://img.shields.io/badge/reference-project
)](https://github.com/Vedarth1/ECOWATCH) Reference project!

A pollution monitoring and PUC validation System


