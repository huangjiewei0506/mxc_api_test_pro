
import pytest

#此文件用来作为运行用例的脚本入口

# 指定参数和路径
# （1）‘-s’：关闭捕捉，输出打印信息。
# （2）‘-v’:用于增加测试用例的冗长。
# （3）‘-k’ ：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行XX.py中包含add的测试用例。
# （4）‘q’:减少测试的运行冗长。
# （5）‘-x’:出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。

if __name__ == '__main__':
    #运行指定的py文件下的所有用例，并打印信息。
    #pytest.main(['-vs','./case/core/test_core.py'])


    #加多一行注释，提交到git
    pytest.main(['-v'])

    #运行test_core.py中TestCore类里面名字为test_core01的测试用例
    #pytest.main(['./case/core/test_core.py::TestCore::test_core01'])

    #以带参数的形式运行某个文件下的某个用例，这种方式可以打印出详细的结果
    #pytest.main(['-vs','./case/core/test_core.py::TestCore::test_core01'])


