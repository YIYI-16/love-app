# Love App - 情侣纪念网站

一个基于Flask的情侣纪念网站，包含倒计时、相册、时间线、地图和愿望清单等功能。

## 功能特性

### 🎯 倒计时功能
- 显示下次见面的倒计时
- 支持自定义目标日期和描述

### 📸 相册功能
- 展示情侣照片
- 自动扫描static/images目录下的图片
- 支持PNG、JPG、JPEG格式

### 📅 时间线功能
- 记录重要时刻的时间线
- 展示情侣关系中的重要事件

### 🗺️ 地图功能
- 智能IP检测，自动选择地图服务
- 国内用户使用高德地图，国外用户使用Google地图
- 标记情侣去过的重要地点

### 📝 愿望清单
- 创建和管理共同的愿望清单
- 标记已完成的项目
- 实时更新状态

## 技术栈

- **后端框架**: Flask 2.3.2
- **前端**: HTML5, CSS3, JavaScript
- **地图服务**: 高德地图 / Google Maps
- **IP检测**: ip-api.com + 纯真IP库

## 安装和运行

### 环境要求
- Python 3.7+
- pip

### 安装步骤

1. 克隆项目
```bash
git clone https://github.com/YIYI-16/love-app.git
cd love-app
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python app.py
```

4. 访问网站
打开浏览器访问: http://localhost:520

### 配置说明

#### 数据文件配置
项目使用JSON文件存储数据，位于`static/data/`目录：

- `countdown.json`: 倒计时配置
- `timeline.json`: 时间线数据
- `locations.json`: 地图位置数据
- `wishlist.json`: 愿望清单数据
- `timers.json`: 多个计时器数据

#### 图片管理
- 将图片放入`static/images/`目录
- 支持格式: PNG, JPG, JPEG
- 相册页面会自动扫描并显示所有图片

## 项目结构

```
love-app/
├── app.py                 # 主应用文件
├── requirements.txt       # Python依赖
├── README.md             # 项目说明
├── static/               # 静态资源
│   ├── data/            # 数据文件
│   └── images/          # 图片文件
└── templates/           # HTML模板
    ├── base.html        # 基础模板
    ├── index.html       # 首页
    ├── gallery.html     # 相册页面
    ├── timeline.html    # 时间线页面
    ├── map.html         # 地图页面
    ├── wishlist.html    # 愿望清单页面
    └── timers.html      # 计时器页面
```

## 自定义配置

### 修改倒计时日期
编辑`static/data/countdown.json`:
```json
{
    "target_date": "2025-08-15T14:00:00",
    "title": "下次见面",
    "description": "期待与你相见"
}
```

### 添加时间线事件
编辑`static/data/timeline.json`:
```json
{
    "events": [
        {
            "date": "2023-01-01",
            "title": "第一次相遇",
            "description": "我们第一次见面的日子",
            "icon": "heart"
        }
    ]
}
```

### 添加地图位置
编辑`static/data/locations.json`:
```json
{
    "locations": [
        {
            "name": "第一次约会的地方",
            "lat": 39.9042,
            "lng": 116.4074,
            "description": "我们第一次约会的美好回忆"
        }
    ]
}
```

## 部署说明

### 本地部署
直接运行`python app.py`即可启动开发服务器。

### 生产环境部署
建议使用WSGI服务器如Gunicorn：
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:520 app:app
```

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

MIT License

## 联系方式

如有问题请联系项目维护者。

---

*用心记录每一份美好，让爱在时光中永恒*
