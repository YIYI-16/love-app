# 数据更新指南

本指南说明如何在Vercel部署的应用中更新图片和时间线等数据文件。

## 更新方法

### 方法1：通过GitHub更新（推荐）

这是最安全的方法，每次更新都会触发Vercel自动重新部署。

#### 更新图片步骤：
1. **添加新图片到本地项目**
   ```bash
   # 将新图片复制到 static/images/ 目录
   cp /path/to/your/new-photo.jpg static/images/
   ```

2. **提交更改到GitHub**
   ```bash
   git add static/images/new-photo.jpg
   git commit -m "添加新照片：new-photo.jpg"
   git push origin master
   ```

3. **等待Vercel自动部署**
   - Vercel会自动检测GitHub的更改
   - 大约1-2分钟后部署完成
   - 刷新网站即可看到新图片

#### 更新JSON数据文件步骤：
1. **编辑数据文件**
   ```bash
   # 编辑相应的JSON文件
   # static/data/countdown.json - 倒计时
   # static/data/timeline.json - 时间线
   # static/data/locations.json - 地图位置
   # static/data/wishlist.json - 愿望清单
   # static/data/timers.json - 计时器
   ```

2. **提交更改**
   ```bash
   git add static/data/your-file.json
   git commit -m "更新时间线数据"
   git push origin master
   ```

### 方法2：直接编辑GitHub文件（快速更新）

1. **访问GitHub仓库**
   - 打开 https://github.com/YIYI-16/love-app
   - 导航到要编辑的文件

2. **编辑文件**
   - 点击文件右上角的"编辑"图标（铅笔图标）
   - 直接修改文件内容
   - 填写提交信息
   - 点击"Commit changes"

3. **等待自动部署**
   - Vercel会自动重新部署
   - 无需本地操作

## 数据文件格式说明

### 倒计时文件 (countdown.json)
```json
{
    "target_date": "2025-08-15T14:00:00",
    "title": "下次见面",
    "description": "期待与你相见"
}
```

### 时间线文件 (timeline.json)
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

### 地图位置文件 (locations.json)
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

### 愿望清单文件 (wishlist.json)
```json
{
    "items": [
        {
            "id": 1,
            "title": "一起去旅行",
            "description": "去一个美丽的地方",
            "completed": false
        }
    ]
}
```

### 计时器文件 (timers.json)
```json
{
    "timers": [
        {
            "id": 1,
            "title": "在一起天数",
            "target_date": "2023-01-01",
            "is_countdown": false
        }
    ]
}
```

## 图片管理最佳实践

### 图片命名规范
- 使用有意义的文件名：`first-date.jpg`, `birthday-2024.jpg`
- 避免特殊字符和空格
- 保持一致的命名风格

### 图片优化建议
- 图片大小：建议不超过2MB
- 格式：优先使用JPG（照片）和PNG（图标）
- 分辨率：宽度不超过2000像素

### 批量添加图片
如果需要添加多张图片，可以使用以下命令：
```bash
# 将多张图片复制到images目录
cp /path/to/photos/*.jpg static/images/

# 批量提交
git add static/images/
git commit -m "添加多张新照片"
git push origin master
```

## 实时更新功能

### 愿望清单实时更新
愿望清单页面支持实时更新完成状态，无需重新部署：
- 在网站上勾选/取消勾选项目
- 状态会自动保存到JSON文件
- 其他用户刷新页面后可以看到更新

### 其他数据的更新
对于时间线、地图位置等数据，需要：
1. 更新JSON文件
2. 提交到GitHub
3. 等待Vercel重新部署（约1-2分钟）

## 故障排除

### 图片不显示？
1. 检查文件名是否正确
2. 确认图片已添加到GitHub
3. 检查浏览器控制台是否有404错误

### JSON格式错误？
1. 使用JSON验证工具检查格式
2. 确保引号、逗号正确
3. 避免尾随逗号

### 更改不生效？
1. 确认已成功推送到GitHub
2. 检查Vercel部署状态
3. 清除浏览器缓存后重试

## 自动化脚本（可选）

如果您经常更新数据，可以创建简单的更新脚本：

### update_data.sh
```bash
#!/bin/bash
# 更新数据并部署
git add .
git commit -m "数据更新 $(date)"
git push origin master
echo "更新已提交，等待Vercel部署..."
```

使用方式：
```bash
chmod +x update_data.sh
./update_data.sh
```

## 总结

- **小更新**：直接通过GitHub网页编辑
- **大更新**：本地修改后推送到GitHub
- **图片更新**：添加到static/images目录后推送
- **自动部署**：每次推送后Vercel自动重新部署

通过这种方式，您可以轻松地维护和更新您的应用内容！
