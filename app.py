import flask

app = flask.Flask('app')


# @app.route()
@app.route('/test')
def test():
    return flask.jsonify({'status': 'it works!'})


app.run()
