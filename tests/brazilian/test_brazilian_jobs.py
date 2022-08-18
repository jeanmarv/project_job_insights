from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    data = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for jobs in data:
        assert "title" in jobs
        assert "salary" in jobs
        assert "type" in jobs
