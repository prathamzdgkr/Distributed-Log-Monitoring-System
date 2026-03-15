def analyze_logs(logs):

    errors = 0
    warnings = 0
    infos = 0

    for log in logs:

        if log[2] == "ERROR":
            errors += 1

        elif log[2] == "WARNING":
            warnings += 1

        elif log[2] == "INFO":
            infos += 1

    result = {
        "errors": errors,
        "warnings": warnings,
        "infos": infos
    }

    return result