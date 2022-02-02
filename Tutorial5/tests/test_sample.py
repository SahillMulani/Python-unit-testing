import pytest
from datetime import datetime
from Tutorial5.myapp.sample import Sample


@pytest.fixture(scope="module")
def dummy_sample():
    return Sample("sahil",datetime(1998,11,18),"coe")

def test_get_age(dummy_sample):
    dummy_sample_age = (datetime.now() - dummy_sample.dob).days // 365
    assert dummy_sample.get_age() == dummy_sample_age

def test_add_credits(dummy_sample):
    dummy_sample.add_credits(5)
    assert dummy_sample.get_credits() == 5

def test_get_credits(dummy_sample):
    assert dummy_sample.get_credits() == 5