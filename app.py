from channel_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='myfakedomain.com', port=8000, debug=True)