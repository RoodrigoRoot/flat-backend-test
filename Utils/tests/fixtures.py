import py
import pytest

@pytest.fixture()
def mock_all_branches():
    data = [
        {
            "name": "branch_b856",
            "commit": {
            "sha": "7513600a20c2913a326c945ddcd2fc234b848441",
            "url": "https://api.github.com/repos/RoodrigoRoot/flat-backend-test/commits/7513600a20c2913a326c945ddcd2fc234b848441"
            },
            "protected": False
        }
    ]
    return data

