from app import app
import database
from datetime import datetime
from flask import request, jsonify
from __init__ import db
from flask import make_response

@app.route('/display/displayByTime', methods=['GET'])
def display_by_time():
    """ Display items by selecting time period
    URL: /display/displayByTime
    Method: GET
    Headers:
        Content-Type: application/json
    Example Body:  {
	                    "userID": 123489011,
	                    "starttime": "2019-05-04-00:00:00",
	                    "endtime": "2019-05-04-23:59:59"
                    }
    Required: userID, starttime, endtime
    Returns:
        successful:
                200: successful. Return with an array of dict. For example:
                {
                    "items": [
                        {
                            "CreateTime": "Sat, 04 May 2019 11:45:58 GMT",
                            "LastUpdateTime": "Sat, 04 May 2019 11:45:58 GMT",
                            "Link": "linkedin.com",
                            "Tag": "social, linked",
                            "Title": "linkedin",
                            "itemID": 4,
                            "userID": 123489011
                        },
                        {
                            "CreateTime": "Sat, 04 May 2019 11:47:11 GMT",
                            "LastUpdateTime": "Sat, 04 May 2019 11:47:11 GMT",
                            "Link": "stackoverflow.com",
                            "Tag": "social, q&a",
                            "Title": "stackoverflow",
                            "itemID": 5,
                            "userID": 123489011
                        }
                    ],
                    "status": "success"
                }
        failed:
                601: Require parameters not found
                602: Error when query from database
    
    """
    if 'userID' not in request.json:
        return make_response(jsonify({"error code": 601, "status": "fail", "ErrorInfo": "Error: userID not found"}), 601)

    userID = int(request.json['userID'])

    #
    #
    # Todo: Add validation part
    #
    #

    if 'starttime' not in request.json:
        return make_response(jsonify({"error code": 601, "status": "fail", "ErrorInfo": "Error: starttime not found"}), 601)
    starttime = request.json['starttime']
    starttime = datetime.strptime(starttime, "%Y-%m-%d-%H:%M:%S")

    if 'endtime' not in request.json:
        return make_response(jsonify({"error code": 601, "status": "fail", "ErrorInfo": "Error: endtime not found"}), 601)
    endtime = request.json['endtime']
    endtime = datetime.strptime(endtime, "%Y-%m-%d-%H:%M:%S")

    try:
        items = db.session.query(database.UserTagTable).filter(database.UserTagTable.userID==userID, database.UserTagTable.CreateTime.between(starttime, endtime)).all()
        return_items = []
        for item in items:
            return_items.append({   "userID":item.userID, 
                                    "itemID":item.itemID,
                                    "Link":item.Link,
                                    "Title":item.Title,
                                    "Tag":item.Tag,
                                    "CreateTime":item.CreateTime,
                                    "LastUpdateTime":item.LastUpdateTime})
        return make_response(jsonify({"status": "success", "items": return_items}), 200)
  
    except: 
        return make_response(jsonify({"error code": 602, "status": "fail", "ErrorInfo": "Error: can not delete item from database"}), 602)
