from flask import jsonify, request, Response
from pydantic import ValidationError

from . import main
from .. import db
from ..models import ShortURL, Link
from ..utils import id_generator, get_base_url


@main.route('/<site_id>/', methods=['GET'])
def go_to_site(site_id: str):
    url_obj = db.session.query(ShortURL).filter_by(url_id=site_id).first()
    if not url_obj:
        return jsonify(dict(message='This URL does not exist')), 400

    original_url = url_obj.original
    return Response(
        status=301,
        headers={
            'Location': original_url
        },
    )


@main.route('/short/', methods=['POST'])
def shorten_url():
    try:
        json_data = Link(**request.json)
    except ValidationError as validation_err:
        errors = validation_err.errors()
        return jsonify(errors), 400

    original_url = json_data.url
    new_id = id_generator()

    cut_rul_obj = ShortURL(
        original=original_url,
        url_id=new_id,
    )
    db.session.add(cut_rul_obj)
    db.session.commit()

    base_url = get_base_url()
    new_url = '{0}/{1}'.format(base_url, new_id)
    return jsonify(dict(new_url=new_url)), 201
