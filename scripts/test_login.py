"""
登录，测试用例
"""
from common.utils import init_driver
from page.page_factory import PageFactory


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = init_driver()  # 驱动对象获取
        self.page_factory = PageFactory(self.driver)  # 工厂类实例化

    def teardown_class(self):
        self.driver.quit()  # 退出驱动对象

    def test_login(self):
        """测试登录方法"""
        self.page_factory.home_page().click_mine()  # 点击我的
        self.page_factory.mine_page().click_login()  # 点击登录注册
        self.page_factory.login_page().input_username("13058070271")  # 输入账号
        self.page_factory.login_page().input_username("zm4567890")  # 输入密码
        self.page_factory.login_page().click_login_btn()  # 点击登录
        self.page_factory.login_page().click_con_btn()  # 点击确认
        nick_name = self.page_factory.login_page().get_nick_name()  # 获取昵称
        print("昵称是：", nick_name)
        # 断言判断结果
