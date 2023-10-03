http_status_codes = {
    100: {
        'description': 'Continue',
        'category': 'Informational',
        'use_case': 'The server acknowledges the request, and the client should proceed with the request.',
        'suggested_action': 'Continue sending the request body if applicable.',
        'rfc_reference': 'RFC 7231, Section 6.2.1',
    },
    101: {
        'description': 'Switching Protocols',
        'category': 'Informational',
        'use_case': 'The server is switching protocols according to the Upgrade header field.',
        'suggested_action': 'No specific action required.',
        'rfc_reference': 'RFC 7231, Section 6.2.2',
    },
    102: {
        'description': 'Processing',
        'category': 'Informational',
        'use_case': 'The server has received and is processing the request, but no response is available yet.',
        'suggested_action': 'Wait for a final response.',
        'rfc_reference': 'RFC 2518, Section 10.1',
    },
    103: {
        'description': 'Early Hints',
        'category': 'Informational',
        'use_case': 'Indicates that the server is likely to send a 1xx response with additional headers, prior to the actual response.',
        'suggested_action': 'Process the additional headers as appropriate.',
        'rfc_reference': 'RFC 8297',
    },
    200: {
        'description': 'OK',
        'category': 'Successful',
        'use_case': 'The request has been successfully processed, and the server is sending the response.',
        'suggested_action': 'Display the received content to the user.',
        'rfc_reference': 'RFC 7231, Section 6.3.1',
    },
    201: {
        'description': 'Created',
        'category': 'Successful',
        'use_case': 'The request has been fulfilled, resulting in the creation of a new resource.',
        'suggested_action': 'The newly created resource can be referenced in the response.',
        'rfc_reference': 'RFC 7231, Section 6.3.2',
    },
    202: {
        'description': 'Accepted',
        'category': 'Successful',
        'use_case': 'The request has been accepted for processing, but the processing has not been completed.',
        'suggested_action': 'No specific action required.',
        'rfc_reference': 'RFC 7231, Section 6.3.3',
    },
    204: {
        'description': 'No Content',
        'category': 'Successful',
        'use_case': 'The request has been successfully processed, but there is no content to return.',
        'suggested_action': 'No specific action required.',
        'rfc_reference': 'RFC 7231, Section 6.3.5',
    },
    206: {
        'description': 'Partial Content',
        'category': 'Successful',
        'use_case': 'The server is delivering only part of the resource due to a range request.',
        'suggested_action': 'Use the received content as appropriate.',
        'rfc_reference': 'RFC 7233, Section 4.1',
    },
    300: {
        'description': 'Multiple Choices',
        'category': 'Redirection',
        'use_case': 'The request has multiple possible responses, and the client should choose one.',
        'suggested_action': 'Select a response based on client preferences.',
        'rfc_reference': 'RFC 7231, Section 6.4.1',
    },
    301: {
        'description': 'Moved Permanently',
        'category': 'Redirection',
        'use_case': 'The requested resource has been permanently moved to a different URL.',
        'suggested_action': 'Update bookmarks or links to the new URL.',
        'rfc_reference': 'RFC 7231, Section 6.4.2',
    },
    302: {
        'description': 'Found',
        'category': 'Redirection',
        'use_case': 'The requested resource temporarily resides under a different URL.',
        'suggested_action': 'Follow the redirection to the new URL if necessary.',
        'rfc_reference': 'RFC 7231, Section 6.4.3',
    },
    303: {
        'description': 'See Other',
        'category': 'Redirection',
        'use_case': 'The response to the request can be found under a different URL.',
        'suggested_action': 'Follow the redirection to the new URL using a GET request.',
        'rfc_reference': 'RFC 7231, Section 6.4.4',
    },
    304: {
        'description': 'Not Modified',
        'category': 'Redirection',
        'use_case': 'The resource has not been modified since the last request.',
        'suggested_action': 'Use a cached copy if available.',
        'rfc_reference': 'RFC 7232, Section 4.1',
    },
    307: {
        'description': 'Temporary Redirect',
        'category': 'Redirection',
        'use_case': 'The request should be repeated with the same method and is expected to be repeated with the same method.',
        'suggested_action': 'Repeat the request to the original URL with the same method.',
        'rfc_reference': 'RFC 7231, Section 6.4.7',
    },
    308: {
        'description': 'Permanent Redirect',
        'category': 'Redirection',
        'use_case': 'The request should be repeated with the same method and is expected to be repeated with the same method.',
        'suggested_action': 'Repeat the request to the original URL with the same method.',
        'rfc_reference': 'RFC 7538',
    },
    400: {
        'description': 'Bad Request',
        'category': 'Client Error',
        'use_case': 'The server cannot understand or process the client\'s request due to malformed syntax.',
        'suggested_action': 'Check the request for syntax errors or invalid parameters.',
        'rfc_reference': 'RFC 7231, Section 6.5.1',
    },
    401: {
        'description': 'Unauthorized',
        'category': 'Client Error',
        'use_case': 'The request requires user authentication or authorization.',
        'suggested_action': 'Provide valid credentials and retry the request.',
        'rfc_reference': 'RFC 7235, Section 3.1',
    },
    402: {
        'description': 'Payment Required',
        'category': 'Client Error',
        'use_case': 'This status code is reserved for future use.',
        'suggested_action': 'No specific action required.',
        'rfc_reference': 'RFC 7231, Section 6.5.2',
    },
    403: {
        'description': 'Forbidden',
        'category': 'Client Error',
        'use_case': 'The server understood the request but refuses to fulfill it.',
        'suggested_action': 'Contact the server administrator or request access if necessary.',
        'rfc_reference': 'RFC 7231, Section 6.5.3',
    },
    404: {
        'description': 'Not Found',
        'category': 'Client Error',
        'use_case': 'The server has not found the requested resource.',
        'suggested_action': 'Check the URL for errors or verify resource availability.',
        'rfc_reference': 'RFC 7231, Section 6.5.4',
    },
    405: {
        'description': 'Method Not Allowed',
        'category': 'Client Error',
        'use_case': 'The method specified in the request is not allowed for the resource identified by the request URI.',
        'suggested_action': 'Use an allowed HTTP method for the resource.',
        'rfc_reference': 'RFC 7231, Section 6.5.5',
    },
    406: {
        'description': 'Not Acceptable',
        'category': 'Client Error',
        'use_case': 'The server cannot produce a response matching the list of acceptable values defined in the request\'s headers.',
        'suggested_action': 'Review and modify the request headers to specify acceptable values.',
        'rfc_reference': 'RFC 7231, Section 6.5.6',
    },
    407: {
        'description': 'Proxy Authentication Required',
        'category': 'Client Error',
        'use_case': 'The client must first authenticate itself with the proxy.',
        'suggested_action': 'Provide valid proxy authentication credentials.',
        'rfc_reference': 'RFC 7235, Section 3.2',
    },
    408: {
        'description': 'Request Timeout',
        'category': 'Client Error',
        'use_case': 'The server timed out waiting for the request.',
        'suggested_action': 'Retry the request after checking the connection and server availability.',
        'rfc_reference': 'RFC 7231, Section 6.5.7',
    },
    409: {
        'description': 'Conflict',
        'category': 'Client Error',
        'use_case': 'Indicates that the request could not be completed due to a conflict with the current state of the target resource.',
        'suggested_action': 'Resolve the conflict and retry the request if applicable.',
        'rfc_reference': 'RFC 7231, Section 6.5.8',
    },
    410: {
        'description': 'Gone',
        'category': 'Client Error',
        'use_case': 'The requested resource is no longer available at the server and no forwarding address is known.',
        'suggested_action': 'Remove references to the resource or update links.',
        'rfc_reference': 'RFC 7231, Section 6.5.9',
    },
    411: {
        'description': 'Length Required',
        'category': 'Client Error',
        'use_case': 'The server requires a content-length header for this request.',
        'suggested_action': 'Include the content-length header in the request.',
        'rfc_reference': 'RFC 7231, Section 6.5.10',
    },
    412: {
        'description': 'Precondition Failed',
        'category': 'Client Error',
        'use_case': 'One or more conditions specified in the request header fields evaluated to false when tested on the server.',
        'suggested_action': 'Adjust the request header fields or remove conditions that are not met.',
        'rfc_reference': 'RFC 7232, Section 4.2',
    },
    413: {
        'description': 'Payload Too Large',
        'category': 'Client Error',
        'use_case': 'The server refuses to process the request because the payload is too large.',
        'suggested_action': 'Reduce the request payload size or use a different method.',
        'rfc_reference': 'RFC 7231, Section 6.5.11',
    },
    414: {
        'description': 'URI Too Long',
        'category': 'Client Error',
        'use_case': 'The server refuses to process the request because the URI is too long.',
        'suggested_action': 'Shorten the URI or use a different method.',
        'rfc_reference': 'RFC 7231, Section 6.5.12',
    },
    415: {
        'description': 'Unsupported Media Type',
        'category': 'Client Error',
        'use_case': 'The server refuses to process the request because the media type is not supported.',
        'suggested_action': 'Use a supported media type in the request headers.',
        'rfc_reference': 'RFC 7231, Section 6.5.13',
    },
    416: {
        'description': 'Range Not Satisfiable',
        'category': 'Client Error',
        'use_case': 'The server cannot satisfy the request''s Range header field.',
        'suggested_action': 'Adjust the Range header field to a valid range.',
        'rfc_reference': 'RFC 7233, Section 4.4',
    },
    417: {
        'description': 'Expectation Failed',
        'category': 'Client Error',
        'use_case': 'The server cannot meet the requirements specified in the Expect request header field.',
        'suggested_action': 'Review and adjust the Expect request header field.',
        'rfc_reference': 'RFC 7231, Section 6.5.14',
    },
    421: {
        'description': 'Misdirected Request',
        'category': 'Client Error',
        'use_case': 'The request was directed at a server that is not able to produce a response.',
        'suggested_action': 'Verify the request target and retry the request if necessary.',
        'rfc_reference': 'RFC 7540, Section 9.1.2',
    },
    422: {
        'description': 'Unprocessable Entity',
        'category': 'Client Error',
        'use_case': 'The server understands the request but cannot process it due to semantic errors.',
        'suggested_action': 'Review and correct the request to resolve semantic errors.',
        'rfc_reference': 'RFC 4918, Section 11.2',
    },
    423: {
        'description': 'Locked',
        'category': 'Client Error',
        'use_case': 'The resource that is being accessed is locked.',
        'suggested_action': 'Wait for the resource to be unlocked or use a different request.',
        'rfc_reference': 'RFC 4918, Section 11.3',
    },
    424: {
        'description': 'Failed Dependency',
        'category': 'Client Error',
        'use_case': 'The method could not be performed on the resource because the requested action depended on another action and that action failed.',
        'suggested_action': 'Resolve the dependency issue and retry the request if applicable.',
        'rfc_reference': 'RFC 4918, Section 11.4',
    },
    425: {
        'description': 'Too Early',
        'category': 'Client Error',
        'use_case': 'The server is unwilling to risk processing a request that might be replayed.',
        'suggested_action': 'Wait and retry the request at a later time.',
        'rfc_reference': 'RFC 8470',
    },
    426: {
        'description': 'Upgrade Required',
        'category': 'Client Error',
        'use_case': 'The server refuses to perform the request using the current protocol but may do so after the client upgrades to a different protocol.',
        'suggested_action': 'Upgrade the client to a different protocol and retry the request.',
        'rfc_reference': 'RFC 2817',
    },
    428: {
        'description': 'Precondition Required',
        'category': 'Client Error',
        'use_case': 'The server requires the request to be conditional.',
        'suggested_action': 'Include a conditional header field in the request.',
        'rfc_reference': 'RFC 6585, Section 3',
    },
    429: {
        'description': 'Too Many Requests',
        'category': 'Client Error',
        'use_case': 'The user has sent too many requests in a given amount of time.',
        'suggested_action': 'Reduce the rate of requests or wait for the rate limit to reset.',
        'rfc_reference': 'RFC 6585, Section 4',
    },
    431: {
        'description': 'Request Header Fields Too Large',
        'category': 'Client Error',
        'use_case': 'The server is unwilling to process the request because its header fields are too large.',
        'suggested_action': 'Reduce the size of request header fields.',
        'rfc_reference': 'RFC 6585, Section 5',
    },
    451: {
        'description': 'Unavailable For Legal Reasons',
        'category': 'Client Error',
        'use_case': 'Indicates that the server is denying access to the resource as a legal demand.',
        'suggested_action': 'Review and address the legal reasons for denial.',
        'rfc_reference': 'RFC 7725',
    },
    500: {
        'description': 'Internal Server Error',
        'category': 'Server Error',
        'use_case': 'A generic error message indicating that something went wrong on the server.',
        'suggested_action': 'Contact the website administrator or support team for assistance.',
        'rfc_reference': 'RFC 7231, Section 6.6.1',
    },
    501: {
        'description': 'Not Implemented',
        'category': 'Server Error',
        'use_case': 'The server does not support the functionality required to fulfill the request.',
        'suggested_action': 'Check the server''s capabilities or report the issue to the server administrator.',
        'rfc_reference': 'RFC 7231, Section 6.6.2',
    },
    502: {
        'description': 'Bad Gateway',
        'category': 'Server Error',
        'use_case': 'The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed.',
        'suggested_action': 'Check the configuration or status of the upstream server.',
        'rfc_reference': 'RFC 7231, Section 6.6.3',
    },
    503: {
        'description': 'Service Unavailable',
        'category': 'Server Error',
        'use_case': 'The server is temporarily unable to handle the request due to maintenance or overload.',
        'suggested_action': 'Retry the request after a delay or seek alternative resources.',
        'rfc_reference': 'RFC 7231, Section 6.6.4',
    },
    504: {
        'description': 'Gateway Timeout',
        'category': 'Server Error',
        'use_case': 'The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server or some other auxiliary server.',
        'suggested_action': 'Check the configuration or status of the upstream server or try the request again.',
        'rfc_reference': 'RFC 7231, Section 6.6.5',
    },
    505: {
        'description': 'HTTP Version Not Supported',
        'category': 'Server Error',
        'use_case': 'The server does not support the HTTP protocol version used in the request.',
        'suggested_action': 'Upgrade the HTTP protocol version or use a different version that is supported by the server.',
        'rfc_reference': 'RFC 7231, Section 6.6.6',
    },
    506: {
        'description': 'Variant Also Negotiates',
        'category': 'Server Error',
        'use_case': 'The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.',
        'suggested_action': 'Check the server''s' 'configuration.',
        'rfc_reference': 'RFC 2295, Section 8.1',
    },
    507: {
        'description': 'Insufficient Storage',
        'category': 'Server Error',
        'use_case': 'The server is unable to store the representation needed to complete the request.',
        'suggested_action': 'Free up server storage or allocate more storage as needed.',
        'rfc_reference': 'RFC 4918, Section 11.5',
    },
    508: {
        'description': 'Loop Detected',
        'category': 'Server Error',
        'use_case': 'The server detected an infinite loop while processing the request.',
        'suggested_action': 'Review and modify the request to resolve the loop.',
        'rfc_reference': 'RFC 5842, Section 7.2',
    },
    510: {
        'description': 'Not Extended',
        'category': 'Server Error',
        'use_case': 'Further extensions to the request are required for the server to fulfill it.',
        'suggested_action': 'Check if the server supports the necessary extensions and add them to the request.',
        'rfc_reference': 'RFC 2774, Section 7',
    },
    511: {
        'description': 'Network Authentication Required',
        'category': 'Server Error',
        'use_case': 'The client needs to authenticate to gain network access.',
        'suggested_action': 'Provide valid network authentication credentials.',
        'rfc_reference': 'RFC 6585, Section 6',
    },
    599: {
        'description': 'Network Connect Timeout Error',
        'category': 'Server Error',
        'use_case': 'This status code is not specified by any RFC but is sometimes used to represent network connect timeout errors.',
        'suggested_action': 'Check network connectivity and retry the request.',
        'rfc_reference': 'Not specified by RFC',
    }
    # Add more status codes with category, use case, suggested_action, and rfc_reference here as needed
}

