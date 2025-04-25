from urllib import response

import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import delete_request, put_request
from src.helpers.common_verification import verify_http_status_code, verify_response_delete
from src.helpers.payload_manager import payload_update_booking
from src.utils.utils import Utils


def verify_response_key(param, param1):
    pass


class TestE2E(object):

    @allure.title("E2E - Create Booking -> update -> Delete(Verify)")
    @allure.description("Verify that created booking id when we update we are able to update")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2ETC1")
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(put_url)

        response = put_request(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        # verification here & more

    verify_http_status_code(response_data=response, expected_data=200)
    verify_response_key(response.json()["firstname"], "Amit")
    verify_response_key(response.json()["lastname"], "Brown")


@allure.title("Test CRUD operation Delete(delete)")
@allure.description("Verify booking gets deleted with the booking ID and token")
def test_delete_booking_id(self, create_token, get_booking_id):
    print(create_token, get_booking_id)
    booking_id = get_booking_id
    token = create_token

    delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
    response = delete_request(
        url=delete_url,
        headers=Utils().common_header_put_delete_patch_cookie(token=token),
        auth=None,
        in_json=False
    )
    verify_http_status_code(response_data=response, expected_data=201)
    verify_response_delete(response=response.text)
