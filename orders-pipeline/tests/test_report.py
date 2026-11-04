from pipeline.report import format_report


def test_format_report_lists_each_store():
    text = format_report({"Mumbai": 25000, "Delhi": 6000})
    assert "Mumbai: 25000" in text and "Delhi: 6000" in text
