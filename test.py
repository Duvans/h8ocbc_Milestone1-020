import app

import unittest
from unittest import result
import director, movie
    

class TestDirector(unittest.TestCase):
    def test_read_all_director(self):
        '''test read all director function is return should be list type'''
        self.assertIs(type(director.read_all()),list)
    

class TestMovie(unittest.TestCase):
    def test_read_all_movie(self):
        '''test read all movie function is return should be list type'''
        self.assertIs(type(movie.read_all()),list)


class TestApi(unittest.TestCase):
    def test_get_all_director(self):
        '''Test get all data director'''
        client = app.connex_app.app.test_client()
        result = client.get('/api/director')

        self.assertEqual(result.status_code, 200)

    def test_get_all_director_with_pagination(self):
        '''
            test Get all director with pagination current page = 80 and data per page = 25
            api : /api/director/{page}/{per_page}
        '''
        client = app.connex_app.app.test_client()
        result = client.get('/api/director/50/20')
        # Make your assertions
        self.assertEqual(result.status_code, 200,'page in director/page/per_page must not exceed max page or data in database')

    def test_get_all_movie_with_pagination(self):
        '''
            test Get all movie with pagination current page = 80 and data per page = 25
            api : /api/movie/{page}/{per_page}
        '''
        client = app.connex_app.app.test_client()
        result = client.get('/api/movie/50/20')
        # Make your assertions
        self.assertEqual(result.status_code, 200,'current page must not exceed max page or data in database')

    def test_get_all_movie(self):
        '''Test Get All data Movie'''
        client = app.connex_app.app.test_client()
        result = client.get('/api/movie')
        # Make your assertions
        self.assertEqual(result.status_code, 200) 

    def test_get_movie_by_popularity(self):
        '''Test Get data Movie sorted by popularity'''
        client = app.connex_app.app.test_client()
        result = client.get('/api/movie/popularity')
        # Make your assertions
        self.assertEqual(result.status_code, 200) 


if __name__ == '__main__':
    unittest.main()
