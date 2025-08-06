from selene import browser, have, be
from selene.core.query import value

from demo_qa_test import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').type(value)

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').type(value)

    def fill_birthday(self, month, year, day):
        browser.element('[id = "dateOfBirthInput"]').click()
        browser.all('.react-datepicker__month-select option').element_by(have.exact_text(month)).click()
        browser.all('.react-datepicker__year-select option').element_by(have.exact_text(year)).click()
        browser.element(f'[aria-label="Choose Saturday, August {day}th, 1995"]').should(be.visible).click()

    def fill_email(self, email):
        browser.element('[id="userEmail"]').type(email)


def test_form_submission(setup_browser):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Carla')
    registration_page.fill_last_name('Johnson')
    registration_page.fill_email('Johnson@gmail.pom')

    #registration_page.set_gender()

    browser.element('//input[@name="gender" and @value="Female"]/following-sibling::label').click()
    browser.element('[id="userNumber"]').type('7788995511')

    browser.execute_script('window.scrollBy(0, 500)')

    registration_page.fill_birthday('August', '1995', '5')


    browser.element('[id="subjectsInput"]').type('Maths').press_enter()
    browser.element('#subjectsInput').type('p')
    browser.all('.subjects-auto-complete__menu div').element_by(have.exact_text('Physics')).click()

    browser.element('//*[@id="hobbiesWrapper"]//label[contains(text(),"Reading")]').click()

    browser.element('[id="uploadPicture"]').send_keys(resource.path('Screenshot_2368.png'))

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
