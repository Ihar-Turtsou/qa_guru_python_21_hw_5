from demo_qa_test.data.users import User
from demo_qa_test.pages.registration_page import RegistrationPage


def test_form_submission(setup_browser):
    registration_page = RegistrationPage()
    carla = User(first_name='Carla',
                 last_name='Johnson',
                 email='Johnson@gmail.pom',
                 gender="Female",
                 phone_number='7788995511',
                 birthday=('August', '1995', '5'),
                 first_subject='Maths',
                 second_subject=('p', 'Physics'),
                 hobby="Reading",
                 file_name='Screenshot_2368.png',
                 address='South Street PA Philadelphia 19147',
                 user_location=('Haryana', 'Panipat')
                 )

    registration_page.open()
    registration_page.register(carla)
    registration_page.should_have_registered(carla)
    print('test finished')
    # breakpoint()
