from yourmodule.agent_activity import AgentActivity

def test_soft_backchannel():
    a = object.__new__(AgentActivity)  # bypass __init__
    a._soft_ignore_words = {"yeah", "ok", "hmm", "right"}
    a._hard_interrupt_words = {"stop", "wait", "hold", "pause"}

    assert a._is_soft_backchannel("yeah") is True
    assert a._is_soft_backchannel("ok ok") is True
    assert a._is_soft_backchannel("hmm") is True

    assert a._is_soft_backchannel("yeah wait") is False
    assert a._is_soft_backchannel("stop") is False


def test_hard_intent():
    a = object.__new__(AgentActivity)
    a._soft_ignore_words = {"yeah", "ok", "hmm", "right"}
    a._hard_interrupt_words = {"stop", "wait", "hold", "pause"}

    assert a._contains_hard_interrupt_intent("stop") is True
    assert a._contains_hard_interrupt_intent("wait") is True
    assert a._contains_hard_interrupt_intent("hold on") is True

    assert a._contains_hard_interrupt_intent("yeah") is False
    assert a._contains_hard_interrupt_intent("hmm") is False
