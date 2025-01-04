import uuid

def get_uid():
    unique_uid = uuid.uuid4()
    return str(unique_uid)