import pytest

from scripts.util.param import get_CMTs_in_file, parse_header_line, CMT, get_available_CMTs


def test_get_CMTs_in_file(tmp_path):
    test_file_content = """
    // CMT01 // Boreal Black Spruce
    2.0               // rhq10:
    // CMT02 // Boreal White Spruce Forest
    2.0               // rhq10:
    // CMT03 // Boreal Deciduous Forest
    2.0               // rhq10:
    // CMT44 // Shrub Tundra Kougarok
    2.0               // rhq10:
    """

    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text(test_file_content)

    cmts_found = get_CMTs_in_file(temp_file)

    expected_cmts = [
        CMT(key='CMT01', num=1, name='Boreal Black Spruce', comment=''),
        CMT(key='CMT02', num=2, name='Boreal White Spruce Forest', comment=''),
        CMT(key='CMT03', num=3, name='Boreal Deciduous Forest', comment=''),
        CMT(key='CMT44', num=44, name='Shrub Tundra Kougarok', comment='')
    ]

    assert cmts_found == expected_cmts, "The CMTs found do not match the expected CMTs."


@pytest.mark.parametrize("header_line, expected_output", [
    ("// CMT07 // Heath Tundra - (ma....", ('CMT07', 'Heath Tundra', '(ma....')),
    ("// CMT07 // Heath Tundra // some other comment...", ('CMT07', 'Heath Tundra', 'some other comment...')),
    ("// CMT07 // Heath Tundra - some old style comment...", ('CMT07', 'Heath Tundra', 'some old style comment...'))
])
def test_parse_header_line(header_line, expected_output):
    cmt = parse_header_line(header_line)
    assert (cmt.key, cmt.name, cmt.comment) == expected_output, "The parsed header line does not match the expected output."


def test_get_available_CMTs(tmp_path):
    param_file_1 = tmp_path / "param1.txt"
    content_1 = """
    // CMT01 // Boreal Black Spruce
    2.0               // rhq10:
    // CMT02 // Boreal White Spruce Forest
    2.0               // rhq10:
    // CMT03 // Boreal Deciduous Forest
    2.0               // rhq10:
    // CMT44 // Shrub Tundra Kougarok
    2.0               // rhq10:
    """
    param_file_1.write_text(content_1)

    param_file_2 = tmp_path / "param2.txt"
    content_2 = """
    // CMT01 // Boreal Black Spruce
    2.0               // rhq10:
    // CMT02 // Boreal White Spruce Forest
    2.0               // rhq10:
    // CMT03 // Boreal Deciduous Forest
    2.0               // rhq10:
    // CMT40 // Shrub Tundra Kougarok
    2.0               // rhq10:
    // CMT44 // Shrub Tundra Kougarok
    2.0               // rhq10:
    """
    param_file_2.write_text(content_2)

    param_file_3 = tmp_path / "param3.txt"
    content_3 = """
    // CMT02 // Boreal White Spruce Forest
    2.0               // rhq10:
    // CMT03 // Boreal Deciduous Forest
    2.0               // rhq10:
    // CMT40 // Shrub Tundra Kougarok
    2.0               // rhq10:
    // CMT44 // Shrub Tundra Kougarok
    2.0               // rhq10:
    """
    param_file_3.write_text(content_3)

    expected_output = [1, 2, 3, 40, 44]
    assert get_available_CMTs(tmp_path) == expected_output, "The available CMTs do not match the expected list of CMT numbers."