# Function to display status code information
def display_status_code_info(code_info):
    print(f'Status Code {code_info["code"]}: {code_info["description"]}')
    print(f'Category: {code_info["category"]}')
    print(f'Use Case: {code_info["use_case"]}')
    print(f'Suggested Action: {code_info["suggested_action"]}')
    print(f'RFC Reference: {code_info["rfc_reference"]}')
    print("\n")

# User input
page_size = 5  # Number of status codes to display per page
current_page = 1  # Start with the first page
matching_statuses = []

# User input
page_size = 5  # Number of status codes to display per page
current_page = 1  # Start with the first page
matching_statuses = []

while True:
    try:
        print("\nOptions:")
        print("1. Lookup by status code")
        print("2. Lookup by description")
        print("3. Search by RFC reference")
        print("4. Next Page")
        print("5. Previous Page")
        print("6. Exit")
        option = int(input('Select an option: '))

        if option == 1:
            status_code = int(input('Enter an HTTP status code: '))
            info = http_status_codes.get(status_code, {'description': 'Unknown'})
            display_status_code_info({"code": status_code, **info})
        elif option == 2:
            description = input('Enter a description or part of a description: ').lower()
            matching_statuses = [
                {"code": code, **info} 
                for code, info in http_status_codes.items() if description in info['description'].lower()
            ]
            if matching_statuses:
                for code_info in matching_statuses:
                    display_status_code_info(code_info)
            else:
                print("No matching status codes found.")
        elif option == 3:
            rfc_reference = input('Enter an RFC reference: ').lower()
            matching_statuses = [
                {"code": code, **info}
                for code, info in http_status_codes.items() if rfc_reference in info['rfc_reference'].lower()
            ]
            if matching_statuses:
                for code_info in matching_statuses:
                    display_status_code_info(code_info)
            else:
                print("No matching status codes found.")
        elif option == 4:
            current_page += 1
        elif option == 5:
            current_page = max(1, current_page - 1)
        elif option == 6:
            break
        else:
            print('Invalid option. Please select a valid option.')
            continue

        # Pagination logic
        total_pages = (len(matching_statuses) + page_size - 1) // page_size
        if current_page > total_pages:
            current_page = total_pages
        if matching_statuses:
            start_idx = (current_page - 1) * page_size
            end_idx = min(start_idx + page_size, len(matching_statuses))
            print(f"Page {current_page}/{total_pages}:\n")
            for code_info in matching_statuses[start_idx:end_idx]:
                display_status_code_info(code_info)
        else:
            print("No matching status codes found.")

    except ValueError:
        print('Invalid input. Please enter a valid HTTP status code, option, or search term.')
