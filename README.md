# air-quality-dashboard
🌍 中国城市空气质量可视化平台（Dash 实现）
📊 项目简介
本项目是一个基于 Dash 框架构建的交互式可视化系统，展示了中国部分城市在2025年5月26日16时 的实时空气质量数据。用户可以根据城市选择、AQI 区间动态查看污染物之间的关系。

📁 数据来源
数据文件：cleaned_air_quality.csv

原始来源：环境监测平台公开数据

包含字段：城市、省份、PM2.5、PM10、SO2、NO2、CO、O3、AQI 等

🚀 功能特色
城市选择：下拉菜单快速切换城市

AQI 范围筛选：滑动条交互式过滤数据

动态图表：展示 AQI 与主要污染物关系
📦 环境依赖
请使用 Python 安装以下依赖：
pip install -r requirements.txt

▶️ 本地运行
python app.py
然后在浏览器打开：
http://127.0.0.1:8050

在线URL：https://air-quality-dashboard-8g9j.onrender.com

📄 项目文件结构
dash_air_quality/

├── app.py                    # 主程序

├── requirements.txt          # 依赖包

├── cleaned_air_quality.csv   # 清洗后的空气质量数据

└── README.md                 # 项目说明文档
