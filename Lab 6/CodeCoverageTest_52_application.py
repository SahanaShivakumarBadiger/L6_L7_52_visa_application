
import pytest
from visa_application import visa_fee, documents_complete, application_status


# Tests for visa_fee()

def test_unknown_visa_type():
    with pytest.raises(ValueError):
        visa_fee("work", 2, "normal", "B")


def test_negative_entries():
    with pytest.raises(ValueError):
        visa_fee("tourist", -1, "normal", "B")


def test_included_entries():
    assert visa_fee("tourist", 1, "normal", "B") == 0


def test_nationality_group_a():
    assert visa_fee("tourist", 2, "normal", "A") == 0


def test_normal_speed():
    assert visa_fee("tourist", 2, "normal", "B") == 40


def test_express_speed():
    assert visa_fee("tourist", 2, "express", "B") == 100


def test_extra_entries_normal():
    assert visa_fee("tourist", 7, "normal", "B") == 360


def test_extra_entries_express():
    assert visa_fee("tourist", 7, "express", "B") == 780


# Tests for documents_complete()

def test_renewal_documents_complete():
    assert documents_complete(1, 0, True) is True


def test_insufficient_renewal_forms():
    assert documents_complete(0, 2, True) is False


def test_insufficient_photos():
    assert documents_complete(3, 1, False) is False


def test_non_renewal_documents_complete():
    assert documents_complete(3, 2, False) is True


def test_insufficient_forms():
    assert documents_complete(2, 2, False) is False


# Tests for application_status()

def test_express_application_open():
    assert application_status(10, True, False) == "open"


def test_normal_application_open():
    assert application_status(30, False, False) == "open"


def test_peak_season():
    assert application_status(45, False, True) == "open"


def test_application_closing():
    assert application_status(20, False, False) == "closing"


def test_application_closed():
    assert application_status(10, False, False) == "closed"
