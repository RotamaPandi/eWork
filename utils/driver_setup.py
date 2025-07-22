from appium import webdriver

def init_driver():
    desired_caps = {
      "platformName": "Android",
      "appium:automationName": "UiAutomator2",
      "appium:deviceName": "emulator-5554",
      "appium:appPackage": "id.edot.ework",
      "appium:appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity",
      "appium:noReset": True
    }

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)