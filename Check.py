http_status_codes = {
    100: {
        'description': 'Continue',
        'category': 'Informational',
        'use_case': 'The server acknowledges the request, and the client should proceed with the request.',
        'suggested_action': 'Continue sending the request body if applicable.',
        'rfc_reference': 'RFC 7231, Section 6.2.1',
    },
    200: {
        'description': 'OK',
        'category': 'Successful',
        'use_case': 'The request has been successfully processed, and the server is sending the response.',
        'suggested_action': 'Display the received content to the user.',
        'rfc_reference': 'RFC 7231, Section 6.3.1',
    },
    302: {
        'description': 'Found',
        'category': 'Redirection',
        'use_case': 'The requested resource temporarily resides under a different URL.',
        'suggested_action': 'Follow the redirection to the new URL if necessary.',
        'rfc_reference': 'RFC 7231, Section 6.4.3',
    },
    400: {
        'description': 'Bad Request',
        'category': 'Client Error',
        'use_case': 'The server cannot understand or process the client\'s request due to malformed syntax.',
        'suggested_action': 'Check the request for syntax errors or invalid parameters.',
        'rfc_reference': 'RFC 7231, Section 6.5.1',
    },
    500: {
        'description': 'Internal Server Error',
        'category': 'Server Error',
        'use_case': 'A generic error message indicating that something went wrong on the server.',
        'suggested_action': 'Contact the website administrator or support team for assistance.',
        'rfc_reference': 'RFC 7231, Section 6.6.1',
    },
    
}

# User input
while True:
    try:
        status_code = int(input('Enter an HTTP status code (or 0 to exit): '))
        if status_code == 0:
            break
        info = http_status_codes.get(status_code, {'description': 'Unknown'})
        print(f'Status Code {status_code}: {info["description"]}')
        print(f'Category: {info["category"]}')
        print(f'Use Case: {info["use_case"]}')
        print(f'Suggested Action: {info["suggested_action"]}')
        print(f'RFC Reference: {info["rfc_reference"]}')
    except ValueError:
        print('Invalid input. Please enter a valid HTTP status code or 0 to exit.')
