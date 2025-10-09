# B站图床防盗链解决方案

## 问题说明

B站图床 (`i0.hdslb.com`) 会检查 HTTP Referer 头，当从外部网站访问时返回 **403 Forbidden** 错误。

## ✅ 已实施的解决方案

### 1. 使用 `referrerpolicy="no-referrer"` (推荐，已添加)

在 `<img>` 标签中添加 `referrerpolicy="no-referrer"` 属性，不发送 Referer 头：

```html
<img 
  src="http://i0.hdslb.com/bfs/new_dyn/xxx.jpg" 
  referrerpolicy="no-referrer"
  crossorigin="anonymous"
/>
```

**优点**：
- ✅ 最简单的方法，无需后端
- ✅ 浏览器原生支持
- ✅ 已在 ProjectItem.vue 中实现

**缺点**：
- ⚠️ 在某些旧浏览器可能不支持
- ⚠️ B站可能调整策略后失效

## 🔧 其他可选方案

### 2. 使用图片代理服务

通过代理服务器转发图片请求：

#### 方案 A: 使用公共代理服务

```javascript
// 将B站图片URL转换为代理URL
const getProxyUrl = (originalUrl) => {
  return `https://images.weserv.nl/?url=${encodeURIComponent(originalUrl)}`
  // 或使用: https://cors-anywhere.herokuapp.com/${originalUrl}
}
```

#### 方案 B: 自建 Nginx 代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /bilibili-proxy/ {
        proxy_pass https://i0.hdslb.com/;
        proxy_set_header Referer "https://www.bilibili.com";
        proxy_set_header User-Agent "Mozilla/5.0";
        proxy_hide_header Access-Control-Allow-Origin;
        add_header Access-Control-Allow-Origin *;
    }
}
```

然后修改图片URL：
```javascript
const imageUrl = originalUrl.replace(
  'http://i0.hdslb.com/',
  'https://your-domain.com/bilibili-proxy/'
)
```

### 3. 下载图片到本地 (最稳定)

**推荐用于生产环境**

将B站图片下载到项目的 `public/images/` 目录：

```bash
# 使用 curl 下载（设置 Referer）
curl -H "Referer: https://www.bilibili.com" \
     "http://i0.hdslb.com/bfs/new_dyn/568c13edcb98a767148ad41f2eec13db22113127.jpg" \
     -o public/images/image1.jpg
```

或使用 Python 脚本批量下载：

```python
import requests
import json

headers = {
    'Referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

with open('src/assets/projects/example.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for project in data['projects']:
    for idx, item in enumerate(project['main']):
        url = item['image']
        filename = f"public/images/project{project['id']}_item{idx}.jpg"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename, 'wb') as img_file:
                img_file.write(response.content)
            print(f"Downloaded: {filename}")
            # 更新JSON中的URL
            item['image'] = f"/images/project{project['id']}_item{idx}.jpg"
```

**优点**：
- ✅ 最稳定，不受外部限制
- ✅ 加载速度快
- ✅ 完全可控

**缺点**：
- ⚠️ 需要占用本地存储空间
- ⚠️ 需要手动更新图片

### 4. 使用 Meta 标签 (全局方案)

在 `index.html` 中添加：

```html
<meta name="referrer" content="no-referrer">
```

**优点**：
- ✅ 全局生效，一次设置

**缺点**：
- ⚠️ 影响所有请求，可能影响某些需要 Referer 的功能

### 5. 使用 CDN 缓存

通过 Cloudflare Workers 或 Vercel Edge Functions 创建缓存：

```javascript
// Cloudflare Workers 示例
export default {
  async fetch(request) {
    const url = new URL(request.url)
    const imageUrl = url.searchParams.get('url')
    
    const response = await fetch(imageUrl, {
      headers: {
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0...'
      }
    })
    
    const newResponse = new Response(response.body, response)
    newResponse.headers.set('Access-Control-Allow-Origin', '*')
    newResponse.headers.set('Cache-Control', 'public, max-age=86400')
    
    return newResponse
  }
}
```

## 📊 方案对比

| 方案 | 实施难度 | 稳定性 | 速度 | 推荐度 |
|------|---------|--------|------|--------|
| referrerpolicy | ⭐ 简单 | ⭐⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 快 | ✅ 开发环境 |
| 图片代理 | ⭐⭐ 中等 | ⭐⭐⭐⭐ 好 | ⭐⭐⭐ 中等 | ✅ 快速方案 |
| 下载本地 | ⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 最好 | ⭐⭐⭐⭐⭐ 快 | ✅✅ 生产环境 |
| Meta标签 | ⭐ 简单 | ⭐⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 快 | ⚠️ 谨慎使用 |
| CDN缓存 | ⭐⭐⭐⭐ 复杂 | ⭐⭐⭐⭐⭐ 最好 | ⭐⭐⭐⭐⭐ 快 | ✅ 大型项目 |

## 🎯 推荐策略

1. **开发阶段**：使用 `referrerpolicy="no-referrer"` (已实施)
2. **准备上线**：下载图片到本地，更新JSON配置
3. **大型项目**：搭建自己的图片CDN或代理服务

## 🔍 测试当前方案

打开浏览器开发者工具，刷新页面：
- 如果图片正常显示 → 方案生效 ✅
- 如果仍然 403 → 需要使用其他方案（建议下载到本地）

## 📝 相关资源

- [Referrer Policy MDN文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Referrer-Policy)
- [CORS跨域资源共享](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)

