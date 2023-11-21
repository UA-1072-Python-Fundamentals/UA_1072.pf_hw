from flask import Flask, render_template, request
from my_functions import log_request, search_letters, count_characters, count_words, between_letters, between_words

app = Flask(__name__)


@app.route('/')
def enter_page() -> 'html':
    return render_template('first_page.html',
                           the_title='Welcome to letters and words seeker!',
                           the_text='This site helps you to find what you want in text')


@app.route('/between_words')
def between_words_page() -> 'html':
    return render_template('between.html',
                           the_title='Welcome to "Search sentences between first and last words"!',
                           the_action="/results_between_words",
                           the_first='Fists word',
                           the_last='Last word')


@app.route('/results_between_words', methods=['POST'])
def do_find_between_words() -> 'html':
    text = request.form['text']
    word1 = request.form['first']
    word2 = request.form['last']
    results = between_words(text, word1, word2)
    log_request('between words', request, results)
    return render_template('results_between.html',
                           the_title='Here are your results:',
                           the_data=results,
                           the_text=text,
                           the_first=word1,
                           the_last=word2,
                           what='word')


@app.route('/between_letters')
def between_letters_page() -> 'html':
    return render_template('between.html',
                           the_title='Welcome to "Search words between first and last letters"!',
                           the_action="/results_between_letters",
                           the_first='Fists character',
                           the_last='Last character',)


@app.route('/results_between_letters', methods=['POST'])
def do_find_between_letters() -> 'html':
    text = request.form['text']
    letter1 = request.form['first']
    letter2 = request.form['last']
    results = between_letters(text, letter1, letter2)
    log_request('between letters', request, results)
    return render_template('results_between.html',
                           the_title='Here are your results:',
                           the_data=results,
                           the_text=text,
                           the_first=letter1,
                           the_last=letter2,
                           what='letter')


@app.route('/count_words')
def count_words_page() -> 'html':
    return render_template('count.html',
                           the_title='Welcome to "Counting words"!',
                           the_action="/results_count_words")


@app.route('/results_count_words', methods=['POST'])
def do_count_words() -> 'html':
    text = request.form['text']
    row_titles = ('Words', 'Times')
    results = count_words(text)
    log_request('count words', request, results)
    return render_template('results_cont.html',
                           the_title='Here are your results:',
                           the_data=results,
                           the_row_titles=row_titles,)


@app.route('/count_characters')
def count_characters_page() -> 'html':
    return render_template('count.html',
                           the_title='Welcome to "Counting characters"!',
                           the_action="/results_count_characters")


@app.route('/results_count_characters', methods=['POST'])
def do_count_characters() -> 'html':
    text = request.form['text']
    row_titles = ('Characters', 'Times')
    results = count_characters(text)
    log_request('count characters' ,request, results)
    return render_template('results_cont.html',
                           the_title = 'Here are your results:',
                           the_data=results,
                           the_row_titles=row_titles,)


@app.route('/letters_in')
def letters_page() -> 'html':
    return render_template('search_letters.html',
                           the_title='Welcome to "Is letter in?"!')


@app.route('/results_letters_in', methods=['POST'])
def do_search_letters_in() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_letters(phrase, letters))
    log_request('search letters in', request, results)
    return render_template('results_letters.html',
                           the_title='Here are your results:',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('log.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(item)
    titles = ('Remote addr', 'User agent', 'Time', 'What', 'Form Data',  'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


@app.route('/about')
def about_page() -> 'html':
    return render_template('first_page.html',
                           the_title='About project',
                           the_text='This project was created by Oleksandr_SawaAser for SoftServe')


if __name__ == '__main__':
    app.run(debug=True)
