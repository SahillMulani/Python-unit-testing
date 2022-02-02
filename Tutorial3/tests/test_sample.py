import sys

from Tutorial3.myapp.sample import add
import pytest

# @pytest.mark.skip(reason="just wanna skip it")
# def test_add_num():
#     assert add(1,2) == 3
#
# @pytest.mark.skipif(sys.version_info > (3,7) , reason="use python 3.7 or less")
# def test_add_str():
#     assert  add("x","y") == "xy"
#
#
# @pytest.mark.xfail(sys.platform == "win32" , reason = "don't run on windows 32 machine")
# def test_add_num():
#     assert add([1],[2]) == [1,2]
#     raise Exception()

@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])] , ids= ["num","str","list"])
def test_add(a,b,c):
    assert add(a,b) == c