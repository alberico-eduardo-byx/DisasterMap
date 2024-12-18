from django.test import TestCase
from ..models import Category, Event

class ModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(id="wildfires", name="Wildfires")
        self.event = Event.objects.create(
            id="EONET_111",
            category=self.category,
            title="Wildfire in TestCase 111",
            description="",
            date= "2024-12-13T19:00:00Z",
            country="Brazil",
            link="",
            sources=[
                {
                    "id": "GDACS",
                    "url": "https://www.gdacs.org/report.aspx?eventtype=WF&amp;eventid=1023069"
                }
            ],
            geometry=[
                {
                    "date": "2024-12-13T19:00:00Z",
                    "type": "Point",
                    "coordinates": [
                        12.542507299986001,
                        13.871897560840004
                    ],
                    "magnitudeUnit": None,
                    "magnitudeValue": None
                }
            ]
        )

    def test_category_str(self):
        self.assertEqual(str(self.category.name), "Wildfires")

    def test_event_str(self):
        self.assertEqual(str(self.event.title), "Wildfire in TestCase 111")

    def test_event_category_relationship(self):
        self.assertEqual(self.event.category, self.category)
        self.assertIn(self.event, self.category.events.all())