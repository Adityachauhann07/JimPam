from flask import Flask, send_from_directory

app = Flask(__name__)

# Define the directory where the GIF is stored
GIF_DIRECTORY = "C:/Users/ADMIN/Desktop/Jimpam"
GIF_FILENAME = "jim_pam.gif"


@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Exclusive GIF</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f4f4f4;
                margin: 0;
                font-family: Helvetica, Arial, sans-serif;
                text-align: center;
            }}
            h2 {{
                color: #333;
                max-width: 80%;
                font-weight: normal;
                font-size: 16px; /* Reduced font size */
                margin-bottom: 15px;
            }}
            img {{
                max-width: 100%;
                height: auto;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <h2>So… this GIF? Never sent it to anyone before. Not even Dwight. Just you. 
        You’re the only one with this link. 
        Kinda exclusive, right? No big deal… 
        but also, maybe a little bit of a big deal.</h2>
        <img src="/gif" alt="Exclusive GIF">
    </body>
    </html>
    """


@app.route("/gif")
def serve_gif():
    return send_from_directory(GIF_DIRECTORY, GIF_FILENAME)


if __name__ == "__main__":
    app.run(debug=True)
