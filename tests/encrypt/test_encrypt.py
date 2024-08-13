from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError) as excinfo:
        encrypt_message("Message", "3")
    assert str(excinfo.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as excinfo:
        encrypt_message(123, 3)
    assert str(excinfo.value) == "tipo inválido para message"

    assert encrypt_message("reversed", -1) == "desrever"
    assert encrypt_message("reversed", 9) == "desrever"

    assert encrypt_message("secret", 3) == "ces_ter"
    assert encrypt_message("secret", 4) == "te_rces"
