from flask import Flask, jsonify, send_file
import os
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app"})

@app.route('/image')
def image():

    text = "sample image"

    # 画像の幅と高さを設定
    width, height = 400, 200
    
    # 白背景の画像を作成
    image = Image.new('RGB', (width, height), color='white')

    # 画像に文字列を描画するための設定
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 40)  # フォントとサイズを指定（arial.ttfはフォントのパス）

    # 画像中央に文字列を描画
    xL, yT, xR, yB = draw.textbbox((0,0), text, font=font)
    text_position = ((width - (xR - xL)) // 2, (height - (yB - yT)) // 2)
    draw.text(text_position, text, font=font, fill='black')

    # 画像をバイナリデータとして保存
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    return send_file(img_byte_array, mimetype='image/png')

@app.route('/api/<test>', methods=['GET'])
def api_text(test):
    return jsonify({"maiha":f"{test}"})

@app.route(r'/table/<text>', methods=['GET'])
def generate_image(text):

    # 画像の幅と高さを設定
    width, height = 400, 200
    
    # 白背景の画像を作成
    image = Image.new('RGB', (width, height), color='white')

    # 画像に文字列を描画するための設定
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 40)  # フォントとサイズを指定（arial.ttfはフォントのパス）

    # 画像中央に文字列を描画
    xL, yT, xR, yB = draw.textbbox((0,0), text, font=font)
    text_position = ((width - (xR - xL)) // 2, (height - (yB - yT)) // 2)
    draw.text(text_position, text, font=font, fill='black')

    # 画像をバイナリデータとして保存
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    return send_file(img_byte_array, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))