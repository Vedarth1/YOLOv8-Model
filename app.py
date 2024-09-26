from flask import Flask, request, json , Response , jsonify,send_file
import os,subprocess
from pathlib import Path
from flask_cors import CORS
from werkzeug.utils import secure_filename
import glob
from zipfile import ZipFile

app = Flask(__name__)
CORS(app)

Path('results/').mkdir(exist_ok=True)
Path('uploads/').mkdir(exist_ok=True)

@app.route('/')
def home():
    return jsonify({"status": "API is working"})

@app.route('/predict', methods=['POST'])
def predict_image():
    try:
        if 'file' not in request.files:
            raise ValueError("File not found")
        
        file = request.files['file']
        if file.filename == '':
            raise ValueError("File not found")
        
        filename = secure_filename(file.filename)
        filename_with_extension = filename.rsplit('.', 1)[0] + '.jpg'
        temp_dir = os.path.join(os.getcwd(), 'uploads')

        temp_file_path = os.path.join(temp_dir, filename_with_extension)
        file.save(temp_file_path)

        print("File received!!! \n Model is working on image!")

        command = f"python ultralytics/yolo/v8/detect/predict.py model='newpts.pt' source=\"{temp_file_path}\""

        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return Response(json.dumps({
                'status': "failed",
                'message': "Model finds an error while processing",
                'error': str(e)
            }), status=500, mimetype='application/json')
        
        print("image processed by model")

        os.remove(temp_file_path)
        x=os.path.join(os.getcwd(),filename_with_extension)
        if os.path.exists(x):
            os.remove(x)

        result_images = glob.glob('results/*.jpg')
        zip_filename = os.path.join('results', 'result_images.zip')
        with ZipFile(zip_filename, 'w') as zipf:
            for image in result_images:
                zipf.write(image, os.path.basename(image))

        for img in result_images:
            os.remove(img)

        return send_file(zip_filename, mimetype='application/zip', as_attachment=True, download_name='result_images.zip')
        
        # return Response(json.dumps({
        #     # 'response':result_rto_info,
        #     'status': "success",
        # }), status=200, mimetype='application/json')

    except Exception as e:
        return Response(
            response=json.dumps({'status': "failed",
                                 "message": "Error Occurred",
                                 "error": str(e)}),
            status=500,
            mimetype='application/json'
        )
    
    finally:
        zip_filename = os.path.join('results', 'result_images.zip')
        if os.path.exists(zip_filename):
            os.remove(zip_filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
