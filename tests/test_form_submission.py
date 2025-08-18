from pathlib import Path
from selene import browser, have, be, by

def test_form_submission(setup_browser):
    browser.open('/automation-practice-form')
    browser.execute_script('window.scrollBy(0, 550)')
    browser.element('[id="firstName"]').type('Carla')
    browser.element('[id="lastName"]').type('Johnson')
    browser.element('[id="userEmail"]').type('Johnson@gmail.pom')
    browser.element('#genterWrapper').element(by.text('Female')).click()
    browser.element('[id="userNumber"]').type('7788995511')

    browser.element('[id = "dateOfBirthInput"]').click()
    browser.all('.react-datepicker__month-select option').element_by(have.exact_text('August')).click()
    browser.all('.react-datepicker__year-select option').element_by(have.exact_text('1995')).click()
    browser.all(f'.react-datepicker__day:not(.react-datepicker__day--outside-month)').element_by(have.exact_text(str(int('5')))).click()

    browser.element('[id="subjectsInput"]').type('Maths').press_enter()
    browser.element('#subjectsInput').type('p')
    browser.all('.subjects-auto-complete__menu div').element_by(have.exact_text('Physics')).click()

    browser.element('#hobbiesWrapper').element(by.text('Reading')).click()

    browser.element('[id="uploadPicture"]').set_value(
        str((Path(__file__).parent / 'resources' / 'Screenshot_2368.png').absolute()))

    browser.element('[id="currentAddress"]').set_value('South Street, PA, Philadelphia, 19147')

    browser.element('#state input').type('Haryana').press_enter()
    browser.element('#city input').type('Panipat').press_enter()

    browser.element('[id="submit"]').click()

    browser.element('.table-responsive').all('tr').should(
        have.exact_texts(
            'Label Values',
            'Student Name Carla Johnson',
            'Student Email Johnson@gmail.pom',
            'Gender Female',
            'Mobile 7788995511',
            'Date of Birth 05 August,1995',
            'Subjects Maths, Physics',
            'Hobbies Reading',
            'Picture Screenshot_2368.png',
            'Address South Street, PA, Philadelphia, 19147',
            'State and City Haryana Panipat',
        )
    )
    print('test finished')
    # breakpoint()
