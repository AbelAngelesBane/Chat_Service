
from rest_framework import status

####################### STATUS CODES ############################
ok = status.HTTP_200_OK
wrong_input = status.HTTP_400_BAD_REQUEST
server_error = status.HTTP_500_INTERNAL_SERVER_ERROR
unauth = status.HTTP_401_UNAUTHORIZED
blank_content = status.HTTP_204_NO_CONTENT

########################## MESSAGES  ############################
wrong_query_vals_msg = "Incorrect value on Query parameter keys"
wrong_body_vals_msg = "Incorrect value on Body parameter keys"
wrong_url_vals_msg = "Incorrect value on URL parameter keys"
wrong_header_key_msg = "Incorrect value on Header keys"

inc_query_parameter_msg = "Incomplete Query parameters"
inc_url_parameter_msg = "Incomplete URL parameters"
inc_body_parameter_msg = "Incomplete Body key"
inc_parameter_msg = "Incomplete parameter"

unath_user_msg = "Unauthorized user"
secret_parameter_msg = "Secret parametereter is not provided"

############################ ERROR ############################
required_url_error = ["This url parameter is required"]
required_query_error = ["This query parameter is required"]
required_field_error = ["This field is required"]

null_field_error = ["Null value is not valid"]

invalid_time_error = ["Invalid time format"]
invalid_date_error = ["Invalid date format"]
invalid_choice_error = ["Invalid choice"]
invalid_value_error = ["The provided value is not valid"]
invalid_format_error = ["Invalid format"]
image_not_in_valid_file_error = ["File format invalid (png, jpg)"]
not_array_error = ["The Body key is not in array"]
not_dict_error = ["The Body key is not in hash map"]
unauth_access_error = ["Provided user is not privileged to acces this end-point"]
multi_file_error = ["Multiple files detected (select only one image file)"]

