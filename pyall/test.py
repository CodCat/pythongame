import pygame
from settings import Settings

def test_Settings():  
    # 创建Settings对象  
    settings = Settings()  

    # 测试外星人速度设置  
    assert settings.alien_speed_factor == 1  

    # 测试飞船速度设置  
    assert settings.ship_speed_factor == 1.5  

    # 测试子弹速度设置  
    assert settings.bullet_speed_factor == 3  

    # 测试屏幕设置  
    assert settings.screen_width == 1200  
    assert settings.screen_height == 800  

    # 测试随游戏进行而变化的设置  
    settings.increase_speed()  
    assert settings.ship_speed_factor == 1.5 * 1.1  
    assert settings.bullet_speed_factor == 3 * 1.1  
    assert settings.alien_speed_factor == 1 * 1.1  

    # 测试外星人点数设置  
    assert settings.alien_points == 50