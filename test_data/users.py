STANDARD_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

INVALID_USER = {
    "username": "wrong_user",
    "password": "wrong_password",
    "expected_error": "Username and password do not match",
}

LOCKED_OUT_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce",
    "expected_error": "Sorry, this user has been locked out",
}