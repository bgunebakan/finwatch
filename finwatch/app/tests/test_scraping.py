from django.test import TestCase
from app.tasks import scrape_stocks


class ScrapingTestCase(TestCase):

    def testNoError(self):
        """Test that the ``scrape_stocks`` task runs with no errors,"""
        result = scrape_stocks.delay()

        # check task finished succesfully
        self.assertEquals(result.get(), "Scheduled task done")
        self.assertTrue(result.successful())
