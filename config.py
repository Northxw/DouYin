# -*- coding:utf-8 -*-


# 多设备相同驱动参数
PLANTFORM = 'Android'
APP_PACKAGE = 'com.ss.android.ugc.aweme'
APP_ACTIVITY = '.main.MainActivity'
PLANTFORM_VERSION = '4.4.2'
DEVICE_UDID = ('127.0.0.1:62026', '127.0.0.1:62025', '127.0.0.1:62001')

# SERVER
DRIVER_SERVERS = "http://localhost:4723/wd/hub"

# XPATH_FOR_PORT-62026
USER_XPATH = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout'

USER_XPATH_ = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]"
# 加载超时时间
TIMEOUT = 20

# 点击时间间隔
CLICK_TIME = 2
