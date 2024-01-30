from fastapi import APIRouter
from flask import Flask, request, jsonify
from api.db_utils import create_connection, md5_hash

router = APIRouter()

@router.post('/login')
def login():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required'}), 400

    username = data['username']
    password = data['password']

    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Check if the user exists in the database
        cursor.execute("SELECT * FROM \"user\" WHERE lower(first_name) = lower(%s) AND pass_hash = %s", (username, md5_hash(password)))
        user = cursor.fetchone()

        if user:
            # If the user exists, you can return a token or other authentication mechanism
            # For simplicity, returning a success message here
            return jsonify({'message': 'Login successful'})

        return jsonify({'error': 'Invalid username or password'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        conn.close()


