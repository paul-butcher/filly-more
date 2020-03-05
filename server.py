from io import BytesIO
from flask import Flask
from flask import request
from tartan.tartan import threadcount_to_image

app = Flask(__name__)


@app.route("/tartan.png")
def get_image():
    buffer = BytesIO()

    img = threadcount_to_image(request.args['threadcount'], (512, 512))
    img.save(buffer, "PNG")

    response = app.make_response(buffer.getvalue())
    response.mimetype = "image/png"
    return response


if __name__ == "__main__":
    app.run()