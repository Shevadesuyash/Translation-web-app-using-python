# app.py
from flask import Flask, request, jsonify, render_template
from googletrans import Translator

app = Flask(__name__, template_folder='templates')

def detect_language(text_to_detect):
    try:
        translator = Translator()
        detected_language = translator.detect(text_to_detect).lang
        return detected_language
    except Exception as e:
        return f"Language detection error: {str(e)}"

def translate_text(from_language, to_language, text_to_translate):
    try:
        translator = Translator()

        if from_language == "auto":
            # Detect the input language
            from_language = detect_language(text_to_translate)

        translation = translator.translate(text_to_translate, src=from_language, dest=to_language)

        translated_text = translation.text
        pronunciation = translation.pronunciation if from_language == "en" else None

        return translated_text, pronunciation
    except Exception as e:
        return f"Translation error: {str(e)}", None

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    from_language = data.get('from_language')
    to_language = data.get('to_language')
    text_to_translate = data.get('text_to_translate')

    translated_text, pronunciation = translate_text(from_language, to_language, text_to_translate)
    
    response = {'translated_text': translated_text}
    if pronunciation:
        response['pronunciation'] = pronunciation
    
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translator.html')
def translator():
    return render_template('translator.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
