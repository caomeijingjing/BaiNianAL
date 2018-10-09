import allure

from Base.base import Base
import Page
class PageLogin(Base):
    # 点击我
    @allure.step('点击我')
    def page_click_me(self):
        self.base_click(Page.me_btn)
    # 点击已有账号，去登录
    @allure.step('点击已有账号，去登录')
    def page_click_info(self):
        self.base_click(Page.user)
    # 输入账号
    @allure.step('输入账号')
    def page_input_user(self,username):
        self.base_input(Page.user_name,username)
    # 输入密码
    @allure.step('输入密码')
    def page_input_pwd(self,password):
        self.base_input(Page.user_pwd,password)
    # 点击登录按钮
    @allure.step('点击登录按钮')
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)
    # 点击设置按钮
    @allure.step('点击设置按钮')
    def page_click_setting(self):
        self.base_click(Page.setting_btn)
    # 滑动 消息推送-->修改密码
    @allure.step('消息推送')
    def page_drag_and_drop(self):
        # 获取 消息推送 元素
        el1=self.base_find_element(Page.msg_send)
        # 获取 修改密码 元素
        el2=self.base_find_element(Page.update_pwd)
        # 调用滑动元素 方法
        self.base_drag_and_drop(el1,el2)
    # 点击退出
    @allure.step('点击退出')
    def page_click_exit(self):
        self.base_click(Page.exit_btn)
    # 确认退出
    @allure.step('确认退出')
    def page_click_exit_ok(self):
        self.base_click(Page.exit_ok)
    # 登录操作步骤封装
    def page_login(self,username,password):
        # 调用点击 我
        self.page_click_me()
        # 点击已有账户去登录
        self.page_click_info()
        # 输入账号
        self.page_input_user(username)
        # 输入密码
        self.page_input_pwd(password)
        # 点击登录
        self.page_click_login_btn()
    # 退出登录封装
    def page_login_logout(self):
        # 点击设置
        self.page_click_setting()
        # 滑动屏幕  消息推送滑到修改密码
        self.page_drag_and_drop()
        # 点击退出按钮
        self.page_click_exit()
        # 确认退出
        self.page_click_exit_ok()
    # 封装 获取nickname方法
    @allure.step('获取nickname')
    def page_get_nickname(self):
        return self.base_get_text(Page.me_nickname)