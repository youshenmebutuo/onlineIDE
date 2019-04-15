import os
class Settings:
    """存储IDE所有设置的类"""

    def __init__(self):
        """IDE设置"""
        self.port: int = 8888
        self.dir_path ="files/"