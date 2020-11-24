
def start_ngrok():
    # based on miguel grinberg's implementation so you can
    # view the ngrok public url from the flask development server
    from pyngrok import ngrok

    url = ngrok.connect(500)
    print('* Tunnel URL:', url)