from rest_framework_jwt.utils import jwt_payload_handler

def self_jwt_payload_handler(user):
    print("call my handler")
    payload = jwt_payload_handler(user)
    payload["role"] = "测试"
    return payload