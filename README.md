# Crawl4AI - 网页内容爬取与分析工具

Crawl4AI是一个强大的网页内容爬取与分析工具，它结合了现代网页爬虫技术和大语言模型的分析能力，能够自动提取和分析网页内容，生成结构化的分析结果。

## 功能特点

- **自动网页爬取**：使用Playwright技术，能够处理现代JavaScript渲染的网页
- **智能内容分析**：利用DeepSeek API对爬取内容进行智能分析
- **结构化输出**：以JSON格式输出分析结果，包括标题、作者、日期、来源、关键词和摘要
- **简洁美观的用户界面**：提供直观的Web界面，方便用户输入URL并查看分析结果
- **原始内容查看**：支持查看爬取的原始内容，便于对比分析结果

## 技术栈

- **后端**：Python、Flask、AsyncIO
- **爬虫**：Playwright
- **分析**：DeepSeek API
- **前端**：HTML、CSS、JavaScript
- **依赖管理**：pip

## 安装与使用

### 前提条件

- Python 3.8+
- DeepSeek API密钥

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/yourusername/crawl4ai.git
cd crawl4ai
```

2. 安装依赖
```bash
pip install -r requirements.txt
playwright install
```

3. 创建.env文件并添加DeepSeek API密钥
```
DEEPSEEK_API_KEY=your_api_key_here
```

4. 运行应用
```bash
python app.py
```

5. 在浏览器中访问 http://127.0.0.1:5000

### 使用方法

1. 在输入框中输入要分析的网页URL
2. 点击"分析"按钮
3. 等待分析完成后，查看分析结果和原始内容

## 项目结构

```
crawl4ai/
├── main.py          # 核心爬取和分析功能
├── app.py           # Flask Web应用
├── templates/       # HTML模板
│   └── index.html   # 主页面模板
├── static/          # 静态资源
│   ├── css/         # CSS样式
│   │   └── style.css
│   └── js/          # JavaScript脚本
│       └── main.js
└── requirements.txt # 项目依赖
```

## 示例分析结果

```json
{
  "文章标题": "上半年海南州经济运行情况分析",
  "作者信息": "贵南统计微讯",
  "发布日期": "2024-07-30",
  "来源网站": "贵南统计微讯",
  "主要话题和关键词": [
    "海南州经济",
    "GDP增长",
    "三次产业",
    "固定资产投资",
    "消费市场"
  ],
  "文章摘要": "文章分析了2024年上半年海南州经济运行情况，指出全州GDP同比增长6.1%，增速居全省首位。供给端三次产业同步增长，其中工业增加值增长18.7%，清洁能源发电行业贡献显著；消费市场降幅收窄但不及预期，固定资产投资降幅持续收窄。财政收入由负转正，城乡居民收入差距缩小，但工业对电力行业依赖度高、大项目有效投资率降低、消费市场疲软等问题仍需关注。文章建议加强企业培育、项目推进、本地建筑业扶持及消费促进措施，以巩固经济向好态势。"
}
```

## 贡献指南

欢迎对本项目提出建议和改进！请遵循以下步骤：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个Pull Request

## 许可证

本项目采用MIT许可证 - 详情请参见LICENSE文件

## 致谢

- DeepSeek API提供强大的内容分析能力
- Playwright提供现代网页爬取技术支持

---

© 2025 CeiZhu. 保留所有权利。
