from Tutorial.myapp.sample import validate_age
import pytest

def test_validate_age_valid_age():
    validate_age(10)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError , match="Age canno be less than Zero") :
        validate_age(-1)
