from flask import Flask, render_template_string

application = gyfbhbkfcfgdFlask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>My CI/CD App</title></head>
<body>
    <h1>Hello, this is auto-trigger test! Thanks!</h1>
    <p>This was deployed automatically via CodePipeline</p>
</body>
</html>
"""

@application.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
