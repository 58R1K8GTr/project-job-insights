from src.pre_built.counter import count_ocurrences


def test_counter():
    result_python = count_ocurrences('data/jobs.csv', 'Python')
    expected_python = 1639
    result_javascript = count_ocurrences('data/jobs.csv', 'Javascript')
    expected_javascript = 122
    assert result_python == expected_python
    assert result_javascript == expected_javascript

