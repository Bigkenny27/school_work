import person
print(f"dingus prime {chr(0x1F384)}")
# adding new people
person1 = person.Person("John Doe", 2005)
person2 = person.Person("big johnny", 19)
person3_neg_year = person.Person("dingus prime", -1)
person4_single_name = person.Person("smartass", 2002)
person5_double_fault = person.Person("idiot", 2342)

# name tests
print("Starting name tests")
assert person1.get_full_name() == "John Doe", print("Testcase 1 FAILED; Person 1 does not have the correct name")
assert person3_neg_year.get_full_name() == "dingus prime", (
    print("Testcase 2 FAILED; Person 3 does not have the correct name"))
assert person4_single_name.get_full_name() == "Guy Incognito", (
    print("Testcase 3 FAILED; Person 4 has an incorrect name yet name does not become Guy Incognito"))
assert person5_double_fault.get_full_name() == "Guy Incognito", (
    print("Testcase 5 FAILED; incorrect name does not result in Guy Incognito"))
print("Name tests passed!")

# year tests
print("Starting year tests")
assert person1.get_year() == 2005, print("Testcase 6 FAILED; Person 1 does not have the correct year")
assert person3_neg_year.get_year() == 2000, print("Testcase 7 FAILED; invalid year does not result in a year change to 2000")
assert person5_double_fault.get_year() == 2000, print("Testcase 8 FAILED; invalid year does not result in a year change to 2000")
print("Year tests passed!")
# ID tests

print("Starting ID tests")
assert person1.get_id() == 1, print("Testcase 9 FAILED; incorrect ID")
assert person2.get_id() == 2, print("Testcase 10 FAILED; incorrect ID")
assert person3_neg_year.get_id() == 3, print("Testcase 11 FAILED; incorrect ID")
assert person4_single_name.get_id() == 4, print("Testcase 12 FAILED; incorrect ID")
assert person5_double_fault.get_id() == 5, print("Testcase 13 FAILED; incorrect ID")
print("ID tests passed!")

# -------------------- Method Testing -----------------------

print("starting __str__ tests")
print(person1)
assert str(person1) == "1: John Doe, 2005", print("__str__ test 1 FAILED; incorrect print")
assert str(person2) == "2: big johnny, 19", print("__str__ test 2 FAILED; incorrect print")
assert str(person5_double_fault) == "5: Guy Incognito, 2000", print("__str__ test 3 FAILED; incorrect print")
print("__str__ tests passed!")

print("starting get_age tests")
assert person1.get_age() == 15, print("get_age test 1 FAILED; incorrect age")
assert person3_neg_year.get_age() == 20, print("get_age test 2 FAILED; incorrect age")
print("get_age tests passed!")

print("starting get_friendly_name tests")
assert person1.get_friendly_name() == "John", print("get_friendly_name test 1 FAILED; not returning first name")
assert person3_neg_year.get_friendly_name() == "dingus", print("get_friendly_name test 2 FAILED; not returning first name")
assert person5_double_fault.get_friendly_name() == "Guy", print("get_friendly_name test 3 FAILED; not returning first name")
print("get_friendly_name tests passed!")

print("Starting christmas tests")
person.Person.celebrate_new_year()
assert person4_single_name.is_christmas, print("is_christmas is showing False after celebrate_new_year")
assert person5_double_fault.current_year == 2021, print("celebrate new year is not incrementing current_year")
assert person3_neg_year.get_friendly_name() == f"dingus {chr(0x1F384)}"
assert person5_double_fault.get_friendly_name() == f"Guy {chr(0x1F384)}"
print("Christmas tests passed!")

print("Starting go_back_to_work tests")
person.Person.go_back_to_work()
assert person2.is_christmas is False, print("go_back_to_work is not changing christmas to False")
assert person4_single_name.current_year == 2021, print("go_back_to_work is somehow changing the year")
assert person1.get_friendly_name() == "John"

print("All tests passed!")



