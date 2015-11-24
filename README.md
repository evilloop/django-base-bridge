# [ Django base bridge ]

# 功能概述

放在我们应用和django内部框架之间的桥接基类，目的是在不修改django源码的情况下可以定制某些模块。

# 依赖

* Python (2.7.X)
* Django (1.7)

# 安装

    # 克隆代码到本地
        
        git clone https://github.com/evilloop/django-base-bridge
        
    # 进入目录
        
        cd django-base-bridge
        
    # 三步安装法
        python setup.py config
        python setup.py build
        python setup.py install

# 用法

    db
    ===
    重新封装了一层原来的Model和fields，便于定制
    
    from base_bridge.db import models


    class Project(models.Model):
        class Meta:
            verbose_name = verbose_name_plural = u'Project'
    
        name = models.CharField(verbose_name=u'名称')
        desc = models.TextField(verbose_name=u'描述')

    views
    ===
    视图装饰器，记录日志和异常处理
    
    View装饰器，调用之前需要重写以下函数：
    - request_pre_process
    - request_exception_process

    from base_bridge.views.decorators import BaseDecorator
    class BeforeView(BaseDecorator):
        @classmethod
        def request_pre_process(cls, request):
            '''
            Do something
            '''
            pass

        @classmethod
        def request_exception_process(cls, request, e):
            '''
            Do something
            '''
            pass

    @BeforeView.catch_exception_without_parameters
    def some_view(request):
        pass