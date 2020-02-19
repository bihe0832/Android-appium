#coding:utf-8
class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

appium_const = _const()
appium_const.IMPLICITLY_WAIT_SHORT=5
appium_const.IMPLICITLY_WAIT_MIDDLE=10
appium_const.IMPLICITLY_WAIT_LONG=20
appium_const.HOST = '127.0.0.1'
appium_const.FIRST_PORT=4725
appium_const.QYWORK = ""

zixie_const = _const()
zixie_const.WECHAT_ID= ""
zixie_const.WECHAT_PASSWORD = ""
zixie_const.TEMP_UUID="4fb845e3"
zixie_const.TEMP_PORT=4725



