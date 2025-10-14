# 🎨 个人作品集

一个简洁优雅的个人作品集网站，适合艺术/设计类专业学生展示作品。

## ✨ 特点

- 📸 **个人简介**：照片 + 关于我
- 🏷️ **分类展示**：项目按 category 自动分类
- 🎴 **卡片布局**：首页展示标题图、标题、描述
- 📄 **详情页面**：点击卡片查看完整图文内容
- 📱 **响应式设计**：完美适配桌面和移动设备
- 🎯 **简洁美观**：专注于作品本身

## 🌐 在线演示

查看示例页面：[https://portfolio-example.qbb.moe](https://portfolio-example.qbb.moe)

## 🚀 快速开始

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm dev

# 构建生产版本
pnpm build
```

## 📝 使用指南

### 1. 修改个人信息

编辑 `src/assets/profile.json` 文件

### 2. 添加项目

编辑 `src/assets/projects/example.json`，每个项目包含：

- `category`: 分类（自动分组）
- `title`: 项目标题
- `titleImage`: 标题图（首页显示）
- `description`: 项目描述（首页显示）
- `main`: 详细内容数组（详情页显示）

### 3. 上传照片

将照片放到 `public/images/` 目录

**详细说明请查看：**

- [使用说明.md](./使用说明.md) - 基础使用教程
- [项目结构说明.md](./项目结构说明.md) - 完整技术文档

## 🛠️ 技术栈

- Vue 3 + Vite
- Vue Router 4
- JavaScript (ES6+)
- CSS3

## 📖 IDE 推荐

- [VS Code](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
