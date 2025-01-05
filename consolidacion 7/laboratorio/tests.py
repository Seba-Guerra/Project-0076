from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

# Create your tests here.


class LaboratorioModelTests(TestCase):

    @classmethod 
    def setUpTestData(cls):  
    # Crear un laboratorio para usar en todas las pruebas 
        cls.laboratorio = Laboratorio.objects.create( 
            nombre='Laboratorio de Prueba', 
            ciudad='Ciudad de Prueba', 
            pais='Pais de Prueba'
    ) 
    def test_data_matches(self): 
        """Verificar que los datos en la base de datos simulada coincidan con los datos creados en setUpTestData.""" 
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id) 
        self.assertEqual(laboratorio.nombre, 'Laboratorio de Prueba') 
        self.assertEqual(laboratorio.ciudad, 'Ciudad de Prueba') 
        self.assertEqual(laboratorio.pais, 'Pais de Prueba')
    
    def test_url_exists_at_desired_location(self): 
        """Confirmar que la URL retorna una respuesta HTTP 200 para el laboratorio.""" 
        response = self.client.get(f'/laboratorio/{self.laboratorio.id}/') 
        self.assertEqual(response.status_code, 200) 
        
    def test_url_accessible_by_name(self): 
        """Asegurarse de que la página usando reverse para llamar al nombre de la URL retorna una respuesta HTTP 200.""" 
        response = self.client.get(reverse('laboratorio_detail', args=[self.laboratorio.id])) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html') 
        self.assertContains(response, 'Laboratorio de Prueba')
