def is_rate_limited(response):
    return response.status_code in [429, 403]