import pytest

from scripts.util.param import get_CMTs_in_file, parse_header_line, CMT


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
