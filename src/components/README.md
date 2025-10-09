# ProjectItem 组件使用说明

## 功能特点

`ProjectItem` 是一个用于展示项目作品集的 Vue 3 组件，具有以下特点：

### ✨ 主要功能
- 📸 **自动图片排版**：图片与描述采用左右交替的网格布局
- 🔍 **图片预览**：点击图片可在灯箱中查看大图
- 📱 **响应式设计**：完美适配桌面和移动设备
- 🎨 **现代UI**：优雅的悬停效果和过渡动画
- 🔗 **外链支持**：可选的查看原文链接

## 使用方法

### 1. 基本用法

```vue
<script setup>
import { ref } from 'vue'
import ProjectItem from './components/ProjectItem.vue'
import projectsData from './assets/projects/example.json'

const projects = ref(projectsData.projects)
</script>

<template>
  <ProjectItem 
    v-for="project in projects" 
    :key="project.id"
    :project="project"
  />
</template>
```

### 2. 数据格式

JSON 数据结构示例：

```json
{
  "projects": [
    {
      "id": 0,
      "title": "项目标题",
      "main": [
        {
          "title": "作品标题",
          "description": "作品描述文字",
          "image": "图片URL",
          "link": "相关链接（可选）"
        }
      ]
    }
  ]
}
```

### 3. Props

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| project | Object | 是 | 项目对象，包含 id、title 和 main 数组 |

## 功能说明

### 自动排版
- 项目中的图片和描述会自动采用网格布局
- 奇数项：图片在左，描述在右
- 偶数项：图片在右，描述在左
- 移动端：图片和描述垂直排列

### 图片查看
1. 鼠标悬停在图片上会显示放大镜图标
2. 点击图片打开灯箱模式
3. 在灯箱中可查看完整大图
4. 点击背景或关闭按钮退出灯箱

### 响应式特性
- **桌面端（>768px）**：图片和描述并排显示
- **移动端（≤768px）**：图片和描述垂直堆叠

## 样式定制

组件使用 scoped CSS，主要颜色变量：

- 主色调：`#42b883`（Vue 绿）
- 文字颜色：`#2c3e50`（深灰）
- 背景：`#fff`（白色卡片）
- 阴影：自适应悬停效果

可以通过修改组件内的 CSS 变量来自定义样式。

## 注意事项

1. 确保图片 URL 可访问
2. 建议使用合适尺寸的图片以优化加载速度
3. 组件使用 `Teleport` 将灯箱挂载到 body，确保 Vue 3 版本支持
4. 打开灯箱时会禁用 body 滚动，关闭时自动恢复

## 浏览器兼容性

- 现代浏览器（Chrome, Firefox, Safari, Edge）
- 需要支持 CSS Grid 和 ES6+
- Vue 3.x

