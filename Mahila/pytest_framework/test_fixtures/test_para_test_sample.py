import pytest

@pytest.mark.parametrize("username , password" ,
                         [('user1','pass1'),
                        ('user2','pass2')])
def test_login_screen(username,password):
    print("credentials :", username ,password)
