from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    expect = {"title", "salary", "type"}
    assert all(set(job.keys()) == expect for job in result) is True
