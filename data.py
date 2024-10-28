class Data:
    login = 'NataLaktionova14'
    password = '123456'
    firstname = 'Natasha'
    correct_courier_info = {
    "login": "NataLaktionova14",
    "password": "123456",
    "firstName": "Natasha"
}
    courier_info_with_invalid_password = {'login': 'NatashaLaktionova14', 'password': '1222'}


class OrderData:
    Order_data_1_without_colors = {
        'firstName': 'Иван',
        'lastName': 'Ивановочкин',
        'address': 'Правды, 10',
        'metroStation': 9,
        'phone': '+79990001122',
        'rentTime': 2,
        'deliveryDate': '2024-11-11',
        'comment': 'Оставьте у двери',
        'color': []
    }

    Order_data_2_color_black = {
        'firstName': 'Джеймс',
        'lastName': 'Франклин',
        'address': ' Юрина 154',
        'metroStation': 11,
        'phone': '+79988776655',
        'rentTime': 3,
        'deliveryDate': '2024-12-12',
        'comment': 'Позвоните по телефону',
        'color': [
            'BLACK'
        ]
    }

    Order_data_3_colors_black_and_grey = {
        'firstName': 'Анастасия',
        'lastName': 'Иванова',
        'address': 'Баррикадная, 19',
        'metroStation': 15,
        'phone': '+70000001122',
        'rentTime': 1,
        'deliveryDate': '2024-11-30',
        'comment': 'Будьте вовремя!',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    Order_data_4_color_grey = {
        'firstName': 'Анна',
        'lastName': 'Михайлова',
        'address': ' Юрина 11',
        'metroStation': 11,
        'phone': '+71188116611',
        'rentTime': 4,
        'deliveryDate': '2024-11-13',
        'comment': 'Позвоните по другому телефону',
        'color': [
            'BLACK'
        ]
    }