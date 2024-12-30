from gtts import gTTS
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# import pymysql


tts = gTTS(text="เดี๋ยวกูจะลองหาวิธีเทรนต่อถ้าได้เดี๋ยวบอก @@@@@@@@@@", lang="th")
tts.save("C:/Users/sittipon/Desktop/voiceprot/output.mp3")



app = Flask(__name__)
CORS(app)

@app.route('/api/aiget', methods=['GET', 'POST'])
def aiconncet():
    aiget = request.get_json()
    print(aiget)
    return jsonify({"success": True}), 200

if __name__ == '__main__':
    app.run(debug=True) 