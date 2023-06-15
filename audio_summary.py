# {
#   "type": "service_account",
#   "project_id": "quick-flame-382205",
#   "private_key_id": "f2e7071e1cbebed3844dcffe2dda9cc8d5def52f",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCw1zQfLP0sM5su\nZhk7VRJC60T0jcglqGwmL3qXy0Q4++Cagh3zLaxN3CY0u/mXLpyYIi5M3uxzfXyD\nI1czFGIXCPIt1HQkIEQ5R5PBklwK9cJEyXJRus/xiwPZ83YRrKftP6gVw/Ju+eU0\nXS8VybqfVSvMd/H8+CLItwZjbTubEBt2siNUTvM79bFJgxrdAawwtnU4nJKNn44O\nGRZsWTbxYRYTNYlzP76Anm0NWAjHorHpOlTvH50Az9euDiVktcYaLABTXYvwj4Lg\nWKkag1KkBNnfJ3DIGXLwQnhWUyhCilGx/tHeE2oAmNc6kwF/7LV/wrhLF83NXIrD\nL+4J2fZdAgMBAAECggEAEt3i4bCbEiwvUjPyXTImUJ1pLe4yfFILt8c4/RjinnHA\n9LsNFvS4fVYPfXDQoCCI9HIxHmJqN6gbsKIEm56BGJQLwnf4LCKFJNdOHEjRKRov\nL8eOOsoDhXGfZ5Fh92DESbuQ40GUi+J9YajPbTOohXdAxP/HAYY3r9JXDCSLR2+z\nBLzTQ16Z4c3n/GLoR4uMGaELy/2XV6l3pvrIbTvmxaQq4O1wHi02/b53PDyRY64p\nOETPjbKPvSIq7/IOTk3AQkAEyE3ZFARXGo0cJ1eP9lcPh28dBRBm96JffNl/VMR6\nmjx4cvQs6ZqpWW08K9bzFxqs8BO+nNIWDoAOPjS8wQKBgQDhUYFtlTNKylgq04ol\nyXVbgI9G2O7ulYKgsgI0TV50CKJ7WNjPwfiP5va1w7VRKh6gV+ge0NhNlwJhrLNE\ntysyn0bmc+8GYmKmRESR8FELTWc5wQTJpL6+1AZbTcI1mCXNC/OPWUwOokTFaaDr\nvSnyGiFyCUwlulPBrwRApZAIiwKBgQDI68lQZNMeLWA+B3Dgxqqk2wWXV7gQJvLG\nGAvGS1fCRFEJ2IUbrwhPlxyyNZQoqwGLxFviQVmQcxsUGOXHeYxi24s229IPJyqy\neMaEjHoQ70FwIt8fE6G7bn4MqL/z5peBxD9Mf6FItCpeaG4Sf90p/EP7dxRYYhfp\nRumZiavxtwKBgQClD1prdqNupLDWHsXTTLQGZjWPxxex/CEHq5/lxM/u3Ox6w+mA\nuS5n7ODK4yYO4XYyLHPFL2Vl4bxC5YsmSbEBkqET7dYqrSRrfRNmfdBBIWD/dCEX\nvvJlRVmqxVoCfQUkIx834kjPZ5xNqkXSrG7wBqh9q8X21XrKJnZNDXxoZQKBgQCQ\nR/G6z4xjgUY5hPJkF4X2+Gkdcxp0TuPLqPzbmsMceB6RqXB8nsajEOrEdoE8awCj\nM5Cf+zmr51yso+xtwDU10F46OMSxqPiaTOyRxqbpfkZJlmEPWfOsOv49bPja1t45\ni4nBD23sXaSHQwq4MiXJvqO68pojld2B4TBi12AoJQKBgQCkFVjlEhYpLyGxzFZp\n8aswLAxA8QFsnAudJS5OWvgz2iED8JgCyTXH83daRCCigZFOglp8Xxo0M8YVpT1L\naJ7GZsbmVu89ZgbDjDBf6QSe/UqtMVKHjrr8NgPZNV3zRCKu9zHTO9yxuuIIX+uh\nNi9NwoPTnRY3v8RDf3IGH8suKw==\n-----END PRIVATE KEY-----\n",
#   "client_email": "myproject@quick-flame-382205.iam.gserviceaccount.com",
#   "client_id": "118007860893781131589",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/myproject%40quick-flame-382205.iam.gserviceaccount.com"
# }

def summarizer2(aud_file):
    from google.cloud import speech
    import os
    import io

    import spacy
    from spacy.lang.en.stop_words import STOP_WORDS
    from string import punctuation
    from heapq import nlargest

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_secret_key.json'

    client = speech.SpeechClient()

    # file_name = aud_file
    # file = open(aud_file, 'rb')
    # content = file.read()
    # audio = speech.RecognitionAudio(content)
    with io.open(aud_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        audio_channel_count=1,  # mono sathi 1 ani stereo 2

        language_code="en-US",
    )
    response = client.recognize(request={"config": config, "audio": audio})

    a = ""
    for result in response.results:
        result = result.alternatives[0].transcript
        a += result

    # print(a)


    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(a)
    # print(doc)
    tokens = [token.text for token in doc]
    # print(tokens)

    # punctuation = punctuation + '\n'
    # punctuation

    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # print(word_frequencies)

    max_freq = max(word_freq.values())
    # max_frequency

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # sentence_scores

    select_len = int(len(sent_tokens) * 0.3)
    # select_length

    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    # summary

    final_summary = [word.text for word in summary]

    summary = ' '.join(final_summary)

    # print(text)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # print(summary)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # print("lenght of origianl text", len(text.split(' ')))
    # print("lenght of summary text", len(summary.split(' ')))
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return summary, doc, len(a.split(' ')), len(summary.split(' '))
