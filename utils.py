
def start_ngrok():
    # based on miguel grinberg's implementation so you can
    # view the ngrok public url from the flask development server
    from pyngrok import ngrok

    public_url = ngrok.connect(5000)  # .connect returns public url assigned to localhost
    print('* Tunnel URL:', public_url)


