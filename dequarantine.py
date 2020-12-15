from flask import request, url_for
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


tags = {
    0: 'quarantine ',
   }

def tag_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('tags_detail', key=key),
        'text': tags[key]
    }


@app.route("/", methods=['GET', 'POST'])
def tags_list():
    """
    List or create tags.
    """
    if request.method == 'POST':
        tag = str(request.data.get('text', ''))
        idx = max(tags.keys()) + 1
        tags[idx] = tag
        return tag_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [tag_repr(idx) for idx in sorted(tags.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def tags_detail(key):
    """
    Retrieve, update or delete tag instances.
    """
    if request.method == 'PUT':
        tag = str(request.data.get('text', ''))
        tags[key] = tag
        return tag_repr(key)

    elif request.method == 'DELETE':
        tags.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in tags:
        raise exceptions.NotFound()
    return tag_repr(key)



if __name__ == "__main__":
    app.run(debug=True)
    print (tags)