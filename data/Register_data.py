from faker import Faker

faker = Faker(locale="fr_FR")


class registerData:

    @staticmethod
    def form_register():
        return{
        "firstName" : faker.first_name(),
        "lastName": faker.last_name(),
        "email": faker.email(),
        "telephone" : "0134874647",
        "password": "Test123!",
        "confirmPassword": "Test123!"
        }

    @staticmethod
    def form_register_failed():
        return{
        "firstName" : faker.first_name(),
        "lastName": faker.last_name(),
        "email": "guillaumeluce@example.org",
        "telephone" : "0134874647",
        "password": "Test123!",
        "confirmPassword": "Test123!"
        }

    @staticmethod
    def form_register_mdp_different():
        return {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "email": "guillaumeluce@example.org",
        "telephone": "0134874647",
        "password": "Test123!",
        "confirmPassword": "Test12333!"
        }