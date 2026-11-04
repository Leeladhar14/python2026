logs = [
    "INFO: Application started",
    "ERROR: Database connection failed",
    "INFO: Request processed",
    "ERROR: Timeout occurred",
    "WARNING: High memory usage",
    "ERROR: Service unavailable"
]


def error_count(logs):
    count_info = 0
    count_error = 0
    count_warning = 0
    error_list = []
    for key in logs:
        if 'INFO' in key:
            count_info +=1
        elif 'ERROR' in key:
            error_list.append(key)
            count_error +=1
        elif 'WARNING' in key:
            count_warning +=1
    print(f'ERROR_COUNT {count_error}, WARNING_COUNT {count_warning}, INFO_COUNT {count_info}')
    print(error_list)

error_count(logs)
