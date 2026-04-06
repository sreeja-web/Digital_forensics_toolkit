def predict(data):
    # Dummy model
    if len(data) > 50:
        return "Suspicious"
    return "Safe"