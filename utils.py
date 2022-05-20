def to_json(data, message, status_code):
    try:
        return {"data": data,
                "meta": {
                    "message": message,
                    "status_code": status_code
                    }
                }
    except:
        return {"data": "",
                "meta": {
                    "message": "fail to return response",
                    "status_code": 400
                    }
                }
