from django.test import TestCase

from .models import ImageDetail

# Create your tests here.


class ImageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.image = ImageDetail.objects.create(
            title='Peito de galinha',
            description='Peito de galinha com tomate',
            image_url='http://www.hojetemfrango.com.br/wp-content/uploads/2018/11/peito-de-frango-com-tomate-grape-e-azeitona-preta.jpg',
        )

    def test_image_model(self):
        self.assertEqual(self.image.title, 'Peito de galinha')
        self.assertEqual(self.image.description, 'Peito de galinha com tomate')
        self.assertEqual(
            self.image.image_url,
            'http://www.hojetemfrango.com.br/wp-content/uploads/2018/11/peito-de-frango-com-tomate-grape-e-azeitona-preta.jpg',
        )

    def test_repr_image_model(self):
        self.assertEqual(str(self.image), 'Peito de galinha')
