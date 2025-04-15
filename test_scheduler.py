from core.scheduler import Scheduler

def test_scheduler_order():
    s = Scheduler(["url1", "url2"])
    assert s.get_next() == "url1"
    assert s.get_next() == "url2"