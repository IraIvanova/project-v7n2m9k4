def validate_args(args, expected_count, message):
    if len(args) < expected_count:
        raise ValueError(message)