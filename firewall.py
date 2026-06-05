from rules import *

def firewall_check(query):
    q = query.lower()

    for token in q.split():
        if token.isdigit():
            return "HIGH RISK", False, \
                   "Numeric dosage value detected"

    for keyword in DANGER_KEYWORDS:
        if keyword in q:
            return "HIGH RISK", False, \
                   f"Danger keyword detected: {keyword}"

    for intent in UNSAFE_INTENTS:
        if intent in q:
            return "HIGH RISK", False, \
                   "Unsafe medical intent detected"

    for med in MEDICINE_LIST:
        if med in q:
            return "MEDIUM RISK", False, \
                   f"Medicine detected: {med}"

    return "SAFE", True, \
           "No harmful patterns found"