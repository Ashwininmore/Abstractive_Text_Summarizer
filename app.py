from flask import Flask, render_template, request
from text_summary import summarizer
from pdf_summary import summarizer1
from audio_summary import summarizer2

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf')
def index1():
    return render_template('index1.html')

@app.route('/audio')
def index2():
    return render_template('index2.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)

    return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

@app.route('/analyze1', methods=['GET', 'POST'])
def analyze1():
    if request.method == 'POST':
        pdf_file = request.form['pdf_file']
        # summary_1: str
        # original_txt_1: str
        # len_orig_txt_1: int
        # len_summary_1: int
        summary, original_txt, len_orig_txt, len_summary = summarizer1(pdf_file)
        # print(summary)
    return render_template('summary1.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

@app.route('/analyze2', methods=['GET', 'POST'])
def analyze2():
    if request.method == 'POST':
        aud_file = request.form['aud_file']
        # summary_1: str
        # original_txt_1: str
        # len_orig_txt_1: int
        # len_summary_1: int
        summary, original_txt, len_orig_txt, len_summary = summarizer2(aud_file)
        # print(summary)
    return render_template('summary2.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)


if __name__ == "__main__":
    app.run(debug=True)

