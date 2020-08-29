data = {
    'students': [
        {
            'name': 'Salvador Vizcaino',
            'class': 2015,
            'scores': [10, 9.8, 7, 7.8, 10, 8.9]
        },
        {
            'name': 'Edgar Torres',
            'class': 2015,
            'scores': [10, 7, 8, 9.9, 10, 8.9]
        },
        {
            'name': 'Galileo Guzman',
            'class': 2015,
            'scores': [10, 8, 8, 6.9, 8.9, 8.9]
        },
        {
            'name': 'Liz Rueda',
            'class': 2015,
            'scores': [10, 8, 8, 6.9, 8.9, 8.9]
        },
        {
            'name': 'Met Velasquez',
            'class': 2015,
            'scores': [10, 10, 9.8, 9.9, 9.9, 8.9]
        }
    ]
}
print(type(data))
# students = data['ksstudents']
students = data.get('students', [])
print(students)