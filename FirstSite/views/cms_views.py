import flask

from infrastructure.view_modifiers import response
from services.cms_service import get_page

blueprint = flask.Blueprint('cms', __name__, template_folder='cms')

@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    print("Getting CMS page for {}".format(full_url))

    page = get_page(full_url)
    if not page:
        return flask.abort(404)
    return page
