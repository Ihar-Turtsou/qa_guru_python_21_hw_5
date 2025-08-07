from demo_qa_test.pages.registration_page import RegistrationPage


def test_form_submission(setup_browser):
    registration_page = RegistrationPage()

    registration_page.open()
    (
    registration_page
    .fill_first_name('Carla')
    .fill_last_name('Johnson')
    .fill_email('Johnson@gmail.pom')
    .set_gender("Female")
    .fill_phone_number('7788995511')
    .fill_birthday('August', '1995', '5')
    .set_subject_by_enter('Maths')
    .set_subject_by_click('p', 'Physics')
    .set_hobby("Reading")
    .upload_picture('Screenshot_2368.png')
    .fill_current_address('South Street PA Philadelphia 19147')
    .choose_location('Haryana', 'Panipat')
    .submit_form()
    )

    registration_page.should_registred_user_with(
            'Carla Johnson',
            'Johnson@gmail.pom',
            'Female',
            '7788995511',
            '05 August,1995',
            'Maths, Physics',
            'Reading',
            'Screenshot_2368.png',
            'South Street PA Philadelphia 19147',
            'Haryana Panipat'
                                                 )
    print('test finished')
    # breakpoint()
