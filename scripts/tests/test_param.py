from scripts.util.param import get_CMTs_in_file


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
        {'cmtkey': 'CMT01', 'cmtnum': 1, 'cmtname': 'Boreal Black Spruce', 'cmtcomment': ''},
        {'cmtkey': 'CMT02', 'cmtnum': 2, 'cmtname': 'Boreal White Spruce Forest', 'cmtcomment': ''},
        {'cmtkey': 'CMT03', 'cmtnum': 3, 'cmtname': 'Boreal Deciduous Forest', 'cmtcomment': ''},
        {'cmtkey': 'CMT44', 'cmtnum': 44, 'cmtname': 'Shrub Tundra Kougarok', 'cmtcomment': ''}
    ]

    assert cmts_found == expected_cmts, "The CMTs found do not match the expected CMTs."
