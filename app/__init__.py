import config, logging, time, traceback, uuid, pytz
from flask import Flask, make_response, jsonify, json, request, render_template
from time import strftime
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy, get_state

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from app.controllers import *

@app.teardown_request
def teardown_request(exception):
    # print('ping teardown => ', time.time())
    if exception:
        print('teardown_request exception => ', str(exception))
        db.session.rollback()
    db.session.remove()
    db.session.close()

@app.errorhandler(404)
def not_found(error):
    print('404 error')
    # return render_template('pages/error.html')
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(exception):
    # logger.error(exception)
    print('Error handler => '+str(exception))
    return make_response(jsonify({'error': 'Server Fatal Error! Kindly Hang on!'}), 404)

@app.errorhandler(Exception)
def unhandled_exception(exception):
    print('Unhandled Error handler => ' + str(exception))
    return make_response(jsonify({'error': 'Server Fatal Error! Kindly Hang on!!'}), 404)

@app.after_request
def after_request(response):
    timestamp = strftime('%Y-%b-%d %H:%M')
    try:
        # print('%s %s %s %s \n%s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.headers, request.full_path, request.get_json(), request.args.to_dict(), response.status)Exception in after request
        request_data = None
        try:
            if request.data:
                request_data = json.loads(request.data)
            else:
                request_data = None
        except Exception as are:
            print('Exception in after request', are, ' | ', request_data)
            request_data = str(request_data)
        log_data = {
            'request_method': request.method,
            'request_full_path': request.full_path,
            'request_data_body': request_data,
            'request_data_args': request.args.to_dict(),
            'response_status': response.status,
            'response_data': response.data.decode('utf-8'),
            'request_headers': dict(request.headers),
            'timestamp': time.time(),
            'log_time_read': datetime.fromtimestamp(int(time.time()), pytz.timezone(
                    'Asia/Kolkata')).isoformat(),
            'request_remote_addr': request.remote_addr
        }
        # print('ping after => ', time.time())
        # if config.PRODUCTION:
        #     log_push('ping', log_data=log_data, push=True)
    except Exception as e:
        # print('Attention Required!! Some Error in Logging')
        print('Exception in after request => '+str(e))
    return response

@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    print('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return e

@app.before_request
def before_request():
    try:
        log_data = {
            'request_headers': dict(request.headers),
            'request_full_path': request.full_path,
            'request_data': request.data.decode('utf-8'),
            'request_data_args': request.args.to_dict(),
            'request_method': request.method,
            'timestamp': time.time(),
            'log_time_read': datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Kolkata')).isoformat(),
            'request_remote_addr': request.remote_addr
        }
        # print('ping before => ', time.time())
        # if config.PRODUCTION:
            # log_push('ping', log_data=log_data, push=True)
    except Exception as e:
        # print('Attention Required!! Some Error in Logging')
        print('Exception in before request => '+str(e))
