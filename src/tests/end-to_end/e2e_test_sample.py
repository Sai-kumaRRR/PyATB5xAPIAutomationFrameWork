import allure
import pytest


class TestE2E(object):

    @allure.title("E2E - Create Booking -> update -> Delete(Verify)")
    @allure.description("Verify that created booking id when we update we are able to update")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1",name="E2ETC1")
    def test_update_booking_with_id_token(self):
        pass

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description("Verify booking gets deleted with the booking ID and token")
    def test_delete_booking_id(self):
        pass