from selene import browser, have, be, by
from demo_qa_test import resource
from demo_qa_test.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('[id="firstName"]')
        self.last_name = browser.element('[id="lastName"]')
        self.user_email = browser.element('[id="userEmail"]')
        self.user_gender = browser.element('#genterWrapper')
        self.user_phone_nuber = browser.element('[id="userNumber"]')
        self.date_of_birth = browser.element('[id = "dateOfBirthInput"]')
        self.month_of_birth = browser.all('.react-datepicker__month-select option')
        self.year_of_birth = browser.all('.react-datepicker__year-select option')
        self.day_of_birth = browser.all('.react-datepicker__day:not(.react-datepicker__day--outside-month)')
        self.subject_enter = browser.element('[id="subjectsInput"]')
        self.subject_type = browser.element('#subjectsInput')
        self.subject_click = browser.all('.subjects-auto-complete__menu div')
        self.user_hobby = browser.element('#hobbiesWrapper')
        self.user_picture = browser.element('[id="uploadPicture"]')
        self.user_address = browser.element('[id="currentAddress"]')
        self.user_state = browser.element('#state input')
        self.user_city = browser.element('#city input')
        self.submit_button = browser.element('[id="submit"]')
        self.result_table = browser.all('tbody tr td:nth-child(2)')


    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('window.scrollBy(0, 500)')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, email):
        self.user_email.type(email)
        return self

    def set_gender(self, value):
        self.user_gender.element(by.text(value)).click()
        return self

    def fill_phone_number(self, value):
        self.user_phone_nuber.type(value)
        return self

    def fill_birthday(self, month, year, day):
        self.date_of_birth.click()
        self.month_of_birth.element_by(have.exact_text(month)).click()
        self.year_of_birth.element_by(have.exact_text(year)).click()
        self.day_of_birth.element_by(have.exact_text(str(int(day)))).click()
        return self

    def set_subject_by_enter(self, value):
        self.subject_enter.type(value).press_enter()
        return self

    def set_subject_by_click(self, type_letter, value):
        self.subject_type.type(type_letter)
        self.subject_click.element_by(have.exact_text(value)).click()
        return self

    def set_hobby(self, value):
        self.user_hobby.element(by.text(value)).click()
        return self

    def upload_picture(self, value):
        self.user_picture.send_keys(resource.path(value))
        return self

    def fill_current_address(self, value):
        self.user_address.set_value(value)
        return self

    def choose_location(self, state, city):
        self.user_state.type(state).press_enter()
        self.user_city.type(city).press_enter()
        return self

    def submit_form(self):
        self.submit_button.click()
        return self

    def should_have_registered(self,user: User):
        self.result_table.should(have.exact_texts(
            user.full_name,
            user.email,
            user.gender,
            user.phone_number,
            user.date_of_birth,
            user.subjects,
            user.hobby,
            user.file_name,
            user.address,
            user.state_city
        ))
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.set_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_birthday(*user.birthday)
        self.set_subject_by_enter(user.first_subject)
        self.set_subject_by_click(*user.second_subject)
        self.set_hobby(user.hobby)
        self.upload_picture(user.file_name)
        self.fill_current_address(user.address)
        self.choose_location(*user.user_location)
        self.submit_form()

