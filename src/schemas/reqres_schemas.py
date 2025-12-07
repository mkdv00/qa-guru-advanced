from voluptuous import ALLOW_EXTRA, Schema, Optional


reqres_get_user_schema = Schema(
    {
        'data': {
            'id': int,
            'email': str,
            'first_name': str,
            'last_name': str,
            'avatar': str
        }
    },
    extra=ALLOW_EXTRA,
    required=True
)
