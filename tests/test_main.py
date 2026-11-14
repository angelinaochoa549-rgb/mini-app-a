import unittest

from main import PasswordOptions, generate_password


class GeneratePasswordTests(unittest.TestCase):
    def test_password_has_requested_length_and_every_selected_group(self) -> None:
        password = generate_password(PasswordOptions(length=24))

        self.assertEqual(len(password), 24)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in "!@#$%^&*()-_=+[]{};:,.?/|~" for char in password))

    def test_password_uses_only_selected_character_groups(self) -> None:
        password = generate_password(
            PasswordOptions(
                length=12,
                lowercase=False,
                uppercase=True,
                numbers=False,
                symbols=False,
            )
        )

        self.assertEqual(len(password), 12)
        self.assertTrue(password.isupper())

    def test_requires_at_least_one_character_group(self) -> None:
        with self.assertRaisesRegex(ValueError, "Selecciona al menos"):
            generate_password(
                PasswordOptions(
                    lowercase=False,
                    uppercase=False,
                    numbers=False,
                    symbols=False,
                )
            )

    def test_minimum_length_includes_all_four_selected_groups(self) -> None:
        password = generate_password(PasswordOptions(length=4))

        self.assertEqual(len(password), 4)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in "!@#$%^&*()-_=+[]{};:,.?/|~" for char in password))


if __name__ == "__main__":
    unittest.main()
