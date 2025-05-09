from utilities.testing import APIViewTestCases

from ...models import Delivery, Purchase, Supplier
from ..custom import APITestCase


class DeliveryTest(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
):
    model = Delivery
    brief_fields = ['date', 'description', 'display', 'id', 'name', 'url']

    bulk_update_data = {
        'description': 'new description',
    }

    @classmethod
    def setUpTestData(cls) -> None:
        supplier1 = Supplier.objects.create(name='Supplier1', slug='supplier1')
        purchase1 = Purchase.objects.create(
            name='Purchase1', supplier=supplier1, status='closed'
        )
        Delivery.objects.create(name='Delivery 1', purchase=purchase1)
        Delivery.objects.create(name='Delivery 2', purchase=purchase1)
        Delivery.objects.create(name='Delivery 3', purchase=purchase1)
        cls.create_data = [
            {
                'name': 'Delivery 4',
                'purchase': purchase1.pk,
            },
            {
                'name': 'Delivery 5',
                'purchase': purchase1.pk,
            },
            {
                'name': 'Delivery 6',
                'purchase': purchase1.pk,
            },
        ]
