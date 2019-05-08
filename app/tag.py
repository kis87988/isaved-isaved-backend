from app import app
import database
from datetime import datetime
from flask import request, jsonify
from __init__ import db
from flask import make_response

@app.route('/tag/modifyItem', methods=['POST'])
def modify_item():
    """Update modification of users to database

    URL: /tag/modifyItem
    Method: POST
    Headers:
        Content-Type: application/json
    Body:   {
                "userID": 123,
                "itemID": 1234,
                "Title": "Example title",
                "Tag": "Example tag"
            }

    Required: userID, itemID
    Returns:
        successful:
                100: successfully modify from database
        failed:
                201: userID not found
                202: itemID not found
                204: can't update item from table
                400: other errors, bad request
    """

    if 'userID' not in request.json:
        return make_response(jsonify({"error code": 201, "status": "fail", "ErrorInfo": "Error: userID not found"}), 201)

    userID = request.json['userID']

    #
    #
    # Todo: Add validation part
    #
    #

    if 'itemID' not in request.json:
        return make_response(jsonify({"error code": 202, "status": "fail", "ErrorInfo": "Error: itemID not found"}), 202)
    itemID = request.json['itemID']

    Title = None
    if 'Title' in request.json:
        Title = request.json['Title']

    Tag = None
    if 'Tag' in request.json:
        Tag = request.json['Tag']

    try:
        item = db.session.query.filter_by(itemID=itemID, userID=userID).first()
        if Title:
            item.Title = Title
        if Tag:
            item.Tag = Tag
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200)
    except:
        return make_response(jsonify({"error code": 204, "status": "fail", "ErrorInfo": "Error: can not delete item from database"}), 204)


@app.route('/tag/addItem', methods = ['POST'])
def add_item():
    """Add an item to database when users save links to their account

    URL: /tag/addItem
    Method: POST
    Headers:
          Content-Type: application/json
    Body:   {
                "Link": "google.com",
                "userID": 1234,
                "Title": "Google Search",
                "Tag": "Search Engine, Google"
            }

    Required: userID and Link

    Returns:
        successful:
                100: successfully add to database
        failed:
                201: userID not found
                202: Link not found
                203: can't add item to table
                400: other errors, bad request
    """
    if 'userID' not in request.json:
        return make_response(jsonify({"error code": 201, "status": "fail", "ErrorInfo": "Error: userID not found"}), 201)

    userID = request.json['userID']

    #
    #
    # Todo: Add validation part
    #
    #

    if 'Link' not in request.json:
        return make_response(jsonify({"error code": 202, "status": "fail", "ErrorInfo": "Error: Link not found"}), 202)
    Link = request.json['Link']

    # Title
    if 'Title' in request.json:
        Title = request.json['Title']
    else:
        Title = ''

    # Tag
    if 'Tag' in request.json:
        Tag = request.json['Tag']
    else:
        Tag = ''

    new_item = database.UserTagTable()
    new_item.Link = Link
    new_item.userID = userID
    new_item.Title = Title
    new_item.Tag = Tag
    new_item.CreateTime = datetime.now()
    new_item.LastUpdateTime = datetime.now()

    try:
        db.session.add(new_item)
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200)
    except:
        return make_response(jsonify({"error code": 203, "status": "fail", "ErrorInfo": "Error: can not add item to database"}), 203)


@app.route('/tag/removeItem', methods = ['POST'])
def remove_item():
    """Remove an item from database when users delete links from their account

    URL: /tag/removeItem
    Method: POST
       Headers:
           Content-Type: application/json
    Body:   {
                "userID": 123,
                "itemID": 1234
            }

    Required: userID and itemID

    Returns:
        successful:
                100: successfully remove from database
        failed:
                201: userID not found
                202: itemID not found
                203: can't remove item from table
                400: other errors, bad request
    """
    if 'userID' not in request.json:
        return make_response(jsonify({"error code": 201, "status": "fail", "ErrorInfo": "Error: userID not found"}), 201)

    userID = request.json['userID']

    #
    #
    # Todo: Add validation part
    #
    #

    if 'itemID' not in request.json:
        return make_response(jsonify({"error code": 202, "status": "fail", "ErrorInfo": "Error: itemID not found"}), 202)
    itemID = request.json['itemID']

    try:
        item = database.UserTagTable.query.filter_by(itemID=itemID, userID=userID).first()
        db.session.delete(item)
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200)
    except:
        return make_response(jsonify({"error code": 203, "status": "fail", "ErrorInfo": "Error: can not delete item from database"}), 203)
