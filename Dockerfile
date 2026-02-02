# 使用官方 PyTorch 镜像
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# 设置环境变量避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装基础工具和 Python 包管理依赖
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 升级 pip
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip

# 安装 scikit-learn
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ dgl scikit-learn

# 可选：安装其他常用库
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ pandas numpy matplotlib jupyter

# 设置工作目录
WORKDIR /app

# 默认启动命令（可选）
CMD ["bash"]
