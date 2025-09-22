# Vercel 部署指南

本指南将帮助您将Flask应用部署到Vercel平台。

## 部署步骤

### 方法1：通过GitHub连接部署（推荐）

1. **访问Vercel官网**
   - 打开 https://vercel.com
   - 使用GitHub账号登录

2. **导入项目**
   - 点击"New Project"
   - 选择"Import Git Repository"
   - 选择您的 `YIYI-16/love-app` 仓库

3. **配置项目**
   - Framework Preset: 选择"Other"
   - Root Directory: 保持默认
   - Build Command: 留空
   - Output Directory: 留空

4. **环境变量（可选）**
   - 通常不需要额外配置
   - 如果需要，可以添加环境变量

5. **部署**
   - 点击"Deploy"
   - 等待部署完成

### 方法2：使用Vercel CLI部署

1. **安装Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **登录Vercel**
   ```bash
   vercel login
   ```

3. **部署项目**
   ```bash
   vercel
   ```

4. **按照提示操作**
   - 选择当前目录
   - 选择默认设置
   - 确认部署

## 项目配置说明

### vercel.json 配置
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    },
    {
      "src": "static/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

### WSGI入口点
- 文件位置: `api/index.py`
- 作用: Vercel使用此文件作为Python应用的入口点

## 部署后的访问

部署成功后，您将获得一个类似以下的URL：
```
https://your-app-name.vercel.app
```

您可以通过此URL访问您的应用。

## 常见问题

### Q: 部署后出现404错误？
A: 检查vercel.json配置是否正确，确保路由配置正确。

### Q: 静态文件无法加载？
A: 确保static目录下的文件路径正确，vercel.json中已配置静态文件路由。

### Q: Python依赖安装失败？
A: 检查requirements.txt文件格式是否正确。

### Q: 如何更新部署？
A: 推送新的提交到GitHub主分支，Vercel会自动重新部署。

## 自定义域名（可选）

如果您有自己的域名，可以在Vercel控制台中配置：
1. 进入项目设置
2. 选择"Domains"
3. 添加您的域名
4. 按照提示配置DNS记录

## 监控和日志

- 在Vercel控制台查看部署状态
- 查看实时日志和错误信息
- 监控应用性能

## 注意事项

1. **免费额度**: Vercel提供免费的部署额度，适合个人项目
2. **自动部署**: 每次推送到GitHub主分支都会触发自动部署
3. **环境变量**: 敏感信息请使用环境变量，不要硬编码在代码中
4. **文件大小限制**: 注意静态文件大小限制

## 技术支持

如果遇到部署问题，可以：
- 查看Vercel官方文档
- 检查部署日志
- 在GitHub Issues中提问

---

部署成功后，您的Flask应用将可以通过互联网访问，无需自己维护服务器！
