# 🚀 B站图床403问题 - 快速修复指南

## ⚡ 快速解决方案（推荐）

### 方案1: 使用 Python 脚本自动下载（最稳定）

```bash
# 1. 安装依赖（如果还没安装）
pip install requests

# 2. 运行下载脚本
python download_images.py

# 3. 完成！图片已下载到本地，JSON已自动更新
```

### 方案2: 测试当前的 referrerpolicy 方案

```bash
# 启动开发服务器
pnpm dev

# 打开浏览器访问，检查图片是否正常显示
```

**已实施的修复：**
- ✅ 在 `<img>` 标签添加 `referrerpolicy="no-referrer"`
- ✅ 在 `index.html` 添加 `<meta name="referrer" content="no-referrer">`
- ✅ 添加图片加载错误处理

## 🔍 如何测试

1. **打开浏览器开发者工具** (F12)
2. **切换到 Network 标签**
3. **刷新页面**
4. **查找图片请求**
   - ✅ 状态码 200 = 成功
   - ❌ 状态码 403 = 需要使用方案1下载到本地

## 📋 手动下载单张图片

如果只需要下载某张图片：

### Windows PowerShell:
```powershell
# 使用 curl（Windows 10+自带）
curl -H "Referer: https://www.bilibili.com" `
     "http://i0.hdslb.com/bfs/new_dyn/568c13edcb98a767148ad41f2eec13db22113127.jpg" `
     -o public/images/image1.jpg
```

### 使用浏览器:
1. 访问 https://www.bilibili.com
2. 打开开发者工具 (F12)
3. 在 Console 中执行：
```javascript
fetch('http://i0.hdslb.com/bfs/new_dyn/568c13edcb98a767148ad41f2eec13db22113127.jpg')
  .then(r => r.blob())
  .then(blob => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'image.jpg';
    a.click();
  });
```

## 🎯 推荐流程

### 开发阶段：
1. ✅ 使用 `referrerpolicy="no-referrer"` (已配置)
2. ✅ 在开发环境测试

### 准备发布：
1. 📥 运行 `python download_images.py` 下载所有图片
2. ✅ 图片自动保存到 `public/images/projects/`
3. ✅ JSON 文件自动更新为本地路径
4. 🚀 部署到服务器

## ❓ 常见问题

### Q1: Python 脚本下载失败怎么办？
**A:** 检查网络连接，或使用浏览器方法手动下载

### Q2: 我不想使用 Python，有其他方法吗？
**A:** 可以使用图片代理服务，参考 `IMAGE_SOLUTION.md` 中的方案2

### Q3: referrerpolicy 方案在我的浏览器不工作
**A:** 可能是浏览器版本较旧，建议使用方案1下载到本地

### Q4: 图片下载后如何更新 JSON？
**A:** Python 脚本会自动更新，或手动修改 example.json 中的 image 路径：
```json
{
  "image": "/images/projects/project0_item0.jpg"
}
```

## 📚 更多详细信息

查看 `IMAGE_SOLUTION.md` 了解所有解决方案的详细对比和实现方法。

