# Common Verification

# HTTP Status code
#Headers
# Data Verification

# JSON schema

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "failed to match status code"


    def verify_response_key(key, expected_data):
        assert key == expected_data," Failed to match the key"



        def verify_json_key_not_null(key):
            assert key != 0 , "Failed key is null"

            def verify_json_key_gr_zero(key):
                assert key > 0, "Failed key is not > 0"
