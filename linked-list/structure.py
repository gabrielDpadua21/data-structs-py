head = {
    "value": 11,
    "next": {
        "value": 22,
        "next": {
            "value": 33,
            "next": {
                "value": 44,
                "next": None
            }
        }
    }
}

print(head["next"]["next"]["next"]["value"])