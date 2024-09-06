from django.test import SimpleTestCase
from django.urls import resolve, reverse
from todo.views import get_tasks, add_task, update_task, delete_task

class TestUrls(SimpleTestCase):
    
    def test_get_urls_resolved(self):
        url = reverse('get_tasks', args=[7]) # get_tasks - it`s name from params on urls.py
        # print(resolve(url))
        
        self.assertEqual(resolve(url).func, get_tasks) # get_tasks or another - you can take prom print(resolve(url))
            
    def test_add_urls_resolved(self):
        url = reverse('add_task', args=[7])
        # print(resolve(url))
        
        self.assertEqual(resolve(url).func, add_task) 
        
    def test_update_urls_resolved(self):
        url = reverse('update_task', args=[5])
        # print(resolve(url))
        
        self.assertEqual(resolve(url).func, update_task)
        
    def test_delete_urls_resolve(self):
        url = reverse('delete_task', args=[7])
        # print(resolve(url))
        
        self.assertEqual(resolve(url).func, delete_task)
