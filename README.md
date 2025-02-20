# 独立博客列表

在算法与流量裹挟的时代，这是一个独立博客的展示平台，让我们一起见证数字世界中的「个人主义」星辰。

![预览图](https://raw.githubusercontent.com/lovexw/blogbase/main/image/homepage.jpg)

## 特性

- 🎨 简洁优雅的界面设计
- 🔄 支持多种排序方式（默认、按名称、随机）
- 🎲 「随机关注」功能助你发现有趣的博客
- 📱 完美适配移动端
- 🔍 支持博客图标显示
- 🏷️ 支持标签分类
- 📰 支持RSS订阅

## 在线演示

访问：[独立博客列表](https://blogbase.xiaowuleyi.com)

## 如何提交你的博客

1. Fork 这个仓库
2. 编辑 `blogs-list.csv` 文件
3. 在文件末尾添加你的博客信息，格式如下：

```csv
博客名称,博客网址,RSS地址,标签(用分号分隔)
```

示例：
```csv
小吴乐意'blog, https://www.xiaowuleyi.com/, https://blog.xiaowuleyi.com/rss.php, 生活随想; 比特币; 商业思考
```

> 注意事项：
> - 博客网址必须以 http:// 或 https:// 开头
> - 如果没有 RSS 地址，请留空，但保留逗号
> - 标签之间使用分号(;)分隔，建议使用3-5个标签
> - 网站图标（favicon）会自动从您的网站根目录获取，请确保您的网站已正确配置 favicon.ico 或在 HTML 头部设置了正确的图标链接

4. 提交 Pull Request

### 收录标准

- 必须是个人独立博客
- 博客内容必须是原创为主
- 博客需要稳定运行，无法访问的会被移除
- 博客需要在近期有更新，超过一年未更新的会被移除
- 拒绝收录商业网站、公司网站

## 部署到 Cloudflare Pages

你可以轻松部署一个自己的独立博客展示站：

1. Fork 这个仓库到你的 GitHub 账号

2. 登录到 [Cloudflare Pages](https://pages.cloudflare.com)

3. 创建新项目，选择「Connect to Git」

4. 选择你 Fork 的仓库

5. 设置部署配置：
   - 构建命令：留空
   - 输出目录：留空
   - 环境变量：无需设置

6. 点击「Save and Deploy」

几分钟后，你的站点就会自动部署完成。每次你更新仓库内容，Cloudflare Pages 都会自动重新部署。

## 本地预览

```bash
# 使用 Python
python -m http.server 8000

# 或使用 Node.js
npx http-server

# 或使用 PHP
php -S localhost:8000
```

然后访问 `http://localhost:8000`

## 贡献

欢迎提交 Pull Request 来完善这个项目。你可以：

- 添加新的博客
- 改进界面设计
- 添加新功能
- 修复 bug
- 改进文档

## 许可

MIT License

## 致谢

感谢所有独立博主们的坚持。正是你们的存在，让这个互联网依然保持着活力与独特的个人色彩。

---

> 流量终将退潮，但记录与分享的热情永不熄灭。
