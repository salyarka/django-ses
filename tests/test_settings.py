from django.test import TestCase
from django.conf import settings
from tests.utils import unload_django_ses


class SettingsImportTest(TestCase):
    def test_aws_access_key_given(self):
        settings.AWS_ACCESS_KEY_ID = "Yjc4MzQ4MGYzMTBhOWY3ODJhODhmNTBkN2QwY2IyZTdhZmU1NDM1ZQo"
        settings.AWS_SECRET_ACCESS_KEY = "NTBjYzAzNzVlMTA0N2FiMmFlODlhYjY5OTYwZjNkNjZmMWNhNzRhOQo"
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.ACCESS_KEY, settings.AWS_ACCESS_KEY_ID)
        self.assertEqual(django_ses.settings.SECRET_KEY, settings.AWS_SECRET_ACCESS_KEY)

    def test_ses_access_key_given(self):
        settings.AWS_SES_ACCESS_KEY_ID = "YmM2M2QwZTE3ODk3NTJmYzZlZDc1MDY0ZmJkMDZjZjhmOTU0MWQ4MAo"
        settings.AWS_SES_SECRET_ACCESS_KEY = "NDNiMzRjNzlmZGU0ZDAzZTQxNTkwNzdkNWE5Y2JlNjk4OGFkM2UyZQo"
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.ACCESS_KEY, settings.AWS_SES_ACCESS_KEY_ID)
        self.assertEqual(django_ses.settings.SECRET_KEY, settings.AWS_SES_SECRET_ACCESS_KEY)

    def test_aws_session_token_given(self):
        settings.AWS_SESSION_TOKEN = "FwoGZXIvYXdzED8aDAILqEtZvcDCx+KsFCK1AUwcLbm4d+mAlRWYN+r1adKoIfwe/T117KNcql" \
            "fbFFc6lgM1BQk9RepOZOyhNnx1ji12BMnA+Sc/9H1gi/QRt51U0EQVhcT7i9YZbipzrYMLpvxe0dwXwC7MTy7NQRkEMhpyXWgFw4Wz+" \
            "pHdZTFI4DOEhjf/t1FcuV2jX0oS0Eqqck2YB6yY03FpQRFVFIKUFcyvt9kMP9F77iHkgnEWBxOVcfSxBHfgQDTCHCecMNDN02/u628o" \
            "xK6elAYyLZu54kuwLAbe3hD2++FpbjCSF88DFWESks8o2PP489XCCCJrX/SnurGNfeWifA=="
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.SESSION_TOKEN, settings.AWS_SESSION_TOKEN)

    def test_ses_session_token_given(self):
        settings.AWS_SES_SESSION_TOKEN = "FwoGZXIvYXdzEB4aDAU4Z6TKwwidfBNJHCK1AcWwz1WuzumwEftz8hpe55Z5u6e1APH2K71UEbJBAl" \
            "cgplAm+W8Bd7puHqMeYVMCFy8o3B9Wx/Ry6fGlY76LIqrX9VrSD6C/f914fqgK4CyrYRPd/Zh+Z4QrCLWaJboj6eOwOU2AuOCF3epfy" \
            "C7yOmHPIR0oY3mYB32g9kUVyK7E/6nfiPcGEZQTwUd19sa3qeJwkTT0suZKSEbXhuLqw9aGwcl6VvsWfG8xQXA8aSd6gTnAH7Qo0pqT" \
            "jQYyLYI7nmsYjpQa2aynxovr7rwKrj71PQstMbK2oKwaT1FzasM0hjs+C5uLhdEjuA=="
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.SESSION_TOKEN, settings.AWS_SES_SESSION_TOKEN)

    def test_ses_configuration_set_given(self):
        settings.AWS_SES_CONFIGURATION_SET = "test-set"
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.AWS_SES_CONFIGURATION_SET, settings.AWS_SES_CONFIGURATION_SET)

    def test_ses_region_to_endpoint_default_given(self):
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.AWS_SES_REGION_NAME, 'us-east-1')
        self.assertEqual(django_ses.settings.AWS_SES_REGION_ENDPOINT, f'email.{django_ses.settings.AWS_SES_REGION_NAME}.amazonaws.com')

    def test_ses_region_to_endpoint_set_given(self):
        settings.AWS_SES_REGION_NAME = 'eu-west-1'
        unload_django_ses()
        import django_ses
        self.assertEqual(django_ses.settings.AWS_SES_REGION_NAME, 'eu-west-1')
        self.assertEqual(django_ses.settings.AWS_SES_REGION_ENDPOINT, 'email.eu-west-1.amazonaws.com')