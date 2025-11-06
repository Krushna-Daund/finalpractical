import datetime

print("Running automated Python test")
print("Current time:", datetime.datetime.utcnow())

try:
    assert 2 + 2 == 4
    print("Test passed successful")
except AssertionError:
    print(" Test failed!")

print(" Test completed")
