1\ 修改pip 安装目录
python -m site
D:\2_PYTHON\Lib
USER_SITE和USER_BASE
    USER_SITE = r"D:\2_PYTHON\Lib\site-packages"
    USER_BASE = r"D:\2_PYTHON\Scripts"


-- JITTOR_HOME   C:\Users\zhwst\.cache\jittor

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

修改PIP源
C:\Users\zhwst\AppData\Roaming\pip\pip.ini

    [global]
    timeout=40
    index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
    extra-index-url=
            http://mirrors.aliyun.com/pypi/simple/
            http://pypi.douban.com/simple
            http://pypi.mirrors.ustc.edu.cn/simple/

    [install]
    trusted-host=
            pypi.tuna.tsinghua.edu.cn
            mirrors.aliyun.com
            pypi.douban.com
            pypi.mirrors.ustc.edu.cn


            python cli_demo.py [chatglm|pangualpha|llama|chatrwkv]
            python cli_demo.py  chatglm
                     protobuf == 3.20.3
                     pip install lxml==4.6.4
            pip install streamlit
            pip install --upgrade --force-reinstall tensorflow
----------------------
https://blog.csdn.net/yutingwu816/article/details/128190030

https://cg.cs.tsinghua.edu.cn/jittor/assets/build/DockerToolbox-19.03.1.exe


--------------------

https://rancherdesktop.io/
（C:\Users\username  .condarc
改变conda虚拟环境的默认路径
envs_dirs:
  - D:\Anaconda3\envs
pkgs_dirs:
  - D:\Anaconda3\pkgs
  
  https://zhuanlan.zhihu.com/p/34612778/
