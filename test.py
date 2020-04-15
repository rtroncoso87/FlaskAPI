from flask import Flask, jsonify, abort, make_response, request, url_for

task = {
        'id': 1,
        'title': 'This is my title',
        'description': 'Description right here',
        'done': False
    }

print(type(task['title']))

if 'title' in task and type(task['title']) != str:
    print('Yea baby')
else:
    print('Nope, not today')