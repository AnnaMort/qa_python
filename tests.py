from main import BooksCollector

class TestBooksCollectogitr:
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мрачный жнец')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_for_value_from_permitted_range(self):
        collector_1 = BooksCollector()
        collector_1.add_new_book('Мрачный жнец')
        collector_1.set_book_rating('Мрачный жнец', 10)
        assert collector_1.books_rating.get('Мрачный жнец') in range(1,11)

    def test_get_book_rating_get_value_for_specific_book(self):
        collector_2 = BooksCollector()
        collector_2.add_new_book('Мрачный жнец')
        collector_2.set_book_rating('Мрачный жнец', 10)
        assert collector_2.get_book_rating('Мрачный жнец') == 10

    def test_get_books_with_specific_rating_result_for_rating_10_true(self):
        collector_3 = BooksCollector()
        collector_3.add_new_book('Мрачный жнец')
        collector_3.set_book_rating('Мрачный жнец', 10)
        assert collector_3.get_books_with_specific_rating(10) == ['Мрачный жнец']

    def test_get_books_rating_with_one_pair_book_and_rating(self):
        collector_4 = BooksCollector()
        collector_4.books_rating = {'Мрачный жнец':10}
        assert collector_4.get_books_rating() == collector_4.books_rating

    def test_add_book_in_favorites_presence_of_specific_book(self):
        collector_5 = BooksCollector()
        collector_5.add_new_book('Мрачный жнец')
        collector_5.add_book_in_favorites('Мрачный жнец')
        assert 'Мрачный жнец' in collector_5.favorites


    def test_delete_book_from_favorites_delete_specific_book_name_from_favorites(self):
        collector_6 = BooksCollector()
        collector_6.add_book_in_favorites('Мрачный жнец')
        collector_6.delete_book_from_favorites('Мрачный жнец')
        assert 'Мрачный жнец' not in collector_6.favorites

    def test_get_list_of_favorites_books_get_list_of_two_books(self):
        collector_7 = BooksCollector()
        collector_7.add_new_book('Мрачный жнец')
        collector_7.add_new_book('Санта-Хрякус')
        collector_7.add_book_in_favorites('Мрачный жнец')
        collector_7.add_book_in_favorites('Санта-Хрякус')
        assert len(collector_7.get_list_of_favorites_books()) == 2

