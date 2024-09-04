from modules.amazonwebsite.amazon_register import Amazonwebsite

from resource.amazonwebsitelocators.amazonregisterlocator import *
import time

import pytest



@pytest.mark.usefixtures("get_driver")
class Testamazon:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.aw=Amazonwebsite(self.driver)

    def test_registeramazon(self):
        self.driver.get("https://www.amazon.com/ap/register?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Freport%2Finfringement&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_noticeform_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.aw.user_fnamelname(name=name)
        self.aw.user_email(email=email)
        self.aw.user_password(password=password)
        self.aw.user_recheck(password=password)
        self.aw.user_submit()
        time.sleep(10)