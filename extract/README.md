docker版本： 19.03.12

如果版本不对，加载容器的时候会出错

docker仓库：https://hub.docker.com/r/cwaffles/openpose

docker常用指令：https://www.runoob.com/docker/docker-tutorial.html

**step1:安装docker**

使用官方安装脚本自动安装

```
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

手动安装

参考链接：https://www.runoob.com/docker/ubuntu-docker-install.html

**step2:安装NVIDIA CONTAINER RUNTIME**

新建一个脚本文件 `vim nvidia.sh` 填入如下内容

```
sudo curl -s -L https://nvidia.github.io/nvidia-container-runtime/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
sudo curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
sudo apt-get update
```

执行脚本

```
sh nvidia.sh
```

安装 nvidia-container-runtime

```
sudo apt-get install nvidia-container-runtime
```

**step3:创建用户组，方便授权**

如果没有sudo权限，可以创建dockers权限组

```
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart
newgrp - docker    //将当前用户以docker用户组的身份再次登录系统
```

通过`cat /etc/group`可以查看用户组信息

**step4:下载镜像，对应cuda10.0,cudnn7.0**

```
docker pull cwaffles/openpose
```

通过镜像创建容器（以下命令执行结束之后自动进入容器）

```
sudo docker run --gpus all --name openpose -it cwaffles/openpose:latest /bin/bash
```

进入容器内部(创建成功会自动进入容器)

```
docker exec -it openpose /bin/bash
```

注：还可以使用以下命令一次删除所有停止的容器。

```
docker rm $(docker ps -a -q)
```

**step5:测试openpose的demo（先测试nvidia是否好用）**

```
＃only body./build/examples/openpose/openpose.bin --video examples/media/video.avi --write_json output/ --display 0 --render_pose 0#Body + face + hands./build/examples/openpose/openpose.bin --video examples/media/video.avi --write_json output/ --display 0 --render_pose 0 --face --hand
```

**step6: 使用docker提取数据集骨骼点**

接下来可以看一下docker容器的共享文件夹来拷贝数据集，第一个命令不常用，直接参考第二和第三个命令。如果需要挂载多个目录就使用多个-v

```
docker run -it -v  /宿主机绝对路径目录:  /容器内目录  镜像名docker run -idt -v --name openpose  /home/$USER/share:/openpose/share cwaffles/openpose:latest    //后台运行docker exec -it  openpose /bin/bash //进入容器
```

docker内部安装vim

```
apt-get updateapt-get install vim
```

挂载数据集

```
exit//退出容器docker run -v  /home/$USER/share:/openpose/share cwaffles/openpose:latest
```

如果要使用vscode或者pycharm进行调试，参考https://blog.csdn.net/lifengss/article/details/105300459，将docker的端口映射到宿主机上面。

```
docker run -itd --gpus all --name openpose -p 8022:22 -v /home/laoguihong/workplace:/openpose/share/code -v /share/openpose:/openpose/data cwaffles/openpose:latest
```

##### 安装python相关包

pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

**报错ffmpeg**

apt-get update && apt-get install ffmpeg